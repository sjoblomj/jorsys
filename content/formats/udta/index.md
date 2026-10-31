# UDTA Format

UDTA holds the data for the units in WarCraft II: their graphics, hit points, costs, sizes, ranges, armor, damage, flags and more, with one entry per unit (see Appendix: Unit Types). The layout is the same in all versions. UDTA data is found in three places:

1. The default copies: MAINDAT.WAR has two. Entry 472 holds the full 5948 bytes in the layout below, with nothing in front of them, and is the one the game uses whenever a map does not give its own unit data. Entry 0 holds 5694 bytes: the same layout without Graphics: Swamp, and with different values for some units. The game loads entry 0 when it starts and then loads entry 472 over it. Only entry 0's four Graphics lists (General, Forest, Winter and Wasteland) are kept, in a spare copy that is never used for drawing; it is only written into saved games, where loading skips it. Both entries are the same in versions 1.3, 1.33 and 1.5.
2. PUD files (maps): a PUD can have a UDTA section, but it does not need one. In a PUD the section starts with 2 bytes in front of the data (not counted in the offsets here). The data can be 5694 bytes (without Graphics: Swamp), so the section is 5696 bytes, or the full 5948 bytes, so the section is 5950 bytes; the game accepts both. If both bytes are 0, the game reads the data that follows and uses it instead of the default copy. Otherwise the game skips the data, even though it is there, and uses the default copy (entry 472). A PUD without a UDTA section also gets the default copy. The Graphics lists (General, Forest, Winter, Wasteland and Swamp) in a PUD are always skipped, even when the rest of the data is read, so the game always uses the Graphics lists of entry 472.
3. Saved games (.SAV files): when the game is saved, the UDTA data in use at that moment is written to the save file in the 5694-byte layout, except that the four Graphics lists written are the ones kept from entry 0. When the save is loaded, the data replaces the unit data from the map, but the Graphics lists are skipped.

## Graphics: Construction Site
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=220 bytes (2 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=The construction site graphic shown while this building is being built. The game adds 110 to the value and uses the result as an entry in the Graphics lists below, where entries 116 to 126 are the construction sites; for example 6 (entry 116) is the land construction site and 15 (entry 125) the wall construction site. Frame 0 of the construction site is shown for the first quarter of the construction and frame 1 for the second quarter; after that the building's own graphic is used.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 16. Only used while the unit is being built.}}
{{end-formattable}}

## Graphics: General
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x00DC}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / 127 entries)}}
  {{formatlbl |label=Description |value=The graphic this unit uses on all tilesets. When the tileset's own Graphics list has an entry for the unit (not 0xFFFF), that one is used instead. Most units only set this one; buildings and the critter use the tileset-specific lists. Entries 0 to 109 are the units. Entries 110 to 126 are extra graphics: 110 and 111 are the peasant and peon carrying lumber, 112 and 113 the peasant and peon carrying gold, 114 and 115 the human and orc oil tanker carrying oil, and 116 to 126 (in the tileset lists) the construction sites (see Graphics: Construction Site).}}
  {{formatlbl |label=Values |value=0xFFFF means no graphic. Otherwise bits 0 to 14 are a file reference into the .war archives (the entry number plus 1000 for MAINDAT.WAR, so 1045 is entry 45 of MAINDAT.WAR).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0F |value=Reuse: instead of loading the graphic again, use the one already loaded for an earlier entry in the same list whose bits 0 to 14 are the same.}}
  {{end-bittable}} }}
{{end-formattable}}

## Graphics: Forest
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x01DA}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / 127 entries)}}
  {{formatlbl |label=Description |value=The graphic this unit uses on Forest maps. 0xFFFF means the unit uses its Graphics: General entry on this tileset.}}
  {{formatlbl |label=Values |value=0xFFFF means no graphic. Otherwise bits 0 to 14 are a file reference into the .war archives (the entry number plus 1000 for MAINDAT.WAR, so 1045 is entry 45 of MAINDAT.WAR).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0F |value=Reuse: instead of loading the graphic again, use the one already loaded for an earlier entry in the same list whose bits 0 to 14 are the same.}}
  {{end-bittable}} }}
{{end-formattable}}

## Graphics: Winter
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02D8}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / 127 entries)}}
  {{formatlbl |label=Description |value=The graphic this unit uses on Winter maps. 0xFFFF means the unit uses its Graphics: General entry on this tileset.}}
  {{formatlbl |label=Values |value=0xFFFF means no graphic. Otherwise bits 0 to 14 are a file reference into the .war archives (the entry number plus 1000 for MAINDAT.WAR, so 1045 is entry 45 of MAINDAT.WAR).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0F |value=Reuse: instead of loading the graphic again, use the one already loaded for an earlier entry in the same list whose bits 0 to 14 are the same.}}
  {{end-bittable}} }}
{{end-formattable}}

## Graphics: Wasteland
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x03D6}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / 127 entries)}}
  {{formatlbl |label=Description |value=The graphic this unit uses on Wasteland maps. 0xFFFF means the unit uses its Graphics: General entry on this tileset.}}
  {{formatlbl |label=Values |value=0xFFFF means no graphic. Otherwise bits 0 to 14 are a file reference into the .war archives (the entry number plus 1000 for MAINDAT.WAR, so 1045 is entry 45 of MAINDAT.WAR).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0F |value=Reuse: instead of loading the graphic again, use the one already loaded for an earlier entry in the same list whose bits 0 to 14 are the same.}}
  {{end-bittable}} }}
{{end-formattable}}

## Range: Sight
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x04D4}}
  {{formatlbl |label=Length |value=440 bytes (1 long / First 110 Units)}}
  {{formatlbl |label=Description |value=Sight range (in tiles) of this unit: the unit reveals a square area of 2 × range + 1 tiles on each side around it. Rangers and Berserkers use 9 instead once their player has the sight upgrade (Scouting).}}
  {{formatlbl |label=Values |value=Integer value between 0 and 9. The game uses the value as an entry in a table of 10 sight routines, so larger values are invalid. 0 works the same as 1.}}
{{end-formattable}}

## Hitpoints
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x068C}}
  {{formatlbl |label=Length |value=220 bytes (2 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=Hitpoints for this Unit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Magic Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0768}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Copied into the unit's mana when the unit is created or changes type. It does not make the unit a spellcaster: whether a unit regains mana over time, and whether it starts with 85 mana, is decided by the Spellcaster bit (0x11) in Unit Flags.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (not a magic user)}}
    {{formatbitlbl |label=0x01 |value=true (magic user)}}
  {{end-bittable}} }}
{{end-formattable}}

## Cost: Build Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x07D6}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Time required to build or train this Unit. A higher value takes longer.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Cost: Gold
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0844}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=The amount of Gold required to build this Unit. Multiply by 10 to get actual value.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Cost: Lumber
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x08B2}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Amount of Lumber required to build this Unit. Multiply by 10 to obtain actual value.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 255.}}
{{end-formattable}}

## Cost: Oil
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0920}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Amount of oil required to build this unit. Multiply by 10 to obtain actual value.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Size: Unit
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x098E}}
  {{formatlbl |label=Length |value=440 bytes (4 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=First two bytes are the X size (width), second two are the Y size (height).}}
  {{formatlbl |label=Values |value=Two integer values between 0 and 65535.}}
{{end-formattable}}

## Size: Box
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0B46}}
  {{formatlbl |label=Length |value=440 bytes (4 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=First two bytes are the X size (width), second two are the Y size (height).}}
  {{formatlbl |label=Values |value=Two integer values between 0 and 65535.}}
{{end-formattable}}

## Attack Range
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0CFE}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Maximum distance (in tiles) from which this unit can attack its target. Rangers and Berserkers get one more once their player has the range upgrade (Longbow / Lighter Axes).}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## React Range: Computer AI
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0D6C}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=How far (in tiles) a computer player's unit of this type looks for enemies to attack.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## React Range: Human AI
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0DDA}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=How far (in tiles) a human player's unit of this type looks for enemies to attack while it is walking somewhere, for example while patrolling. A human player's unit that is standing still only looks within its attack range.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Armor
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0E48}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Amount of armor this unit has.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Multiselectable Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0EB6}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Flag which determines whether the unit can be selected with other units.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (not multiselectable)}}
    {{formatbitlbl |label=0x01 |value=true (multiselectable)}}
  {{end-bittable}} }}
{{end-formattable}}

## Priority / AI Treatment
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0F24}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Used when a unit picks an enemy to attack by itself. Enemies that can attack come first (those within the unit's attack range before those further away), and among those the game picks the one with the highest priority minus a penalty for distance.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Damage: Basic
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0F92}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Basic damage dealt by this unit when it attacks.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Damage: Piercing
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1000}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Piercing damage dealt by this unit when it attacks.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Weapon Upgrade Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x106E}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Flag which determines whether this unit upgrades its weapon.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (no weapon upgrade)}}
    {{formatbitlbl |label=0x01 |value=true (weapon upgrade)}}
  {{end-bittable}} }}
{{end-formattable}}

## Armor Upgrade Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x10DC}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Flag which determines whether this unit upgrades its armor.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (no armor upgrade)}}
    {{formatbitlbl |label=0x01 |value=true (armor upgrade)}}
  {{end-bittable}} }}
{{end-formattable}}

## Weapon Missile
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x114A}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Missile this unit fires when it attacks. 0x1D (None) means the unit attacks in melee.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Lightning}}
    {{formatbitlbl |label=0x01 |value=Griffon Hammer}}
    {{formatbitlbl |label=0x02 |value=Dragon Breath and Fireball}}
    {{formatbitlbl |label=0x03 |value=Flameshield Fireball}}
    {{formatbitlbl |label=0x04 |value=Flame Shield}}
    {{formatbitlbl |label=0x05 |value=Blizzard}}
    {{formatbitlbl |label=0x06 |value=Death &amp; Decay}}
    {{formatbitlbl |label=0x07 |value=Big Cannon}}
    {{formatbitlbl |label=0x08 |value=Exorcism}}
    {{formatbitlbl |label=0x09 |value=Heal Effect}}
    {{formatbitlbl |label=0x0A |value=Touch of Death}}
    {{formatbitlbl |label=0x0B |value=Rune}}
    {{formatbitlbl |label=0x0C |value=Tornado (Whirlwind)}}
    {{formatbitlbl |label=0x0D |value=Catapult Rock}}
    {{formatbitlbl |label=0x0E |value=Ballista Bolt}}
    {{formatbitlbl |label=0x0F |value=Arrow}}
    {{formatbitlbl |label=0x10 |value=Axe}}
    {{formatbitlbl |label=0x11 |value=Submarine Missile}}
    {{formatbitlbl |label=0x12 |value=Turtle Missile}}
    {{formatbitlbl |label=0x13 |value=Small Fire}}
    {{formatbitlbl |label=0x14 |value=Big Fire}}
    {{formatbitlbl |label=0x15 |value=Ballista &amp; Catapult Impact}}
    {{formatbitlbl |label=0x16 |value=Normal Spell}}
    {{formatbitlbl |label=0x17 |value=Explosion}}
    {{formatbitlbl |label=0x18 |value=Cannon}}
    {{formatbitlbl |label=0x19 |value=Cannon Fire (shown at the unit that fires Cannon or Big Cannon)}}
    {{formatbitlbl |label=0x1A |value=Cannon Explosion (shown where Cannon or Big Cannon hits)}}
    {{formatbitlbl |label=0x1B |value=Daemon Fire}}
    {{formatbitlbl |label=0x1C |value=Green Cross}}
    {{formatbitlbl |label=0x1D |value=None (melee)}}
  {{end-bittable}} }}
{{end-formattable}}

## Unit Type
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x11B8}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Whether the unit is a land, air or sea unit. Not only visual: the game copies it into each unit when the unit is created, and uses it, for example, when looking for a free square to place the unit on and when a missile hits the unit.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Land}}
    {{formatbitlbl |label=0x01 |value=Air}}
    {{formatbitlbl |label=0x02 |value=Sea}}
  {{end-bittable}} }}
{{end-formattable}}

## Decay Rate
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1226}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=How fast this unit decays. A unit with a non-zero decay rate gets a hidden timer that starts at 255. The game counts the decay rate down over and over; each time it runs out, the timer goes down by one and the unit's hit points are not affected. Once the timer reaches 0, the unit loses 5 hit points each time instead, and dies when it has fewer than 5 left. Decay rates only apply to units created during the game, not those placed on the map at design time, and never to units with the Spellcaster bit (0x11) in Unit Flags.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. 0 means the unit never decays.}}
{{end-formattable}}

## Repair Priority (Computer)
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1294}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=How urgently a computer player repairs this building. When a computer player's peasant or peon looks for a building to repair, it considers its player's finished buildings in the same area that have less than 3/4 of their hit points, and picks the one with the highest value. This is the only place the game uses this field.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. Only matters for buildings.}}
{{end-formattable}}

## Right Click Action
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1302}}
  {{formatlbl |label=Length |value=58 bytes (1 byte / First 58 Units)}}
  {{formatlbl |label=Description |value=What this unit does when you have it selected and right click. The game turns the right click into an order depending on this value and on what was clicked.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=None: nothing happens}}
    {{formatbitlbl |label=0x01 |value=Attack: Attack an enemy unit, Attack Wall on a wall, otherwise Move. Units without the Attacks bit (0x13) in Unit Flags always Move}}
    {{formatbitlbl |label=0x02 |value=Move}}
    {{formatbitlbl |label=0x03 |value=Harvest: Attack an enemy unit; Harvest a gold mine or trees when not carrying anything; Return with Goods to an own building that takes what is carried; Repair a damaged own building; otherwise Move}}
    {{formatbitlbl |label=0x04 |value=Haul Oil: Harvest an own oil platform when empty; Return with Goods to an own building that takes oil when carrying oil; otherwise Move}}
    {{formatbitlbl |label=0x05 |value=Demolish: Demolish an enemy unit, otherwise Move}}
    {{formatbitlbl |label=0x06 |value=Sail: the same as Move}}
  {{end-bittable}} }}
{{end-formattable}}

## Point Value
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x133C}}
  {{formatlbl |label=Length |value=220 bytes (2 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=Point value awarded towards total score for a player which destroys this unit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Weapon Attack Domain
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1418}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Domain whose units this unit can attack.}}
  {{formatlbl |label=Values |value=Bit flags; any combination is valid (just add them together). 0 means the unit cannot attack.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=None}}
    {{formatbitlbl |label=0x01 |value=Land}}
    {{formatbitlbl |label=0x02 |value=Sea}}
    {{formatbitlbl |label=0x04 |value=Air}}
  {{end-bittable}} }}
{{end-formattable}}

## Unit Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1486}}
  {{formatlbl |label=Length |value=440 bytes (4 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=Flags which determine special properties this unit has.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Land Unit; Set on all land units in the default data. It has no effect of its own; it only counts as one of the mobile-unit bits. Bits 0x00 to 0x04 together mark a unit as a mobile unit rather than a building: much of the game only checks whether any of them is set (e.g. only such units respond to right clicks). Whether a unit moves on land, sea or in the air is decided by the Unit Type field, not by this bit.}}
    {{formatbitlbl |label=0x01 |value=Air Unit; Set on the flying units (Kurdran, Deathwing, Gnomish Flying Machine, Goblin Zeppelin, Gryphon Rider, Dragon, Eye of Kilrogg, Daemon) in the default data. When a unit picks an enemy to attack by itself, air units (and submarines) within its attack range are preferred over everything else; an air unit does not pick enemy air units that cannot attack. The flag also gives the unit the same death sound as units with Exploding Death (0x02), and computer players count it as an air unit when forming attack groups. Bits 0x00 to 0x04 together mark a unit as a mobile unit rather than a building: much of the game only checks whether any of them is set (e.g. only such units respond to right clicks).}}
    {{formatbitlbl |label=0x02 |value=Exploding Death; Set on the Ballista and Catapult in the default data. The unit explodes when killed (missile 23, Explosion), uses the death sound shared with air units, and does not play the idle animation (turning around now and then) when standing still. Its basic damage is increased by the Ballista/Catapult weapon upgrade, by 15 for each level, instead of the normal weapon upgrade. Bits 0x00 to 0x04 together mark a unit as a mobile unit rather than a building: much of the game only checks whether any of them is set (e.g. only such units respond to right clicks).}}
    {{formatbitlbl |label=0x03 |value=Sea Unit; Set on the ships in the default data. Its weapon and armor upgrades come from the ship upgrades: 5 extra basic damage and 5 extra armor for each level, instead of 2 for land units. While standing still, the unit bobs up and down. A sea unit that returns with goods delivers oil. Submarines can attack it, and computer players count it as a sea unit when forming attack groups. Bits 0x00 to 0x04 together mark a unit as a mobile unit rather than a building: much of the game only checks whether any of them is set (e.g. only such units respond to right clicks).}}
    {{formatbitlbl |label=0x04 |value=Critter; Set on the Critter, Skeleton and Daemon in the default data. When the player's unit with this bit is attacked, the "under attack" warning is not given. When the game places such a unit next to a spot (as for Raise Dead, the daemon and Polymorph), missile 22 (Normal Spell) is shown on it. Bits 0x00 to 0x04 together mark a unit as a mobile unit rather than a building: much of the game only checks whether any of them is set (e.g. only such units respond to right clicks).}}
    {{formatbitlbl |label=0x05 |value=Building; Set on all buildings, the gold mine, the oil patch, the Circle of Power, the Dark Portal, the Runestone, walls and the destroyed sites in the default data. A peasant or peon right-clicked on a damaged own building repairs it, and computer players' workers repair such buildings by themselves. While the player's own building is being built or is busy, the progress bar is shown when it is selected. When one is attacked, the warning sound for buildings is used instead of the one for units.}}
    {{formatbitlbl |label=0x06 |value=Submarine; Set on the Gnomish Submarine and Giant Turtle in the default data. The unit cannot be seen by other players, except when one of their units with Submarine Spotter (0x07) is close enough. It can only attack sea units (0x03), oil platforms (0x0B) and shore buildings (0x10). When a unit picks an enemy to attack by itself, submarines within its attack range are preferred like air units.}}
    {{formatbitlbl |label=0x07 |value=Submarine Spotter; Set on the flying units, the submarines, and the scout, guard and cannon towers in the default data. Submarines (0x06) of other players near the unit become visible to its player.}}
    {{formatbitlbl |label=0x08 |value=Peon; Set on the Peasant and Peon in the default data. While carrying goods, the unit is drawn with the graphics for carrying lumber or gold (Graphics entries 110 to 113). A computer player's unit with this bit looks for damaged buildings to repair when it is idle. The flag also makes it a non-combatant, like Mage (0x1A).}}
    {{formatbitlbl |label=0x09 |value=Tanker; Set on the human and orc Oil Tanker in the default data. While carrying oil, the unit is drawn with the graphic for a full tanker (Graphics entries 114 and 115). The flag also makes it a non-combatant, like Mage (0x1A).}}
    {{formatbitlbl |label=0x0A |value=Transport; Set on the human and orc Transport in the default data. The unit carries up to six passengers: a friendly unit moved onto it boards it, and Unload Passengers puts them ashore. Peasants and peons can repair it like a building.}}
    {{formatbitlbl |label=0x0B |value=Oil Platform; Set on the human and orc Oil Platform in the default data. It must be built on top of an oil patch, and takes over the oil left in the patch. Tankers harvest oil from it. Submarines can attack it. Shipyards and refineries cannot be built within 4 squares of it. Computer players' workers do not repair it.}}
    {{formatbitlbl |label=0x0C |value=Gold Storage; Set on the Town Hall, Great Hall, Keep, Stronghold, Castle and Fortress in the default data. Peasants and peons deliver both gold and lumber to it. It cannot be built within 3 squares of a gold mine (0x16) ("You cannot build a townhall too near a goldmine").}}
    {{formatbitlbl |label=0x0D |value=Leaves no remains; Set on the dead body and the destroyed sites in the default data. When a unit with this bit is killed, it is removed straight away, instead of turning into a dead body (units) or leaving a destroyed site behind (buildings).}}
    {{formatbitlbl |label=0x0E |value=Attack Ground; Set on the Ballista, Catapult, Battleship and Juggernaught in the default data. Only units with this bit can be given the Attack Ground order, and the Attack Ground button is shown when one of the selected units has it. While attacking an enemy it found by itself, the unit holds fire when units of its own player are within one square of the target.}}
    {{formatbitlbl |label=0x0F |value=Undead; Set on the Death Knight, Teron Gorefiend, Gul'dan and the Skeleton in the default data. Exorcism damages only units with this bit.}}
    {{formatbitlbl |label=0x10 |value=Shore Building; Set on the shipyards, foundries and refineries in the default data. It must be built on the coast. Except for the foundries, it cannot be built within 4 squares of an oil patch or an oil platform ("You cannot build too near a patch of oil"). Submarines can attack it.}}
    {{formatbitlbl |label=0x11 |value=Spellcaster; Set on the Mage, Death Knight, Paladin, Ogre-Mage and the heroes that use mana (Teron Gorefiend, Dentarg, Khadgar, Turalyon, Cho'gall, Gul'dan, Uther Lightbringer) in the default data. The unit has mana: it starts with 85 when created and regains it over time, and the stats panel shows it as "Magic:". Units with this bit never decay (see Decay Rate).}}
    {{formatbitlbl |label=0x12 |value=Lumber Storage; Set on the Elven Lumber Mill and Troll Lumber Mill in the default data. Peasants and peons deliver lumber (but not gold) to it.}}
    {{formatbitlbl |label=0x13 |value=Attacks; Set on all units that can fight, and the guard and cannon towers, in the default data. Right click Attack (see Right Click Action) only gives an attack order to units with this bit. When a unit picks an enemy to attack by itself, enemies with this bit are preferred over those without it. Only units with this bit come to help when a nearby friendly unit is attacked, and computer players only pick units with this bit for attack groups.}}
    {{formatbitlbl |label=0x14 |value=Tower; Set on the guard and cannon towers in the default data. When finished or upgraded, the building starts in the Tower Guard action, attacking enemies in range. Towers do not come to help when a nearby friendly unit is attacked.}}
    {{formatbitlbl |label=0x15 |value=Oil Patch; Set on the oil patch in the default data. Shipyards and refineries cannot be built within 4 squares of it. (Whether an oil platform is built on an oil patch is checked by the unit number, not by this bit.)}}
    {{formatbitlbl |label=0x16 |value=Gold Mine; Set on the gold mine in the default data. Its only use: buildings with Gold Storage (0x0C) cannot be built within 3 squares of it. (Harvesting checks the unit number of the gold mine, not this bit.)}}
    {{formatbitlbl |label=0x17 |value=Hero; Set on Cho'gall, Lothar, Gul'dan, Uther Lightbringer and Zul'jin in the default data. When the level's Rescue Table entry requires a special unit (0x1000), one of the rescued units must have this bit.}}
    {{formatbitlbl |label=0x18 |value=Oil Storage; Set on the shipyards and refineries in the default data. A tanker carrying oil that is right-clicked on it returns its oil there.}}
    {{formatbitlbl |label=0x19 |value=Sapper; Set on the Dwarven Demolition Squad and Goblin Sappers in the default data; it does not make them explode (that is the Demolish order). The flag makes it a non-combatant, like Mage (0x1A), and gives the unit the same death sound as units with Exploding Death (0x02) and air units.}}
    {{formatbitlbl |label=0x1A |value=Mage; Set on the Mage, Death Knight, Teron Gorefiend and Khadgar in the default data. The flag only means it is Non-combatant: when attacked, the unit moves away instead of fighting back; it does not come to help nearby friendly units that are attacked; computer players never pick it for an attack group; and when looking for enemies it plans its path around enemy units instead of through them. Peon (0x08), Tanker (0x09) and Sapper (0x19) also make a unit a non-combatant.}}
    {{formatbitlbl |label=0x1B |value=Organic; Set on all living units in the default data (not on ballistas, catapults, ships, the Gnomish Flying Machine, the Goblin Zeppelin or the Eye of Kilrogg). Healing, Bloodlust, Polymorph and Death Coil only affect units with this bit.}}
    {{formatbitlbl |label=0x1C |value=Unused; Not set on any unit in the default data, and the game never checks it.}}
    {{formatbitlbl |label=0x1D |value=Unused; Not set on any unit in the default data, and the game never checks it.}}
    {{formatbitlbl |label=0x1E |value=Unused; Not set on any unit in the default data, and the game never checks it.}}
    {{formatbitlbl |label=0x1F |value=Unused; Not set on any unit in the default data, and the game never checks it.}}
  {{end-bittable}} }}
{{end-formattable}}

## Graphics: Swamp
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x163E}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / 127 entries)}}
  {{formatlbl |label=Description |value=The graphic this unit uses on Swamp maps. 0xFFFF means the unit uses its Graphics: General entry on this tileset. Only present in the Beyond the Dark Portal format: with this field the UDTA data is 5948 bytes long, without it 5694 bytes (see the description of this section).}}
  {{formatlbl |label=Values |value=0xFFFF means no graphic. Otherwise bits 0 to 14 are a file reference into the .war archives (the entry number plus 1000 for MAINDAT.WAR, so 1045 is entry 45 of MAINDAT.WAR).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0F |value=Reuse: instead of loading the graphic again, use the one already loaded for an earlier entry in the same list whose bits 0 to 14 are the same.}}
  {{end-bittable}} }}
{{end-formattable}}

---

## Appendix: Unit Types
{{begin-formattable}}
  {{formatlbl |label=Description |value=The unit list. The per-unit fields have one entry per unit in this order: the fields with 110 entries cover 0x00 to 0x6D, and the Graphics lists have 127 entries (see Graphics: General for the extra entries after the units). The numbers are the same as in the Train and Build command buttons of WAR2.EXE. The entries marked Unused have no name in the game.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Footman}}
    {{formatbitlbl |label=0x01 |value=Grunt}}
    {{formatbitlbl |label=0x02 |value=Peasant}}
    {{formatbitlbl |label=0x03 |value=Peon}}
    {{formatbitlbl |label=0x04 |value=Ballista}}
    {{formatbitlbl |label=0x05 |value=Catapult}}
    {{formatbitlbl |label=0x06 |value=Knight}}
    {{formatbitlbl |label=0x07 |value=Ogre}}
    {{formatbitlbl |label=0x08 |value=Elven Archer}}
    {{formatbitlbl |label=0x09 |value=Troll Axethrower}}
    {{formatbitlbl |label=0x0A |value=Mage}}
    {{formatbitlbl |label=0x0B |value=Death Knight}}
    {{formatbitlbl |label=0x0C |value=Paladin}}
    {{formatbitlbl |label=0x0D |value=Ogre-Mage}}
    {{formatbitlbl |label=0x0E |value=Dwarven Demolition Squad}}
    {{formatbitlbl |label=0x0F |value=Goblin Sappers}}
    {{formatbitlbl |label=0x10 |value=Attack Peasant}}
    {{formatbitlbl |label=0x11 |value=Attack Peon}}
    {{formatbitlbl |label=0x12 |value=Ranger}}
    {{formatbitlbl |label=0x13 |value=Berserker}}
    {{formatbitlbl |label=0x14 |value=Alleria}}
    {{formatbitlbl |label=0x15 |value=Teron Gorefiend}}
    {{formatbitlbl |label=0x16 |value=Kurdran and Sky'ree}}
    {{formatbitlbl |label=0x17 |value=Dentarg}}
    {{formatbitlbl |label=0x18 |value=Khadgar}}
    {{formatbitlbl |label=0x19 |value=Grom Hellscream}}
    {{formatbitlbl |label=0x1A |value=Human Oil Tanker}}
    {{formatbitlbl |label=0x1B |value=Orc Oil Tanker}}
    {{formatbitlbl |label=0x1C |value=Human Transport}}
    {{formatbitlbl |label=0x1D |value=Orc Transport}}
    {{formatbitlbl |label=0x1E |value=Elven Destroyer}}
    {{formatbitlbl |label=0x1F |value=Troll Destroyer}}
    {{formatbitlbl |label=0x20 |value=Battleship}}
    {{formatbitlbl |label=0x21 |value=Ogre Juggernaught}}
    {{formatbitlbl |label=0x22 |value=Unused 0x22}}
    {{formatbitlbl |label=0x23 |value=Deathwing}}
    {{formatbitlbl |label=0x24 |value=Unused 0x24}}
    {{formatbitlbl |label=0x25 |value=Unused 0x25}}
    {{formatbitlbl |label=0x26 |value=Gnomish Submarine}}
    {{formatbitlbl |label=0x27 |value=Giant Turtle}}
    {{formatbitlbl |label=0x28 |value=Gnomish Flying Machine}}
    {{formatbitlbl |label=0x29 |value=Goblin Zeppelin}}
    {{formatbitlbl |label=0x2A |value=Gryphon Rider}}
    {{formatbitlbl |label=0x2B |value=Dragon}}
    {{formatbitlbl |label=0x2C |value=Turalyon}}
    {{formatbitlbl |label=0x2D |value=Eye of Kilrogg}}
    {{formatbitlbl |label=0x2E |value=Danath}}
    {{formatbitlbl |label=0x2F |value=Korgath Bladefist}}
    {{formatbitlbl |label=0x30 |value=Unused 0x30}}
    {{formatbitlbl |label=0x31 |value=Cho'gall}}
    {{formatbitlbl |label=0x32 |value=Lothar}}
    {{formatbitlbl |label=0x33 |value=Gul'dan}}
    {{formatbitlbl |label=0x34 |value=Uther Lightbringer}}
    {{formatbitlbl |label=0x35 |value=Zuljin}}
    {{formatbitlbl |label=0x36 |value=Unused 0x36}}
    {{formatbitlbl |label=0x37 |value=Skeleton}}
    {{formatbitlbl |label=0x38 |value=Daemon}}
    {{formatbitlbl |label=0x39 |value=Critter}}
    {{formatbitlbl |label=0x3A |value=Farm}}
    {{formatbitlbl |label=0x3B |value=Pig Farm}}
    {{formatbitlbl |label=0x3C |value=Human Barracks}}
    {{formatbitlbl |label=0x3D |value=Orc Barracks}}
    {{formatbitlbl |label=0x3E |value=Church}}
    {{formatbitlbl |label=0x3F |value=Altar of Storms}}
    {{formatbitlbl |label=0x40 |value=Scout Tower (Human)}}
    {{formatbitlbl |label=0x41 |value=Watch Tower (Orc)}}
    {{formatbitlbl |label=0x42 |value=Stables}}
    {{formatbitlbl |label=0x43 |value=Ogre Mound}}
    {{formatbitlbl |label=0x44 |value=Gnomish Inventor}}
    {{formatbitlbl |label=0x45 |value=Goblin Alchemist}}
    {{formatbitlbl |label=0x46 |value=Gryphon Aviary}}
    {{formatbitlbl |label=0x47 |value=Dragon Roost}}
    {{formatbitlbl |label=0x48 |value=Human Shipyard}}
    {{formatbitlbl |label=0x49 |value=Orc Shipyard}}
    {{formatbitlbl |label=0x4A |value=Town Hall}}
    {{formatbitlbl |label=0x4B |value=Great Hall}}
    {{formatbitlbl |label=0x4C |value=Elven Lumber Mill}}
    {{formatbitlbl |label=0x4D |value=Troll Lumber Mill}}
    {{formatbitlbl |label=0x4E |value=Human Foundry}}
    {{formatbitlbl |label=0x4F |value=Orc Foundry}}
    {{formatbitlbl |label=0x50 |value=Mage Tower}}
    {{formatbitlbl |label=0x51 |value=Temple of the Damned}}
    {{formatbitlbl |label=0x52 |value=Human Blacksmith}}
    {{formatbitlbl |label=0x53 |value=Orc Blacksmith}}
    {{formatbitlbl |label=0x54 |value=Human Refinery}}
    {{formatbitlbl |label=0x55 |value=Orc Refinery}}
    {{formatbitlbl |label=0x56 |value=Human Oil Platform}}
    {{formatbitlbl |label=0x57 |value=Orc Oil Platform}}
    {{formatbitlbl |label=0x58 |value=Keep}}
    {{formatbitlbl |label=0x59 |value=Stronghold}}
    {{formatbitlbl |label=0x5A |value=Castle}}
    {{formatbitlbl |label=0x5B |value=Fortress}}
    {{formatbitlbl |label=0x5C |value=Gold Mine}}
    {{formatbitlbl |label=0x5D |value=Oil Patch}}
    {{formatbitlbl |label=0x5E |value=Human Start Location}}
    {{formatbitlbl |label=0x5F |value=Orc Start Location}}
    {{formatbitlbl |label=0x60 |value=Human Guard Tower}}
    {{formatbitlbl |label=0x61 |value=Orc Guard Tower}}
    {{formatbitlbl |label=0x62 |value=Human Cannon Tower}}
    {{formatbitlbl |label=0x63 |value=Orc Cannon Tower}}
    {{formatbitlbl |label=0x64 |value=Circle of Power}}
    {{formatbitlbl |label=0x65 |value=Dark Portal}}
    {{formatbitlbl |label=0x66 |value=Runestone}}
    {{formatbitlbl |label=0x67 |value=Wall (Human)}}
    {{formatbitlbl |label=0x68 |value=Wall (Orc)}}
    {{formatbitlbl |label=0x69 |value=Dead Body}}
    {{formatbitlbl |label=0x6A |value=Destroyed Site (1x1)}}
    {{formatbitlbl |label=0x6B |value=Destroyed Site (2x2)}}
    {{formatbitlbl |label=0x6C |value=Destroyed Site (3x3)}}
    {{formatbitlbl |label=0x6D |value=Destroyed Site (4x4)}}
  {{end-bittable}} }}
{{end-formattable}}

