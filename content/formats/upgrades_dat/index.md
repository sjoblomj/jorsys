# upgrades.dat Format

upgrades.dat holds the data for upgrades: improvements that can be researched at one or more levels, such as Terran Infantry Weapons or Metabolic Boost (see Appendix: Upgrades list). It gives each upgrade's cost, how the cost grows with each level, its icon, its name, its race, its highest level and whether it belongs to Brood War. It is the file arr\upgrades.dat in the game's MPQ archives and is 1281 bytes long. Each field below is a list with one entry for each of the 61 upgrades, and the lists are stored one after another with nothing in between, so the offsets are from the start of the file. The layout is the same in every version from 1.04 to 1.17, of both StarCraft and Brood War, and StarEdit reads the file in the same layout. StarCraft 1.00 to 1.03 used an older, shorter layout, with 46 upgrades (920 bytes). That older file is still in StarDat.mpq in later versions, but it is never loaded: the newer copy in patch_rt.mpq (or, in 1.05 to 1.07, BrooDat.mpq) is found first. The patch_rt.mpq copy is the same in 1.08 to 1.17. The game loads the file again each time a game starts, before the map's own settings are applied, so a change to the file takes effect at the next game. Fields are read in order, and the game stops with a file error if the file is longer than the layout. A shorter file that ends exactly where a field ends loads without an error; the fields after the end then keep whatever they held before.

The cost of the next level is Cost plus Cost Factor times the level the player already has; for the first level that is just Cost. A map can replace the six cost fields. Its upgrade settings (the CHK section UPGS in StarCraft maps and UPGx in Brood War maps) hold all six for each upgrade, and for every upgrade whose "use default settings" flag is clear they replace the values of this file for that game. Saved games store the six cost fields as well.

Upgrades 0 to 45 are those of the original StarCraft and 46 to 60 were added by Brood War. Entry 60 is the game's "no upgrade" value: units.dat and weapons.dat use it for units and weapons that no upgrade affects. Entries 18, 45, 46, 48, 50 and 55 to 59 are unused.

## Cost: Minerals
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Minerals needed for the first level of this upgrade. For level n+1 the cost is this value plus Cost Factor: Minerals times n, worked out in 16 bits (so it wraps around above 65535). Taken when the upgrade starts and given back if it is cancelled.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Minerals
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x007A}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Minerals added to the cost for each level the player already has (see Cost: Minerals). StarEdit only shows this field for upgrades with more than one level.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x00F4}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Vespene gas needed for the first level of this upgrade. For level n+1 the cost is this value plus Cost Factor: Vespene Gas times n, worked out in 16 bits. Taken when the upgrade starts and given back if it is cancelled.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Vespene Gas
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x016E}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Vespene gas added to the cost for each level the player already has (see Cost: Vespene Gas). StarEdit only shows this field for upgrades with more than one level.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Research Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x01E8}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Time the first level of this upgrade takes, in game frames. For level n+1 the time is this value plus Cost Factor: Research Time times n. The result is copied into the building's 16-bit upgrade countdown, so a time above 65535 wraps around. StarEdit shows times divided by 15, as seconds.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost Factor: Research Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0262}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Frames added to the time for each level the player already has (see Cost: Research Time). StarEdit only shows this field for upgrades with more than one level.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Requirements
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02DC}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Where this upgrade's requirements start in the game's built-in requirement list (the upgrade requirements, inside the executable, not in any data file), as a position in that list. 0 means the upgrade has no requirements entry and is never allowed. The game fills this field in itself: whenever it checks a upgrade whose entry holds 0xFFFF, it walks the built-in list, stores the position for every upgrade listed there (replacing what the file had), and sets every entry still 0xFFFF to 0. So a value other than 0xFFFF only survives for upgrades that have no entry in the built-in list, or if the file has no 0xFFFF at all, and it then picks (part of) an existing entry of the list; nothing checks it. The shipped file has 0xFFFF everywhere, so the game always uses its built-in list.}}
  {{formatlbl |label=Values |value=0xFFFF (let the game fill it in).}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0356}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Frame of unit\cmdbtns\cmdicons.grp shown in the status panel while this upgrade is being researched. It is also the armor icon of a selected unit, for the upgrade named in the unit's Armor Upgrade field in units.dat. Weapon icons come from weapons.dat and the shield icon is fixed. Command buttons do not use this field.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last frame of cmdicons.grp.}}
{{end-formattable}}

## Label
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x03D0}}
  {{formatlbl |label=Length |value=122 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Name of the upgrade: a string number in rez\stat_txt.tbl, counting from 1. The game uses it in the tooltip of the icon shown while the upgrade is being researched, and in the tooltips of a unit's armor icon and of its shield icon (which names upgrade 15, Protoss Plasma Shields). StarEdit uses it to name the upgrade in its upgrade settings.}}
  {{formatlbl |label=Values |value=Integer value between 1 and the number of strings in rez\stat_txt.tbl. 0 or a number beyond the last string gives an empty name.}}
{{end-formattable}}

## Race
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x044A}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=Only used by StarEdit, which lists the upgrades under their race in the upgrade settings of a map, and leaves out upgrades with the value 3. The game itself never reads this field.}}
  {{formatlbl |label=Values |value=Values above 3 are not rejected by StarEdit: it uses the value as an index into its three race headings and takes the heading from whatever follows them in memory, which differs between versions and between its two dialogs that list the upgrades. Where that is zero (the value 4 in one of the two dialogs of StarEdit 1.15.0), the upgrade is listed at the top level, outside the races.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Zerg}}
    {{formatbitlbl |label=0x01 |value=Terran}}
    {{formatbitlbl |label=0x02 |value=Protoss}}
    {{formatbitlbl |label=0x03 |value=None: StarEdit leaves the entry out of its lists}}
  {{end-bittable}} }}
{{end-formattable}}

## Max Level
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0487}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=The highest level of this upgrade. When a new game starts (not a saved one), every player's highest level for the upgrade is set to this value; the map's upgrade settings can then set other levels for each player. If it is above 1, the upgrade button's tooltip shows the level being researched. The cheat that raises all upgrades raises each one up to this value. StarEdit leaves upgrades with the value 0 out of its lists, uses the value as the highest level that can be set, and only shows the Cost Factor fields when it is above 1.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Brood War Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x04C4}}
  {{formatlbl |label=Length |value=61 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=Only used by StarEdit, which shows the upgrades marked 1 only when the map is a Brood War map. The game itself never reads this field.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Shown in StarEdit for StarCraft and Brood War maps}}
    {{formatbitlbl |label=0x01 |value=Shown in StarEdit only for Brood War maps}}
    {{formatbitlbl |label=0x02 and up |value=Never shown in StarEdit}}
  {{end-bittable}} }}
{{end-formattable}}

---

## Appendix: Upgrades list
{{begin-formattable}}
  {{formatlbl |label=Description |value=The upgrade list, with the names the game uses (from each upgrade's Label) and what each upgrade does in brackets where the name does not say. Every field of the file has one entry for each of these, in this order. Entries marked unused have no name. Burst Lasers (18) has a name, but no button researches it and its Max Level is 0.}}
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
    {{formatbitlbl |label=0x10 |value=U-238 Shells (Marine range)}}
    {{formatbitlbl |label=0x11 |value=Ion Thrusters (Vulture speed)}}
    {{formatbitlbl |label=0x12 |value=Burst Lasers (unused)}}
    {{formatbitlbl |label=0x13 |value=Titan Reactor (Science Vessel energy)}}
    {{formatbitlbl |label=0x14 |value=Ocular Implants (Ghost sight)}}
    {{formatbitlbl |label=0x15 |value=Moebius Reactor (Ghost energy)}}
    {{formatbitlbl |label=0x16 |value=Apollo Reactor (Wraith energy)}}
    {{formatbitlbl |label=0x17 |value=Colossus Reactor (Battlecruiser energy)}}
    {{formatbitlbl |label=0x18 |value=Ventral Sacs (Overlord transport)}}
    {{formatbitlbl |label=0x19 |value=Antennae (Overlord sight)}}
    {{formatbitlbl |label=0x1A |value=Pneumatized Carapace (Overlord speed)}}
    {{formatbitlbl |label=0x1B |value=Metabolic Boost (Zergling speed)}}
    {{formatbitlbl |label=0x1C |value=Adrenal Glands (Zergling attack speed)}}
    {{formatbitlbl |label=0x1D |value=Muscular Augments (Hydralisk speed)}}
    {{formatbitlbl |label=0x1E |value=Grooved Spines (Hydralisk range)}}
    {{formatbitlbl |label=0x1F |value=Gamete Meiosis (Queen energy)}}
    {{formatbitlbl |label=0x20 |value=Metasynaptic Node (Defiler energy)}}
    {{formatbitlbl |label=0x21 |value=Singularity Charge (Dragoon range)}}
    {{formatbitlbl |label=0x22 |value=Leg Enhancements (Zealot speed)}}
    {{formatbitlbl |label=0x23 |value=Scarab Damage}}
    {{formatbitlbl |label=0x24 |value=Reaver Capacity}}
    {{formatbitlbl |label=0x25 |value=Gravitic Drive (Shuttle speed)}}
    {{formatbitlbl |label=0x26 |value=Sensor Array (Observer sight)}}
    {{formatbitlbl |label=0x27 |value=Gravitic Boosters (Observer speed)}}
    {{formatbitlbl |label=0x28 |value=Khaydarin Amulet (High Templar energy)}}
    {{formatbitlbl |label=0x29 |value=Apial Sensors (Scout sight)}}
    {{formatbitlbl |label=0x2A |value=Gravitic Thrusters (Scout speed)}}
    {{formatbitlbl |label=0x2B |value=Carrier Capacity}}
    {{formatbitlbl |label=0x2C |value=Khaydarin Core (Arbiter energy)}}
    {{formatbitlbl |label=0x2D |value=Unused 45}}
    {{formatbitlbl |label=0x2E |value=Unused 46}}
    {{formatbitlbl |label=0x2F |value=Argus Jewel (Corsair energy)}}
    {{formatbitlbl |label=0x30 |value=Unused 48}}
    {{formatbitlbl |label=0x31 |value=Argus Talisman (Dark Archon energy)}}
    {{formatbitlbl |label=0x32 |value=Unused 50}}
    {{formatbitlbl |label=0x33 |value=Caduceus Reactor (Medic energy)}}
    {{formatbitlbl |label=0x34 |value=Chitinous Plating (Ultralisk armor)}}
    {{formatbitlbl |label=0x35 |value=Anabolic Synthesis (Ultralisk speed)}}
    {{formatbitlbl |label=0x36 |value=Charon Booster (Goliath air range)}}
    {{formatbitlbl |label=0x37 |value=Unused 55}}
    {{formatbitlbl |label=0x38 |value=Unused 56}}
    {{formatbitlbl |label=0x39 |value=Unused 57}}
    {{formatbitlbl |label=0x3A |value=Unused 58}}
    {{formatbitlbl |label=0x3B |value=Unused 59}}
    {{formatbitlbl |label=0x3C |value=None (no upgrade)}}
  {{end-bittable}} }}
{{end-formattable}}

