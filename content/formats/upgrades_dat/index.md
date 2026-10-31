# upgrades.dat Format

## Cost: Minerals
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Cost in Minerals to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value betwen 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Minerals
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x007A}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Factor cost in Minerals to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x00F4}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Cost in Vespene Gas required to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Vespene Gas
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x016E}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Factor Cost in Vespene Gas to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Research Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x01E8}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Time required to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Research Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0262}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Factor Cost in Time required to research this Upgrade.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02DC}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Unknown, probably a set of flags for each upgrade. All upgrades have 0xFFFF.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0356}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Index of an icon in cmdicons.grp}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of cmdicons.grp}}
{{end-formattable}}

## Label
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x03D0}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Index of label in rez\stat_txt.tbl}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of rez\stat_txt.tbl}}
{{end-formattable}}

## Race
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x044A}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=Determines which races can research this upgrade.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Zerg}}
    {{formatbitlbl |label=0x01 |value=Terran}}
    {{formatbitlbl |label=0x02 |value=Protoss}}
    {{formatbitlbl |label=0x03 |value=All}}
  {{end-bittable}} }}
{{end-formattable}}

## Repeat
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0487}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=The number of times this upgrade can be researched.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Brood War Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x04C4}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=Boolean flag which determines whether this upgrade is restricted to Brood War.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (SC and BW)}}
    {{formatbitlbl |label=0x01 |value=true (BW only)}}
  {{end-bittable}} }}
{{end-formattable}}

---

## Appendix: Upgrades list
{{begin-formattable}}
  {{formatlbl |label=Description |value=List of upgrades.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Terran Infantry Armor}}
    {{formatbitlbl |label=0x01 |value=Terran Vehicle Plating}}
    {{formatbitlbl |label=0x02 |value=Terran Ship Plating}}
    {{formatbitlbl |label=0x03 |value=Zerg Carapace}}
    {{formatbitlbl |label=0x04 |value=Zerg Flyer Carapace}}
    {{formatbitlbl |label=0x05 |value=Protoss Armor}}
    {{formatbitlbl |label=0x06 |value=Protoss Plating}}
    {{formatbitlbl |label=0x07 |value=Terran Infantry Weapons}}
    {{formatbitlbl |label=0x08 |value=Terran Vehicle Weapons}}
    {{formatbitlbl |label=0x09 |value=Terran Ship Weapons}}
    {{formatbitlbl |label=0x0A |value=Zerg Melee Attacks}}
    {{formatbitlbl |label=0x0B |value=Zerg Missile Attacks}}
    {{formatbitlbl |label=0x0C |value=Zerg Flyer Attacks}}
    {{formatbitlbl |label=0x0D |value=Protoss Ground Weapons}}
    {{formatbitlbl |label=0x0E |value=Protoss Air Weapons}}
    {{formatbitlbl |label=0x0F |value=Protoss Plasma Shields}}
    {{formatbitlbl |label=0x10 |value=U-238 Shells}}
    {{formatbitlbl |label=0x11 |value=Ion Thrusters}}
    {{formatbitlbl |label=0x12 |value=Burst Lasers (Unused)}}
    {{formatbitlbl |label=0x13 |value=Titan Reactor (SV +50)}}
    {{formatbitlbl |label=0x14 |value=Ocular Implants}}
    {{formatbitlbl |label=0x15 |value=Moebius Reactor (Ghost +50)}}
    {{formatbitlbl |label=0x16 |value=Apollo Reactor (Wraith +50)}}
    {{formatbitlbl |label=0x17 |value=Colossus Reactor (BC +50)}}
    {{formatbitlbl |label=0x18 |value=Ventral Sacs}}
    {{formatbitlbl |label=0x19 |value=Antennae}}
    {{formatbitlbl |label=0x1A |value=Pneumatized Carapace}}
    {{formatbitlbl |label=0x1B |value=Metabolic Boost}}
    {{formatbitlbl |label=0x1C |value=Adrenal Glands}}
    {{formatbitlbl |label=0x1D |value=Muscular Augments}}
    {{formatbitlbl |label=0x1E |value=Grooved Spines}}
    {{formatbitlbl |label=0x1F |value=Gamete Meiosis (Queen +50)}}
    {{formatbitlbl |label=0x20 |value=Metasynaptic Node (Defiler +50)}}
    {{formatbitlbl |label=0x21 |value=Singularity Charge}}
    {{formatbitlbl |label=0x22 |value=Leg Enhancements}}
    {{formatbitlbl |label=0x23 |value=Scarab Damage}}
    {{formatbitlbl |label=0x24 |value=Reaver Capacity}}
    {{formatbitlbl |label=0x25 |value=Gravitic Drive}}
    {{formatbitlbl |label=0x26 |value=Sensor Array}}
    {{formatbitlbl |label=0x27 |value=Gravitic Boosters}}
    {{formatbitlbl |label=0x28 |value=Khaydarin Amulet (HT +50)}}
    {{formatbitlbl |label=0x29 |value=Apial Sensors}}
    {{formatbitlbl |label=0x2A |value=Gravitic Thrusters}}
    {{formatbitlbl |label=0x2B |value=Carrier Capacity}}
    {{formatbitlbl |label=0x2C |value=Khaydarin Core (Arbiter +50)}}
    {{formatbitlbl |label=0x2D |value=Unknown Upgrade45}}
    {{formatbitlbl |label=0x2E |value=Unknown Upgrade46}}
    {{formatbitlbl |label=0x2F |value=Argus Jewel (Corsair +50)}}
    {{formatbitlbl |label=0x30 |value=Unknown Upgrade48}}
    {{formatbitlbl |label=0x31 |value=Argus Talisman (DA +50)}}
    {{formatbitlbl |label=0x32 |value=Unknown Upgrade50}}
    {{formatbitlbl |label=0x33 |value=Caduceus Reactor (Medic +50)}}
    {{formatbitlbl |label=0x34 |value=Chitinous Plating}}
    {{formatbitlbl |label=0x35 |value=Anabolic Synthesis}}
    {{formatbitlbl |label=0x36 |value=Charon Booster}}
    {{formatbitlbl |label=0x37 |value=Unknown Upgrade55}}
    {{formatbitlbl |label=0x38 |value=Unknown Upgrade56}}
    {{formatbitlbl |label=0x39 |value=Unknown Upgrade57}}
    {{formatbitlbl |label=0x3A |value=Unknown Upgrade58}}
    {{formatbitlbl |label=0x3B |value=Unknown Upgrade59}}
    {{formatbitlbl |label=0x3C |value=Unknown Upgrade60}}
  {{end-bittable}} }}
{{end-formattable}}

