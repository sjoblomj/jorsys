#!/usr/bin/env python3
"""Render backed-up forum threads (nested page.json trees) into Incunable-
templated Markdown, one file per thread, preserving reply nesting, plus one
thread-list page per source.

Consumes the page.json files produced under backup/<source>/<board>/<thread>/
and, for each thread, writes an Incunable page directory containing an
index.md that uses the begin-forumthread/end-forumthread and
begin-forumpost/end-forumpost templates (see ../templates/) to represent the
thread and its nested replies. The post body is taken from each post's
content.markdown field, which already contains cleaned Markdown.

Nesting is expressed by literally nesting {{begin-forumpost}}...
{{end-forumpost}} blocks: a reply's block is written inside its parent's
block, right after the parent's own body and before the parent's
{{end-forumpost}}. A post whose own page.json entry is a bare "missing"
stub (no content) gets {{missing-post}} as its body instead.

For each source, also writes a thread-list index.md (begin-threadlist /
begin-existingthreads / begin-missingthreads templates) linking every
successfully fetched thread, followed by a collapsed (CSS-only, via
<details>) list of threads the board's own index once listed but we have no
page.json for. Titles/authors/dates for the fetched list come from each
thread's own page.json; for the missing list they come from the board-wide
.metadata file (adapter.titles / adapter.postinfo), which covers every
thread the board ever listed, fetched or not.

Under every thread entry (fetched or missing alike), a {{replylink}} row is
also emitted for each of its replies, indented by reply depth. Reply
authors/dates come from .metadata's adapter.postinfo too, so these show up
even for threads whose root post itself was never archived. A reply row
links to its post's anchor (#post-<chain>) on the thread page whenever that
specific post is a real, non-"missing" entry in that thread's own
page.json; otherwise (thread not fetched, or that particular post itself
missing within a fetched thread) it stays plain text.
"""
import argparse
import html
import json
import sys
from pathlib import Path

DEFAULT_SOURCES = ["backup/wardraft-forums", "backup/stals"]
DEFAULT_OUTPUT_ROOT = "rendered"


def safe_name(s):
    return "".join("_" if c in '/\\\0' or ord(c) < 32 else c for c in s)


def tmpl_arg(value, nesting=1):
    """Sanitize a value for embedding as a `{{template |key=value}}`
    argument. Incunable's template substituter reads one `{{...}}` call per
    source line and splits its arguments on '|', so a raw newline or an
    unbalanced '|'/'{{'/'}}' in the value would corrupt the call.

    `nesting` counts how many of the substituter's gsub-based ${key}
    substitutions this value's text will pass through before it reaches
    final output: 1 for a value used as a normal, unnested argument; 2 for
    one embedded (raw, via render_highlight) inside another call that is
    itself spliced unescaped into a further call's argument, and so on.
    Each such pass independently applies awk gsub's replacement-text rule
    that a bare "&" means "insert the whole match" -- so a literal "&"
    surviving N passes needs 2**N - 1 backslashes in front of it, not just
    one; one pass's output (e.g. "\\&" -> "&") becomes the next pass's raw
    input, and *that* still-bare "&" gets misinterpreted all over again."""
    value = (value or "").replace("\r", " ").replace("\n", " ")
    value = value.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")
    value = value.replace("|", "&#124;")
    # The substituter fills in ${key} placeholders via awk's gsub(), which
    # treats a bare "&" in the replacement text as "insert the whole match"
    # (i.e. the literal "${key}" placeholder). Escape it last, since the
    # substitutions above can themselves introduce "&" (HTML entities).
    value = value.replace("&", "\\" * (2**nesting - 1) + "&")
    return value


def parent_of(chain, has_zero_root):
    """WarDraft-style trees use chain "0" as the synthetic thread root, with
    top-level replies as bare single-segment chains ("1", "2", ...) whose
    implicit parent is "0". Stals-style trees have no "0" sentinel: the root
    post's chain is just its own post id. Both use "_"-joined ancestry for
    everything below the root."""
    if chain == "0":
        return None
    if "_" in chain:
        return chain.rsplit("_", 1)[0]
    return "0" if has_zero_root else None


def build_children(posts):
    chains = {p["post"]["chain"] for p in posts}
    has_zero_root = "0" in chains
    children = {}
    for p in posts:
        chain = p["post"]["chain"]
        parent = parent_of(chain, has_zero_root)
        children.setdefault(parent, []).append(p)
    return children, has_zero_root


def author_name(post):
    a = post.get("author") or {}
    return a.get("name") or "(unknown)"


def render_contact(post):
    a = post.get("author") or {}
    email = a.get("email")
    website = a.get("website")
    bits = []
    if email:
        bits.append(
            f'<a class="forumpost-email" href="mailto:{html.escape(email)}">{html.escape(email)}</a>'
        )
    if website:
        bits.append(f'<a class="forumpost-website" href="{html.escape(website)}">{html.escape(website)}</a>')
    if not bits:
        return ""
    return ' <span class="forumpost-contact">' + " ".join(bits) + "</span>"


def render_replyto(chain, by_chain, has_zero_root):
    parent_chain = parent_of(chain, has_zero_root)
    if parent_chain is None:
        return ""
    parent_post = by_chain.get(parent_chain)
    if parent_post is None:
        return ""
    return (
        ' <span class="forumpost-replyto">&#8627; replying to '
        f'<a href="#post-{html.escape(parent_chain)}">{html.escape(author_name(parent_post))}</a></span>'
    )


def render_highlight(text):
    """Wrap already-HTML-escaped `text` in a {{highlight}} template call.
    Must be spliced into a call's argument value raw (never passed through
    tmpl_arg again afterwards), since tmpl_arg would escape away the very
    "{{"/"}}" that make this a real nested template call. nesting=2: this
    call's own "text" argument survives its own resolution, and the
    resulting fragment is itself spliced raw into whatever call embeds this
    one (see tmpl_arg's nesting parameter)."""
    return "{{highlight |text=" + tmpl_arg(text, nesting=2) + "}}"


def render_post(post, children, by_chain, has_zero_root):
    chain = post["post"]["chain"]
    ts = post.get("timestamp") or {}
    url = post["post"].get("url") or ""
    if post["post"].get("missing"):
        content = "{{missing-post}}"
    else:
        content = (post.get("content") or {}).get("markdown") or ""

    args = {
        "anchor": chain,
        "chain": chain,
        "contact": render_contact(post),
        "replyto": render_replyto(chain, by_chain, has_zero_root),
        "datetime": html.escape(ts.get("iso8601") or ""),
        "url": html.escape(url),
    }
    call = "{{begin-forumpost " + " ".join(f"|{k}={tmpl_arg(v)}" for k, v in args.items())
    call += f" |author={render_highlight(html.escape(author_name(post)))}" + "}}"

    parts = [call, "", content.strip(), ""]
    for kid in children.get(chain, []):
        parts.append(render_post(kid, children, by_chain, has_zero_root))
        parts.append("")
    parts.append("{{end-forumpost}}")
    return "\n".join(parts)


def render_thread(data, board_name):
    title = data.get("title") or "(untitled)"
    thread_id = data.get("thread_id") or ""
    posts = data.get("posts") or []
    children, has_zero_root = build_children(posts)
    by_chain = {p["post"]["chain"]: p for p in posts}
    roots = children.get(None, [])

    body = "\n\n".join(render_post(r, children, by_chain, has_zero_root) for r in roots)

    thread_call = (
        "{{begin-forumthread "
        f"|source={tmpl_arg(html.escape(board_name))} "
        f"|threadid={tmpl_arg(html.escape(thread_id))} "
        f"|postcount={tmpl_arg(str(len(posts)))}"
        "}}"
    )

    return f"# {title}\n\n{thread_call}\n\n{body}\n\n{{{{end-forumthread}}}}\n"


def strip_id_prefix(name):
    # Board/thread directories are named "<id> - <name>"; drop the id prefix.
    _, sep, rest = name.partition(" - ")
    return rest if sep else name


def board_name_from_thread_dir(thread_dir):
    return strip_id_prefix(thread_dir.parent.name)


def board_name_from_source_root(source_root):
    for entry in sorted(source_root.iterdir()):
        if entry.is_dir() and not entry.name.startswith("."):
            return strip_id_prefix(entry.name)
    return source_root.name


def thread_root_info(data):
    """Author name and ISO timestamp of a thread's root post, straight from
    its own page.json. Only used as a fallback for the thread list, when the
    board-wide .metadata has nothing for this thread: page.json's root post
    can itself be a bare "missing" stub with no author/timestamp, which
    .metadata (parsed from the board's own index page) usually still has."""
    posts = data.get("posts") or []
    children, _ = build_children(posts)
    roots = children.get(None, [])
    if not roots:
        return "(unknown)", ""
    ts = roots[0].get("timestamp") or {}
    return author_name(roots[0]), ts.get("iso8601") or ""


def resolve_thread_meta(tid, titles, postinfo, fallback_title, fallback_author, fallback_iso):
    """Title/author/date for the thread list. The board-wide .metadata is
    authoritative here: it's parsed from the board's own index page, so it
    still has an author and date even when a thread's root post was never
    successfully archived (its page.json entry would then be a bare
    "missing" stub with no author/timestamp of its own). The fallbacks
    (from page.json, for threads we did fetch) only fill in what
    .metadata doesn't have."""
    info = postinfo.get(tid) or {}
    # .metadata's title/author come straight from a regex parse of the
    # board's index page and aren't whitespace-trimmed the way page.json's
    # fields are; strip them so switching sources doesn't shift spacing.
    title = (titles.get(tid) or fallback_title or "").strip()
    author = (info.get("author") or fallback_author or "").strip()
    iso = info.get("date_iso8601") or fallback_iso
    return title, author, iso


def short_date(iso):
    return iso.split("T")[0] if iso else ""


def render_thread_meta(author, iso):
    """'by AUTHOR · DATE', or just 'by AUTHOR' when there's no date (e.g. the
    thread's root post is itself missing). Built as one fragment rather than
    separate ${author}/${date} template args so the separator doesn't show
    up dangling when there's nothing after it. The author here is never
    inside a link (see begin-threadlink/begin-missingthreadlink), so it's
    always wrapped in {{highlight}}. The "&" of "&middot;" is pre-escaped as
    "\\&" (what tmpl_arg would otherwise do) since this fragment is spliced
    into its caller's template call raw, bypassing tmpl_arg, to keep the
    nested {{highlight}} call intact."""
    by = f"by {render_highlight(html.escape(author))}"
    date = short_date(iso)
    if not date:
        return by
    return f'{by} \\&middot; <time datetime="{html.escape(iso)}">{date}</time>'


def load_metadata(source_root):
    """Board-wide {topic_id: title} and {post_id: {author, date_iso8601,
    ...}} maps, as persisted by the adapter into .metadata. titles covers
    every thread the board's own index ever listed, fetched or not; that's
    the source of truth for which threads we're missing."""
    meta_path = source_root / ".metadata"
    if not meta_path.is_file():
        return {}, {}
    try:
        data = json.loads(meta_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Skipping metadata {meta_path}: {e}", file=sys.stderr)
        return {}, {}
    adapter = data.get("adapter") or {}
    return adapter.get("titles") or {}, adapter.get("postinfo") or {}


def id_sort_key(id_str):
    try:
        return (0, int(id_str))
    except ValueError:
        return (1, id_str)


def chain_sort_key(chain):
    try:
        return tuple(int(p) for p in chain.split("_"))
    except ValueError:
        return (chain,)


def postinfo_uses_prefixed_chains(postinfo):
    """True (stals-style): postinfo entries carry explicit topic_id/chain
    fields, and chain already includes the topic_id prefix (the root's own
    chain == topic_id, no "0" sentinel). False (wardraft-style): postinfo
    has no such fields, so its own key doubles as the chain: "<topic_id>"
    for the root, "<topic_id>_<chain>" for replies, chain local to the
    topic, "0" reserved for the root."""
    return any("topic_id" in info and "chain" in info for info in postinfo.values())


def group_replies_by_topic(postinfo):
    """{topic_id: {chain: info}} for every postinfo entry that is a reply
    rather than the topic's own root post, using each source's native
    chain convention -- the same one page.json's own "chain" field uses,
    so parent_of() applies to it unchanged."""
    by_topic = {}
    for pid, info in postinfo.items():
        if "topic_id" in info and "chain" in info:
            topic_id, chain = info["topic_id"], info["chain"]
        elif "_" in pid:
            topic_id, chain = pid.split("_", 1)
        else:
            topic_id, chain = pid, "0"
        if chain == topic_id or chain == "0":
            continue  # the root post itself, not a reply
        by_topic.setdefault(topic_id, {})[chain] = info
    return by_topic


def render_reply_text(author, iso, link_url=None, missing=False):
    """Built from tmpl_arg-escaped leaf pieces rather than one blanket
    tmpl_arg call on the whole fragment, so a nested {{highlight}} call (used
    for an author name that isn't inside a link) survives intact -- see
    render_highlight. `missing` marks a reply post that wasn't itself
    archived -- whether its thread wasn't fetched at all, or it's an
    unfetched post within a thread we do have (only ever true when link_url
    is None)."""
    author_esc = html.escape(author)
    author_disp = tmpl_arg(author_esc) if link_url else render_highlight(author_esc)
    date = short_date(iso)
    lead = "Missing reply by" if missing else "Reply by"
    text = f"{lead} {author_disp}"
    if date:
        text += f", {tmpl_arg(date)}"
    if link_url:
        return f'<a href="{tmpl_arg(link_url)}">{text}</a>'
    return text


def render_reply_rows(topic_id, replies_by_chain, has_zero_root, thread_url=None, existing_chains=None):
    """DFS-ordered, depth-indented {{replylink}} calls for one thread's
    replies, straight from .metadata -- this works even for a thread whose
    root post was itself never archived (no page.json at all), since
    .metadata covers every post the board's own index ever listed. A reply
    whose own chain is a real (non-"missing") post in that thread's
    page.json links to its anchor there; thread_url/existing_chains are
    omitted for threads we have no page.json for at all, so every reply
    then stays plain text."""
    if not replies_by_chain:
        return ""
    existing_chains = existing_chains or set()
    children = {}
    for chain in replies_by_chain:
        children.setdefault(parent_of(chain, has_zero_root), []).append(chain)
    for chains in children.values():
        chains.sort(key=chain_sort_key)

    def walk(chain, depth):
        is_missing = chain not in existing_chains
        link_url = f"{thread_url}#post-{html.escape(chain)}" if thread_url and not is_missing else None
        text = render_reply_text(
            replies_by_chain[chain].get("author") or "(unknown)",
            replies_by_chain[chain].get("date_iso8601") or "",
            link_url,
            missing=is_missing,
        )
        # text is spliced in raw, not re-wrapped in tmpl_arg: it may already
        # contain a nested {{highlight}} call (see render_reply_text), and
        # tmpl_arg would escape that call's "{{"/"}}" away.
        rows = ["{{replylink " f"|depth={depth} |text={text}" "}}"]
        for child in children.get(chain, []):
            rows.extend(walk(child, depth + 1))
        return rows

    root_anchor = "0" if has_zero_root else topic_id
    rows = []
    for chain in children.get(root_anchor, []):
        rows.extend(walk(chain, 1))
    if not rows:
        return ""
    return '  <ul class="threadlist-replies">\n' + "\n".join(rows) + "\n  </ul>\n"


# "meta" (built by render_thread_meta) is spliced in raw rather than through
# tmpl_arg, like "text" in render_reply_rows above: it already contains a
# nested {{highlight}} call, which a blanket tmpl_arg pass would escape away.
def render_existing_entry(item):
    args = {k: v for k, v in item.items() if k not in ("replies", "meta")}
    call = "{{begin-threadlink " + " ".join(f"|{k}={tmpl_arg(v)}" for k, v in args.items())
    call += f" |meta={item['meta']}" + "}}"
    return f'{call}\n{item.get("replies") or ""}{{{{end-threadlink}}}}'


def render_missing_entry(item):
    args = {k: v for k, v in item.items() if k not in ("replies", "meta")}
    call = "{{begin-missingthreadlink " + " ".join(f"|{k}={tmpl_arg(v)}" for k, v in args.items())
    call += f" |meta={item['meta']}" + "}}"
    return f'{call}\n{item.get("replies") or ""}{{{{end-missingthreadlink}}}}'


def render_thread_list(board_name, existing, missing):
    existing_items = "\n".join(render_existing_entry(e) for e in existing)
    missing_items = "\n".join(render_missing_entry(m) for m in missing)
    list_call = (
        "{{begin-threadlist "
        f"|source={tmpl_arg(html.escape(board_name))} "
        f"|existingcount={tmpl_arg(str(len(existing)))} "
        f"|missingcount={tmpl_arg(str(len(missing)))}"
        "}}"
    )
    missing_call = "{{begin-missingthreads " f"|missingcount={tmpl_arg(str(len(missing)))}" "}}"

    return (
        f"# {board_name} — Threads\n\n"
        f"{list_call}\n\n"
        "{{begin-existingthreads}}\n"
        f"{existing_items}\n"
        "{{end-existingthreads}}\n\n"
        f"{missing_call}\n\n"
        f"{missing_items}\n"
        "{{end-missingthreads}}\n\n"
        "{{end-threadlist}}\n"
    )


def main():
    ap = argparse.ArgumentParser(
        description="Render nested forum threads (page.json trees) as Incunable-templated Markdown."
    )
    ap.add_argument(
        "--source",
        action="append",
        dest="sources",
        default=None,
        help="Root directory containing page.json files (repeatable). "
        f"Default: {', '.join(DEFAULT_SOURCES)}",
    )
    ap.add_argument(
        "--output-root",
        default=DEFAULT_OUTPUT_ROOT,
        help="Directory to write rendered threads into. Each source gets a "
        "<output-root>/<source-name>/threads/<thread> directory with an "
        "index.md, plus an <output-root>/<source-name>/index.md thread-list "
        "page. Default: %(default)s",
    )
    args = ap.parse_args()

    sources = args.sources or DEFAULT_SOURCES
    output_root = Path(args.output_root)

    written = 0
    for source in sources:
        src = Path(source)
        if not src.is_dir():
            print(f"Source not found, skipping: {src}", file=sys.stderr)
            continue

        source_name = src.name
        board_name = board_name_from_source_root(src)
        titles, postinfo = load_metadata(src)
        has_zero_root_meta = not postinfo_uses_prefixed_chains(postinfo)
        replies_by_topic = group_replies_by_topic(postinfo)

        existing = []
        fetched_ids = set()
        for page in sorted(src.rglob("page.json")):
            try:
                data = json.loads(page.read_text(encoding="utf-8"))
            except Exception as e:
                print(f"Skipping {page}: {e}", file=sys.stderr)
                continue

            thread_dir = page.parent
            thread_board_name = board_name_from_thread_dir(thread_dir)
            md_text = render_thread(data, thread_board_name)

            thread_id = data.get("thread_id") or "thread"
            out_dir = output_root / source_name / "threads" / safe_name(thread_id)
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / "index.md"
            out_path.write_text(md_text, encoding="utf-8")
            written += 1
            print(f"Wrote {out_path}", file=sys.stderr)

            fetched_ids.add(thread_id)
            root_author, root_iso = thread_root_info(data)
            title, author, iso = resolve_thread_meta(
                thread_id, titles, postinfo,
                data.get("title") or "(untitled)", root_author, root_iso,
            )
            thread_url = html.escape(f"{source_name}/threads/{safe_name(thread_id)}.html")
            existing_chains = {
                p["post"]["chain"] for p in (data.get("posts") or []) if not p["post"].get("missing")
            }
            existing.append((thread_id, {
                "id": html.escape(thread_id),
                "title": html.escape(title),
                "url": thread_url,
                "meta": render_thread_meta(author, iso),
                "replies": render_reply_rows(
                    thread_id, replies_by_topic.get(thread_id, {}), has_zero_root_meta,
                    thread_url, existing_chains,
                ),
            }))

        missing = []
        for tid, ttitle in titles.items():
            if tid in fetched_ids:
                continue
            title, author, iso = resolve_thread_meta(tid, titles, postinfo, ttitle or "(untitled)", "(unknown)", "")
            missing.append((tid, {
                "id": html.escape(tid),
                "title": html.escape(title),
                "meta": render_thread_meta(author, iso),
                "replies": render_reply_rows(tid, replies_by_topic.get(tid, {}), has_zero_root_meta),
            }))

        existing.sort(key=lambda t: id_sort_key(t[0]))
        missing.sort(key=lambda t: id_sort_key(t[0]))

        list_md = render_thread_list(board_name, [e for _, e in existing], [m for _, m in missing])
        list_dir = output_root / source_name
        list_dir.mkdir(parents=True, exist_ok=True)
        (list_dir / "index.md").write_text(list_md, encoding="utf-8")
        print(
            f"Wrote {list_dir / 'index.md'} "
            f"({len(existing)} existing, {len(missing)} missing)",
            file=sys.stderr,
        )

    print(f"Done: {written} thread(s).", file=sys.stderr)


if __name__ == "__main__":
    main()
