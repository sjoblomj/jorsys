# techdata.dat Format

## Cost: Minerals
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Cost in Minerals required to research this Technology.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0058}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Cost in Vespene Gas to research this Technology.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Research Time
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x00B0}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Time required to research this Technology.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Cost: Mana
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0108}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Mana required to use this Technology.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0160}}
  {{formatlbl |label=Length |value=176 bytes (4 bytes / Technology)}}
  {{formatlbl |label=Description |value=Unknown, most likely this is a flag of some sort. Always set to 0xFFFFFFFF.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 2^32}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0210}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=The index of an icon in the cmdicons.grp file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of cmdicons.grp.}}
{{end-formattable}}

## Label
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0268}}
  {{formatlbl |label=Length |value=88 bytes (2 bytes / Technology)}}
  {{formatlbl |label=Description |value=Index of a string in rez\stat_txt.tbl which is the label for this technology.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of rez\stat_txt.tbl}}
{{end-formattable}}

## Race
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x02C0}}
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
  {{formatlbl |label=Offset |value=0x02EC}}
  {{formatlbl |label=Length |value=44 bytes (1 byte / Technology)}}
  {{formatlbl |label=Description |value=Boolean flag which determines whether this Technology is already researched.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (not researched)}}
    {{formatbitlbl |label=0x01 |value=true (researched)}}
  {{end-bittable}} }}
{{end-formattable}}

## Brood War Flag
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0318}}
  {{formatlbl |label=Length |value=44 bytes (1 byte / Technology)}}
  {{formatlbl |label=Description |value=Boolean flag that determines whether this technology is Brood War-researchable only.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (SC and BW)}}
    {{formatbitlbl |label=0x01 |value=true (BW Only)}}
  {{end-bittable}} }}
{{end-formattable}}

