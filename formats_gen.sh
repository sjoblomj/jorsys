#!/bin/bash

for f in formats/*.json; do
    file=$(basename "$f" .json)
    title=$(echo "$file" | tr _ .)
    echo "Generating format file $title into content/formats/$file/index.md"

    mkdir -p content/formats/"$file"
    printf "# %s Format\n\n" "$title" > content/formats/"$file"/index.md

    jq -r 'map(
      "## " + .name + "\n" +
      "{{begin-formattable}}\n" +
        "  {{formatlbl |label=Offset |value=" + .offset + "}}\n" +
        "  {{formatlbl |label=Length |value=" + .length + "}}\n" +
        "  {{formatlbl |label=Description |value=" + .description + "}}\n" +
      (if .values == null then "" else
        "  {{formatlbl |label=Values |value=" + .values + "}}\n"
      end) +
      (if .bits == [] then "" else
        "  {{formatlbl |label=Bits |value={{begin-bittable}}" + (.bits | map("      {{formatbitlbl |label=" + .bit + " |value=" + .value + "}}") | join("")) + "    {{end-bittable}}  }}\n"
      end) +
      "{{end-formattable}}\n"
    ) | join("\n")' formats/"$file".json >> content/formats/"$file"/index.md
done
