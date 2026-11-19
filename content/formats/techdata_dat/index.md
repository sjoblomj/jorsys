# techdata.dat Format

techdata.dat holds the data for technologies: the spells and abilities that are researched once, such as Stim Packs, Lockdown or Burrowing (see Appendix: Techdata list). It gives each technology's research cost, the energy it costs to use, its icon, its name, its race and whether it belongs to Brood War. It is the file arr\techdata.dat in the game's MPQ archives and is 836 bytes long. Each field below is a list with one entry for each of the 44 technologies, and the lists are stored one after another with nothing in between, so the offsets are from the start of the file. The layout is the same in every version from 1.04 to 1.17, of both StarCraft and Brood War, and StarEdit reads the file in the same layout. StarCraft 1.00 to 1.03 used an older, shorter layout, with 24 technologies (432 bytes). That older file is still in StarDat.mpq in later versions, but it is never loaded: the newer copy in patch_rt.mpq (or, in 1.05 to 1.07, BrooDat.mpq) is found first. The patch_rt.mpq copy is the same in 1.08 to 1.17. The game loads the file again each time a game starts, before the map's own settings are applied, so a change to the file takes effect at the next game. Fields are read in order, and the game stops with a file error if the file is longer than the layout. A shorter file that ends exactly where a field ends loads without an error; the fields after the end then keep whatever they held before.

A map can replace the costs. Its technology settings (the CHK section TECS in StarCraft maps and TECx in Brood War maps) hold minerals, gas, time and energy for each technology, and for every technology whose "use default settings" flag is clear these replace the four Cost fields of this file for that game. Saved games store the four Cost fields as well. Which technologies each player may research, and which they start with, come from the map, not from this file.

Technologies 0 to 23 are those of the original StarCraft and 24 to 43 were added by Brood War. Entries 26, 33 and 35 to 43 are unused.

## Cost: Minerals
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Minerals needed to research this technology. Taken when the research starts and given back if it is cancelled.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0058}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Vespene gas needed to research this technology. Taken when the research starts and given back if it is cancelled.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Research Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x00B0}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Time the research takes, in game frames: the value is copied into the building's research countdown when the research starts. The progress bar shown while researching is measured against it too. StarEdit shows the time divided by 15, as seconds.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Energy
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0108}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Energy a unit needs, and spends, to use this technology. The value is in whole energy points; the game multiplies it by 256, because units keep their energy in 1/256 points. The cost charged for a spell is looked up through the order's technology in orders.dat. Some of the checks (for example the one made when the spell is clicked) keep only the low byte of the value, so a cost above 255 does not work consistently. A button that uses the technology shows this cost in its tooltip.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255 (see the description). Units can hold at most 250 energy.}}
{{end-formattable}}

## Requirements: Research
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0160}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Where this technology's research requirements start in the game's built-in requirement list (the technology research requirements, inside the executable, not in any data file), as a position in that list. 0 means the technology has no requirements entry and is never allowed. The game fills this field in itself: whenever it checks a technology whose entry holds 0xFFFF, it walks the built-in list, stores the position for every technology listed there (replacing what the file had), and sets every entry still 0xFFFF to 0. So a value other than 0xFFFF only survives for technologies that have no entry in the built-in list, or if the file has no 0xFFFF at all, and it then picks (part of) an existing entry of the list; nothing checks it. The shipped file has 0xFFFF everywhere, so the game always uses its built-in list.}}
  {{formatlbl |label=Values |value=0xFFFF (let the game fill it in).}}
{{end-formattable}}

## Requirements: Use
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x01B8}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Where this technology's requirements for using it (casting the spell or using the ability, checked each time a unit tries) start in the game's built-in requirement list (the technology use requirements, inside the executable, not in any data file), as a position in that list. 0 means the technology has no requirements entry and is never allowed. The game fills this field in itself: whenever it checks a technology whose entry holds 0xFFFF, it walks the built-in list, stores the position for every technology listed there (replacing what the file had), and sets every entry still 0xFFFF to 0. So a value other than 0xFFFF only survives for technologies that have no entry in the built-in list, or if the file has no 0xFFFF at all, and it then picks (part of) an existing entry of the list; nothing checks it. The shipped file has 0xFFFF everywhere, so the game always uses its built-in list.}}
  {{formatlbl |label=Values |value=0xFFFF (let the game fill it in).}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0210}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Frame of unit\cmdbtns\cmdicons.grp shown in the status panel while this technology is being researched. Command buttons do not use it; their icons are part of the button sets in the executable.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last frame of cmdicons.grp.}}
{{end-formattable}}

## Label
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0268}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Name of the technology: a string number in rez\stat_txt.tbl, counting from 1. The game uses it in the tooltip of the icon shown while the technology is being researched ("Cancel Research" followed by the name in brackets). StarEdit uses it to name the technology in its technology settings.}}
  {{formatlbl |label=Values |value=Integer value between 1 and the number of strings in rez\stat_txt.tbl. 0 or a number beyond the last string gives an empty name.}}
{{end-formattable}}

## Race
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02C0}}
  {{formatlbl |label=Length |value=44 bytes (1 byte / Technology)}}
  {{formatlbl |label=Description |value=Only used by StarEdit, which lists the technologies under their race in the technology settings of a map, and leaves out technologies with the value 3. The game itself never reads this field.}}
  {{formatlbl |label=Values |value=Values above 3 are not rejected by StarEdit: it uses the value as an index into its three race headings and takes the heading from whatever follows them in memory, which differs between versions. Where that is zero (the value 4 in StarEdit 1.15.0), the technology is listed at the top level, outside the races.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Zerg}}
    {{formatbitlbl |label=0x01 |value=Terran}}
    {{formatbitlbl |label=0x02 |value=Protoss}}
    {{formatbitlbl |label=0x03 |value=None: StarEdit leaves the entry out of its lists}}
  {{end-bittable}} }}
{{end-formattable}}

## Researched
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02EC}}
  {{formatlbl |label=Length |value=44 bytes (1 byte / Technology)}}
  {{formatlbl |label=Description |value=Not used: no code in StarCraft or StarEdit reads this field, in any version from 1.04 to 1.17. In the shipped file it is 1 for the technologies that need no research (Scanner Sweep, Defensive Matrix, Infestation, Dark Swarm, Parasite, Archon Warp, Dark Archon Meld, Feedback, Healing) and for the unused entry 33. Whether a player starts with a technology is set by the map.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Needs research (not used by the game)}}
    {{formatbitlbl |label=0x01 |value=Available without research (not used by the game)}}
  {{end-bittable}} }}
{{end-formattable}}

## Brood War Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0318}}
  {{formatlbl |label=Length |value=44 bytes (1 byte / Technology)}}
  {{formatlbl |label=Description |value=Only used by StarEdit, which shows the technologies marked 1 only when the map is a Brood War map. The game itself never reads this field.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Shown in StarEdit for StarCraft and Brood War maps}}
    {{formatbitlbl |label=0x01 |value=Shown in StarEdit only for Brood War maps}}
    {{formatbitlbl |label=0x02 and up |value=Never shown in StarEdit}}
  {{end-bittable}} }}
{{end-formattable}}

---

## Appendix: Techdata list
{{begin-formattable}}
  {{formatlbl |label=Description |value=The technology list, with the names the game uses (from each technology's Label). Every field of the file has one entry for each of these, in this order. Entries 26, 33 and 35 to 43 have no name and no use. The game's technology number 44 means "no technology" (for example in orders.dat), but it has no entry in this file.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Stim Packs}}
    {{formatbitlbl |label=0x01 |value=Lockdown}}
    {{formatbitlbl |label=0x02 |value=EMP Shockwave}}
    {{formatbitlbl |label=0x03 |value=Spider Mines}}
    {{formatbitlbl |label=0x04 |value=Scanner Sweep}}
    {{formatbitlbl |label=0x05 |value=Tank Siege Mode}}
    {{formatbitlbl |label=0x06 |value=Defensive Matrix}}
    {{formatbitlbl |label=0x07 |value=Irradiate}}
    {{formatbitlbl |label=0x08 |value=Yamato Gun}}
    {{formatbitlbl |label=0x09 |value=Cloaking Field}}
    {{formatbitlbl |label=0x0A |value=Personnel Cloaking}}
    {{formatbitlbl |label=0x0B |value=Burrowing}}
    {{formatbitlbl |label=0x0C |value=Infestation}}
    {{formatbitlbl |label=0x0D |value=Spawn Broodling}}
    {{formatbitlbl |label=0x0E |value=Dark Swarm}}
    {{formatbitlbl |label=0x0F |value=Plague}}
    {{formatbitlbl |label=0x10 |value=Consume}}
    {{formatbitlbl |label=0x11 |value=Ensnare}}
    {{formatbitlbl |label=0x12 |value=Parasite}}
    {{formatbitlbl |label=0x13 |value=Psionic Storm}}
    {{formatbitlbl |label=0x14 |value=Hallucination}}
    {{formatbitlbl |label=0x15 |value=Recall}}
    {{formatbitlbl |label=0x16 |value=Stasis Field}}
    {{formatbitlbl |label=0x17 |value=Archon Warp}}
    {{formatbitlbl |label=0x18 |value=Restoration}}
    {{formatbitlbl |label=0x19 |value=Disruption Web}}
    {{formatbitlbl |label=0x1A |value=Unused 26}}
    {{formatbitlbl |label=0x1B |value=Mind Control}}
    {{formatbitlbl |label=0x1C |value=Dark Archon Meld}}
    {{formatbitlbl |label=0x1D |value=Feedback}}
    {{formatbitlbl |label=0x1E |value=Optical Flare}}
    {{formatbitlbl |label=0x1F |value=Maelstrom}}
    {{formatbitlbl |label=0x20 |value=Lurker Aspect}}
    {{formatbitlbl |label=0x21 |value=Unused 33}}
    {{formatbitlbl |label=0x22 |value=Healing}}
    {{formatbitlbl |label=0x23 |value=Unused 35}}
    {{formatbitlbl |label=0x24 |value=Unused 36}}
    {{formatbitlbl |label=0x25 |value=Unused 37}}
    {{formatbitlbl |label=0x26 |value=Unused 38}}
    {{formatbitlbl |label=0x27 |value=Unused 39}}
    {{formatbitlbl |label=0x28 |value=Unused 40}}
    {{formatbitlbl |label=0x29 |value=Unused 41}}
    {{formatbitlbl |label=0x2A |value=Unused 42}}
    {{formatbitlbl |label=0x2B |value=Unused 43}}
  {{end-bittable}} }}
{{end-formattable}}

