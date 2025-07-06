# upgrades.dat Format

## Cost: Minerals
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Cost in Minerals to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value betwen 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Minerals
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x007A}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Factor cost in Minerals to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x00F4}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Cost in Vespene Gas required to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Vespene Gas
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x016E}}
  {{formatlbl |label=Length |value=Factor Cost in Vespene Gas to research this Upgrade.}}
  {{formatlbl |label=Description |value=}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Research Time
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x01E8}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Time required to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Research Time
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0262}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Factor Cost in Time required to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x02DC}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Unknown, probably a set of flags for each upgrade. All upgrades have 0xFFFF.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0356}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Index of an icon in cmdicons.grp}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of cmdicons.grp}}
{{end-formattable}}

## Label
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x03D0}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Index of label in rez\stat_txt.tbl}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of rez\stat_txt.tbl}}
{{end-formattable}}

## Race
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x044A}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=Determines which races can research this upgrade.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x00 |value=Zerg}}      {{formatbitlbl |label=0x01 |value=Terran}}      {{formatbitlbl |label=0x02 |value=Protoss}}      {{formatbitlbl |label=0x03 |value=All}}    {{end-bittable}}  }}
{{end-formattable}}

## Repeat
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0487}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=The number of times this upgrade can be researched.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Brood War Flag
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x04C4}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=Boolean flag which determines whether this upgrade is restricted to Brood War.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x00 |value=false (SC and BW)}}      {{formatbitlbl |label=0x01 |value=true (BW only)}}    {{end-bittable}}  }}
{{end-formattable}}

