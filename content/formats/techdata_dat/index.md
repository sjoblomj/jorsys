# techdata.dat Format

## Cost: Minerals
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Cost in Minerals required to research this Technology.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0058}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Cost in Vespene Gas to research this Technology.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Research Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x00B0}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Time required to research this Technology.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Cost: Mana
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0108}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Mana required to use this Technology.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0160}}
  {{formatlbl |label=Length |value=176 bytes (4 bytes / Technology)}}
  {{formatlbl |label=Description |value=Unknown, most likely this is a flag of some sort. Always set to 0xFFFFFFFF.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 2^32}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0210}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=The index of an icon in the cmdicons.grp file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of cmdicons.grp.}}
{{end-formattable}}

## Label
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0268}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Index of a string in rez\stat_txt.tbl which is the label for this technology.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of rez\stat_txt.tbl}}
{{end-formattable}}

## Race
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02C0}}
  {{formatlbl |label=Length |value=44 bytes (1 byte / Technology)}}
  {{formatlbl |label=Description |value=Determines the race this Technology is researched by.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Zerg}}
    {{formatbitlbl |label=0x01 |value=Terran}}
    {{formatbitlbl |label=0x02 |value=Protoss}}
    {{formatbitlbl |label=0x03 |value=All}}
  {{end-bittable}} }}
{{end-formattable}}

## Researched
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02EC}}
  {{formatlbl |label=Length |value=44 bytes (1 byte / Technology)}}
  {{formatlbl |label=Description |value=Boolean flag which determines whether this Technology is already researched.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (not researched)}}
    {{formatbitlbl |label=0x01 |value=true (researched)}}
  {{end-bittable}} }}
{{end-formattable}}

## Brood War Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0318}}
  {{formatlbl |label=Length |value=44 bytes (1 byte / Technology)}}
  {{formatlbl |label=Description |value=Boolean flag that determines whether this technology is Brood War-researchable only.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (SC and BW)}}
    {{formatbitlbl |label=0x01 |value=true (BW Only)}}
  {{end-bittable}} }}
{{end-formattable}}

---

## Appendix: Techdata list
{{begin-formattable}}
  {{formatlbl |label=Description |value=List of technologies.}}
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
    {{formatbitlbl |label=0x0D |value=Spawn Broodlings}}
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
    {{formatbitlbl |label=0x1A |value=Unknown Tech26}}
    {{formatbitlbl |label=0x1B |value=Mind Control}}
    {{formatbitlbl |label=0x1C |value=Dark Archon Meld}}
    {{formatbitlbl |label=0x1D |value=Feedback}}
    {{formatbitlbl |label=0x1E |value=Optical Flare}}
    {{formatbitlbl |label=0x1F |value=Maelstrom}}
    {{formatbitlbl |label=0x20 |value=Lurker Aspect}}
    {{formatbitlbl |label=0x21 |value=Unknown Tech33}}
    {{formatbitlbl |label=0x22 |value=Healing}}
    {{formatbitlbl |label=0x23 |value=Unknown Tech35}}
    {{formatbitlbl |label=0x24 |value=Unknown Tech36}}
    {{formatbitlbl |label=0x25 |value=Unknown Tech37}}
    {{formatbitlbl |label=0x26 |value=Unknown Tech38}}
    {{formatbitlbl |label=0x27 |value=Unknown Tech39}}
    {{formatbitlbl |label=0x28 |value=Unknown Tech40}}
    {{formatbitlbl |label=0x29 |value=Unknown Tech41}}
    {{formatbitlbl |label=0x2A |value=Unknown Tech42}}
    {{formatbitlbl |label=0x2B |value=Unknown Tech43}}
  {{end-bittable}} }}
{{end-formattable}}

