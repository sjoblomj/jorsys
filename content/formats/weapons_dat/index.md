# weapons.dat Format

weapons.dat holds the data for the weapons units attack with, and for the spells that work by firing a weapon (see Appendix: Weapons list): the bullet each fires, what it can target, its range, damage and how the damage is dealt, its cooldown, and the name, icon and error message shown for it. It is the file arr\weapons.dat in the game's MPQ archives and is 5460 bytes long. Each field below is a list with one entry for each of the 130 weapons, and the lists are stored one after another with nothing in between, so the offsets are from the start of the file. The layout is the same in every version from 1.04 to 1.17, of both StarCraft and Brood War, and StarEdit reads the file in the same layout. StarCraft 1.00 to 1.03 used an older, shorter layout with 100 weapons (4200 bytes). That older file is still in StarDat.mpq in later versions, but it is never loaded: the newer copy in patch_rt.mpq (or, in 1.05 to 1.07, BrooDat.mpq) is found first. The patch_rt.mpq copy is the same in 1.08 to 1.17; the BrooDat.mpq copy differs from it only in the maximum range of weapon 7 (160 instead of 192) and the damage of weapons 84 (16 instead of 14) and 103 (5 instead of 6). The game loads the file again each time a game starts, before the map's own settings are applied. Fields are read in order, and the game stops with a file error if the file is longer than the layout. A shorter file that ends exactly where a field ends loads without an error; the fields after the end then keep whatever they held before.

Which weapons a unit uses is set in units.dat (Ground Weapon and Air Weapon). Weapon number 130 means "no weapon" there; it has no entry in this file. No field is checked against the size of the table it points into, so out-of-range values read whatever follows in memory.

A map can replace Damage and Bonus. Its unit settings (the CHK section UNIS in StarCraft maps and UNIx in Brood War maps) hold them for each weapon, and for every unit whose "use default settings" flag is clear, they are copied into the unit's ground and air weapon (those of its turret, if it has one). Weapons of units left at their defaults keep the values of this file. Saved games store Damage and Bonus as well.

Damage is dealt in steps. A bullet deals (Damage + Bonus × the player's level of the Damage Upgrade) hit points, divided where a splash or bounce says so. The target's shields take it first, less the shield upgrade level (unless the damage class is 4); what is left is reduced by the target's armor plus its armor upgrade level (again unless the class is 4), then multiplied by the factor for the damage class and the target's size (see Damage Class). If the shields took none of the hit, it deals at least half a hit point.

## Label
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Name of the weapon: a string number in rez\stat_txt.tbl, counting from 1. Shown in the tooltip of the weapon icon in a selected unit's status panel, together with the damage. StarEdit shows it in the unit settings.}}
  {{formatlbl |label=Values |value=Integer value between 1 and the number of strings in rez\stat_txt.tbl.}}
{{end-formattable}}

## Graphics
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0104}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=The bullet the weapon fires: an entry of flingy.dat. Only the low 16 bits are used. 0 means the weapon fires no bullet; melee weapons (claws, blades, Toxic Spores and Psi Blades) have 0 and deal their damage straight from the unit's animation script instead.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 208, the last entry of flingy.dat. Higher values are not rejected: the game reads the bullet's settings from the memory after the flingy.dat tables.}}
{{end-formattable}}

## Unused (Technology)
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x030C}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Not used: no code in StarCraft or StarEdit reads this field (checked in 1.05, 1.15.0 and 1.17). In the shipped file it holds the techdata.dat number of the spell the weapon belongs to (for example 1 for Lockdown and 19 for Psionic Storm), and 44, "no technology", for ordinary weapons.}}
  {{formatlbl |label=Values |value=Any value; ignored.}}
{{end-formattable}}

## Target Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x038E}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=What the weapon may be used against. Each bit is a condition the target must meet; the weapon can hit a unit only if it is in the air and bit 0x0001 is set, or on the ground and 0x0002 is set, and all the other set bits allow it. Units that cannot be hit (invincible or in stasis) are always refused. The same test decides which units a splash hurts, so a ground-only splash never hurts air units.}}
  {{formatlbl |label=Values |value=Bit flags; add together. In the shipped file: 0x0001 air only, 0x0002 ground only, 0x0003 both, 0x0012 Spider Mines, 0x0013 Parasite, 0x0017 Lockdown, 0x0043 most area spells, 0x0053 Psionic Storm, 0x00B2 Spawn Broodling, 0x011B Consume.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0001 |value=Can hit units in the air}}
    {{formatbitlbl |label=0x0002 |value=Can hit units on the ground}}
    {{formatbitlbl |label=0x0004 |value=Target must be mechanical (units.dat flag 0x40000000)}}
    {{formatbitlbl |label=0x0008 |value=Target must be organic (units.dat flag 0x10000)}}
    {{formatbitlbl |label=0x0010 |value=Target must not be a building (units.dat flag 0x1)}}
    {{formatbitlbl |label=0x0020 |value=Target must not be robotic (units.dat flag 0x4000)}}
    {{formatbitlbl |label=0x0040 |value=Can be aimed at a position on the ground rather than a unit}}
    {{formatbitlbl |label=0x0080 |value=Target must be organic or mechanical}}
    {{formatbitlbl |label=0x0100 |value=Target must belong to the attacking player}}
    {{formatbitlbl |label=0x0200 to 0x8000 |value=Not used}}
  {{end-bittable}} }}
{{end-formattable}}

## Minimum Range
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0492}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Closest distance, in pixels, at which the weapon can be used; the distance is measured between the edges of the attacker's and the target's dimensions (units.dat). 0 means no minimum. Only the Siege Tank's Arclite Shock Cannon has one in the shipped file (64).}}
  {{formatlbl |label=Values |value=Integer value between 0 and 4294967295.}}
{{end-formattable}}

## Maximum Range
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x069A}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Furthest distance, in pixels, at which the weapon can be used, measured like Minimum Range. Some units add to it: +64 in a Bunker, and the range upgrades, which depend on the unit type, not on the weapon (Marine +32 with U-238 Shells, Goliath +96 for its Hellfire Missile Pack with Charon Booster, Hydralisk +32 with Grooved Spines, Dragoon +64 with Singularity Charge, and, in Brood War games, Alan Schezar's Hellfire Missile Pack +96 and Fenix as Dragoon +64). When units.dat is loaded, each unit's Target Acquisition Range is raised to at least this value ÷ 32 for its ground and air weapon. Bullets with Behaviour 9 fly this far plus 20 pixels.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 4294967295. The shipped values run from 2 to 384.}}
{{end-formattable}}

## Damage Upgrade
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x08A2}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The upgrade (upgrades.dat) whose level multiplies Bonus. Its level is also printed on the weapon's icon in the status panel. Upgrade 60 is used for weapons no upgrade affects; the game has no special case for it (no one can research it, so its level stays 0), but StarEdit greys out the Bonus field for it, or for any upgrade whose Max Level is 0.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 60. Higher values are not rejected: the game reads the level from the memory after the player's upgrade levels (first the levels of the following players, then unrelated data). Common values are:}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x07 |value=Terran Infantry Weapons}}
    {{formatbitlbl |label=0x08 |value=Terran Vehicle Weapons}}
    {{formatbitlbl |label=0x09 |value=Terran Ship Weapons}}
    {{formatbitlbl |label=0x0A |value=Zerg Melee Attacks}}
    {{formatbitlbl |label=0x0B |value=Zerg Missile Attacks}}
    {{formatbitlbl |label=0x0C |value=Zerg Flyer Attacks}}
    {{formatbitlbl |label=0x0D |value=Protoss Ground Weapons}}
    {{formatbitlbl |label=0x0E |value=Protoss Air Weapons}}
    {{formatbitlbl |label=0x23 |value=Scarab Damage}}
    {{formatbitlbl |label=0x3C |value=None (no upgrade)}}
  {{end-bittable}} }}
{{end-formattable}}

## Damage Class
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0924}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=How the damage is scaled by the target's size (Size in units.dat), and whether armor applies. The factors are: independent 0% for every size; explosive 50% against small, 75% against medium, 100% against large; concussive 100%, 50%, 25%; normal and ignore armor 100% for every size. Units of size 0 (independent) get 0% from every class. Because a hit the shields took none of deals at least half a hit point, a 0% hit still deals half a hit point. Class 0 drains shields normally but does not show the shield hit flash. Class 4 skips both the shield upgrade and the armor reduction.}}
  {{formatlbl |label=Values |value=Values above 4 are not rejected: they are treated like classes 1 to 3 (the shield upgrade and armor apply), and their factors are read from the unrelated data after the table.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Independent: 0% (half a hit point per hit)}}
    {{formatbitlbl |label=0x01 |value=Explosive}}
    {{formatbitlbl |label=0x02 |value=Concussive}}
    {{formatbitlbl |label=0x03 |value=Normal}}
    {{formatbitlbl |label=0x04 |value=Ignore Armor}}
  {{end-bittable}} }}
{{end-formattable}}

## Behaviour
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x09A6}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=How the bullet is fired and moves. Behaviours 0, 1, 2 and 7 roll whether the shot misses (the chance depends on, for example, attacking up a cliff or into Dark Swarm); a missed shot lands 30 pixels short and deals no damage to the target. Bullets of all behaviours except 2 and 4 start at the unit, moved by Forward Offset and Upward Offset.}}
  {{formatlbl |label=Values |value=Values of 10 and above make the bullet fail to appear, so the weapon does nothing.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Flies to the position the target had when it fired}}
    {{formatbitlbl |label=0x01 |value=Follows the target (homing), unless it missed}}
    {{formatbitlbl |label=0x02 |value=Appears on the target and hits at once}}
    {{formatbitlbl |label=0x03 |value=Stays at the target position and deals its damage every 7 frames until Lifetime runs out (Psionic Storm)}}
    {{formatbitlbl |label=0x04 |value=Appears at the position the unit was ordered to target and hits at once}}
    {{formatbitlbl |label=0x05 |value=Hits at once from where the attacker stands (melee and short-range weapons)}}
    {{formatbitlbl |label=0x06 |value=Kills the attacking unit (Scourge, Infested Terran)}}
    {{formatbitlbl |label=0x07 |value=Bounces: hits up to 3 targets, each later hit dealing a third of the one before (Glave Wurm)}}
    {{formatbitlbl |label=0x08 |value=Spreads its shots around the target in turn (Halo Rockets)}}
    {{formatbitlbl |label=0x09 |value=Flies straight ahead to Maximum Range plus 20 pixels (Subterranean Spines)}}
  {{end-bittable}} }}
{{end-formattable}}

## Lifetime
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0A28}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=How long the bullet can last, in frames. A flying bullet (Behaviour 0, 1, 8 or 9) is removed when it arrives or after this many frames, whichever comes first; a Behaviour 3 bullet lasts this long and deals its damage every 7 frames (Psionic Storm's 60 gives 9 ticks). Other behaviours do not use it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. Shipped: 30 for Hellfire and Anti-matter Missiles, 60 for Glave Wurm, Seeker Spores, Psionic Storm and Tormentor Missiles, 255 otherwise.}}
{{end-formattable}}

## Damage Type
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0AAA}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=What happens when the bullet hits (or, for Behaviour 3, at each tick). The spells that are weapons (Lockdown, EMP Shockwave and so on) are cast through this field.}}
  {{formatlbl |label=Values |value=Values 19, 20, 23 and anything above 24 stop the game with the fatal error "CBullet: Damage". Mind Control and Feedback have 19 and 20 in the shipped file, but those spells never fire a bullet.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=None}}
    {{formatbitlbl |label=0x01 |value=Damage the target}}
    {{formatbitlbl |label=0x02 |value=Splash: damage every unit around, including the attacker's own (see Splash Radius)}}
    {{formatbitlbl |label=0x03 |value=Enemy splash: as 2, but the attacker's own units other than the target are spared}}
    {{formatbitlbl |label=0x04 |value=Lockdown the target (131 frames)}}
    {{formatbitlbl |label=0x05 |value=Nuclear missile: splash as 2, with damage max(500, ⅔ of the unit's maximum hit points plus shields); Damage and Bonus are ignored}}
    {{formatbitlbl |label=0x06 |value=Parasite}}
    {{formatbitlbl |label=0x07 |value=Spawn Broodling}}
    {{formatbitlbl |label=0x08 |value=EMP Shockwave, with the radius taken from Splash Radius: Inner of weapon 33, whatever this weapon has}}
    {{formatbitlbl |label=0x09 |value=Irradiate}}
    {{formatbitlbl |label=0x0A |value=Ensnare}}
    {{formatbitlbl |label=0x0B |value=Plague}}
    {{formatbitlbl |label=0x0C |value=Stasis Field}}
    {{formatbitlbl |label=0x0D |value=Dark Swarm}}
    {{formatbitlbl |label=0x0E |value=Consume}}
    {{formatbitlbl |label=0x0F |value=Damage the target even if the shot missed (Yamato Gun)}}
    {{formatbitlbl |label=0x10 |value=Restoration}}
    {{formatbitlbl |label=0x11 |value=Disruption Web}}
    {{formatbitlbl |label=0x12 |value=Damage the target, then add acid spores around it (Devourer)}}
    {{formatbitlbl |label=0x13 |value=Fatal error (Mind Control)}}
    {{formatbitlbl |label=0x14 |value=Fatal error (Feedback)}}
    {{formatbitlbl |label=0x15 |value=Optical Flare}}
    {{formatbitlbl |label=0x16 |value=Maelstrom}}
    {{formatbitlbl |label=0x17 |value=Fatal error}}
    {{formatbitlbl |label=0x18 |value=Air splash: as described under Splash Radius}}
  {{end-bittable}} }}
{{end-formattable}}

## Splash Radius: Inner
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0B2C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=For a splash (Damage Type 2, 3 or 5), the distance in pixels from the bullet to the edge of a unit within which it takes full damage. Beyond the inner radius, units take half damage within the middle radius and a quarter within the outer radius, and burrowed units are only hit within the inner radius. For the air splash (Damage Type 24): the target takes full damage if it is within the inner radius, otherwise one random enemy within the outer radius does; then every other unit takes half within the middle radius or a quarter within the outer one. Subterranean Spines (weapon 109) hit only within the inner radius, each unit once per attack. Every unit hurt must pass the Target Flags.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Splash Radius: Middle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0C30}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=For a splash, the distance in pixels within which a unit takes half damage (see Splash Radius: Inner).}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Splash Radius: Outer
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0D34}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=For a splash, the distance in pixels within which a unit takes a quarter of the damage (see Splash Radius: Inner). The Infested Terran also walks up to this distance of weapon 54 before exploding.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Damage
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0E38}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Damage of one hit, in hit points, before upgrades, armor and size. Some spells read it through fixed weapon numbers: Irradiate (weapon 34) spreads its damage over its cooldown, and Plague (weapon 60) deals it over 76 ticks, skipping any tick that would kill. The status panel shows it multiplied by Damage Factor. A map's unit settings can replace it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Bonus
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0F3C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Damage added for each level of the Damage Upgrade. A map's unit settings can replace it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cooldown
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1040}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Frames between attacks. The game adds to it for acid spores on the unit (max(3, cooldown ÷ 8) for each), then multiplies by 1.25 if the unit is slowed (Ensnare) or by 0.5 if it is sped up (Stim Packs or Adrenal Glands), keeps the result between 5 and 250, and adds a random −1 to +2. Irradiate's cooldown (weapon 34) is also how long Irradiate lasts. A cooldown of 0 on a weapon that any unit type with hit points or shields has as its ground or air weapon (or that of its turret) stops the game with a division by zero whenever a game starts: the game then builds the computer AI's table of unit strengths, dividing by the cooldown of each of those weapons.}}
  {{formatlbl |label=Values |value=Integer value between 1 and 255. Values below 5 act like 5 and above 250 like 250, apart from the random change.}}
{{end-formattable}}

## Damage Factor
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x10C2}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=With 2, every attack fires a second bullet right after the first (Hellfire and Anti-matter Missiles, Halo Rockets); any other value fires one. The status panel multiplies Damage and Bonus by it, except that it always uses 2 for the Firebat, the Zealot and their heroes and 1 for the Valkyrie. StarEdit multiplies it by units.dat's Max Hits to show the damage.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Attack Angle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1144}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=How far, in 256ths of a full turn, the unit may face away from its target and still fire. 128 or more means any direction; 0 means it must face the target exactly. The Lurker ignores it. Workers also use their ground weapon's value to decide whether they face a building to repair or build it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Launch Spin
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x11C6}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Turns the bullet's starting direction by this many 256ths of a turn, to the left and right in turn for successive bullets from the same unit, which makes homing missiles curve. 0 means straight.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Forward Offset
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1248}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=How many pixels in front of the unit the bullet starts. The animation script command attkshiftproj changes it for the weapon while a game runs (the Lurker uses it); the file is reloaded for the next game.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Upward Offset
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x12CA}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=How many pixels above the unit the bullet starts.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Error Message
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x134C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Message shown when a unit is ordered to use the weapon on a target it cannot hit: a string number in rez\stat_txt.tbl, counting from 1 (879 is "Unable to attack target."). Targets in stasis or that cannot be hit get fixed messages instead.}}
  {{formatlbl |label=Values |value=Integer value between 1 and the number of strings in rez\stat_txt.tbl.}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1450}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Frame of unit\cmdbtns\cmdicons.grp shown for the weapon in a selected unit's status panel.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last frame of cmdicons.grp.}}
{{end-formattable}}

---

## Appendix: Weapons list
{{begin-formattable}}
  {{formatlbl |label=Description |value=The weapon list. Every field of the file has one entry for each of these, in this order. Weapon 130 means "no weapon" in units.dat and has no entry here.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Gauss Rifle (Normal)}}
    {{formatbitlbl |label=0x01 |value=Gauss Rifle (Jim Raynor-Marine)}}
    {{formatbitlbl |label=0x02 |value=C-10 Concussion Rifle (Normal)}}
    {{formatbitlbl |label=0x03 |value=C-10 Concussion Rifle (Sarah Kerrigan)}}
    {{formatbitlbl |label=0x04 |value=Fragmentation Grenade (Normal)}}
    {{formatbitlbl |label=0x05 |value=Fragmentation Grenade (Jim Raynor-Vulture)}}
    {{formatbitlbl |label=0x06 |value=Spider Mines}}
    {{formatbitlbl |label=0x07 |value=Twin Autocannons (Normal)}}
    {{formatbitlbl |label=0x08 |value=Hellfire Missile Pack (Normal)}}
    {{formatbitlbl |label=0x09 |value=Twin Autocannons (Alan Schezar)}}
    {{formatbitlbl |label=0x0A |value=Hellfire Missile Pack (Alan Schezar)}}
    {{formatbitlbl |label=0x0B |value=Arclite Cannon (Normal)}}
    {{formatbitlbl |label=0x0C |value=Arclite Cannon (Edmund Duke)}}
    {{formatbitlbl |label=0x0D |value=Fusion Cutter}}
    {{formatbitlbl |label=0x0E |value=Fusion Cutter (Harvest)}}
    {{formatbitlbl |label=0x0F |value=Gemini Missiles (Normal)}}
    {{formatbitlbl |label=0x10 |value=Burst Lasers (Normal)}}
    {{formatbitlbl |label=0x11 |value=Gemini Missiles (Tom Kazansky)}}
    {{formatbitlbl |label=0x12 |value=Burst Lasers (Tom Kazansky)}}
    {{formatbitlbl |label=0x13 |value=ATS Laser Battery (Normal)}}
    {{formatbitlbl |label=0x14 |value=ATA Laser Battery (Normal)}}
    {{formatbitlbl |label=0x15 |value=ATS Laser Battery (Norad II+Mengsk+DuGalle)}}
    {{formatbitlbl |label=0x16 |value=ATA Laser Battery (Norad II+Mengsk+DuGalle)}}
    {{formatbitlbl |label=0x17 |value=ATS Laser Battery (Hyperion)}}
    {{formatbitlbl |label=0x18 |value=ATA Laser Battery (Hyperion)}}
    {{formatbitlbl |label=0x19 |value=Flame Thrower (Normal)}}
    {{formatbitlbl |label=0x1A |value=Flame Thrower (Gui Montag)}}
    {{formatbitlbl |label=0x1B |value=Arclite Shock Cannon (Normal)}}
    {{formatbitlbl |label=0x1C |value=Arclite Shock Cannon (Edmund Duke)}}
    {{formatbitlbl |label=0x1D |value=Longbolt Missiles}}
    {{formatbitlbl |label=0x1E |value=Yamato Gun}}
    {{formatbitlbl |label=0x1F |value=Nuclear Missile}}
    {{formatbitlbl |label=0x20 |value=Lockdown}}
    {{formatbitlbl |label=0x21 |value=EMP Shockwave}}
    {{formatbitlbl |label=0x22 |value=Irradiate}}
    {{formatbitlbl |label=0x23 |value=Claws (Normal)}}
    {{formatbitlbl |label=0x24 |value=Claws (Devouring One)}}
    {{formatbitlbl |label=0x25 |value=Claws (Infested Kerrigan)}}
    {{formatbitlbl |label=0x26 |value=Needle Spines (Normal)}}
    {{formatbitlbl |label=0x27 |value=Needle Spines (Hunter Killer)}}
    {{formatbitlbl |label=0x28 |value=Kaiser Blades (Normal)}}
    {{formatbitlbl |label=0x29 |value=Kaiser Blades (Torrasque)}}
    {{formatbitlbl |label=0x2A |value=Toxic Spores (Broodling)}}
    {{formatbitlbl |label=0x2B |value=Spines}}
    {{formatbitlbl |label=0x2C |value=Spines (Harvest)}}
    {{formatbitlbl |label=0x2D |value=Acid Spray (Unused)}}
    {{formatbitlbl |label=0x2E |value=Acid Spore (Normal)}}
    {{formatbitlbl |label=0x2F |value=Acid Spore (Kukulza-Guardian)}}
    {{formatbitlbl |label=0x30 |value=Glave Wurm (Normal)}}
    {{formatbitlbl |label=0x31 |value=Glave Wurm (Kukulza-Mutalisk)}}
    {{formatbitlbl |label=0x32 |value=Venom (Unused-Defiler)}}
    {{formatbitlbl |label=0x33 |value=Venom (Unused-Defiler Hero)}}
    {{formatbitlbl |label=0x34 |value=Seeker Spores}}
    {{formatbitlbl |label=0x35 |value=Subterranean Tentacle}}
    {{formatbitlbl |label=0x36 |value=Suicide (Infested Terran)}}
    {{formatbitlbl |label=0x37 |value=Suicide (Scourge)}}
    {{formatbitlbl |label=0x38 |value=Parasite}}
    {{formatbitlbl |label=0x39 |value=Spawn Broodlings}}
    {{formatbitlbl |label=0x3A |value=Ensnare}}
    {{formatbitlbl |label=0x3B |value=Dark Swarm}}
    {{formatbitlbl |label=0x3C |value=Plague}}
    {{formatbitlbl |label=0x3D |value=Consume}}
    {{formatbitlbl |label=0x3E |value=Particle Beam}}
    {{formatbitlbl |label=0x3F |value=Particle Beam (Harvest)}}
    {{formatbitlbl |label=0x40 |value=Psi Blades (Normal)}}
    {{formatbitlbl |label=0x41 |value=Psi Blades (Fenix-Zealot)}}
    {{formatbitlbl |label=0x42 |value=Phase Disruptor (Normal)}}
    {{formatbitlbl |label=0x43 |value=Phase Disruptor (Fenix-Dragoon)}}
    {{formatbitlbl |label=0x44 |value=Psi Assault (Normal-Unused)}}
    {{formatbitlbl |label=0x45 |value=Psi Assault (Tassadar+Aldaris)}}
    {{formatbitlbl |label=0x46 |value=Psionic Shockwave (Normal)}}
    {{formatbitlbl |label=0x47 |value=Psionic Shockwave (Tassadar/Zeratul Archon)}}
    {{formatbitlbl |label=0x48 |value=Unknown72}}
    {{formatbitlbl |label=0x49 |value=Dual Photon Blasters (Normal)}}
    {{formatbitlbl |label=0x4A |value=Anti-matter Missiles (Normal)}}
    {{formatbitlbl |label=0x4B |value=Dual Photon Blasters (Mojo)}}
    {{formatbitlbl |label=0x4C |value=Anti-matter Missiles (Mojo)}}
    {{formatbitlbl |label=0x4D |value=Phase Disruptor Cannon (Normal)}}
    {{formatbitlbl |label=0x4E |value=Phase Disruptor Cannon (Danimoth)}}
    {{formatbitlbl |label=0x4F |value=Pulse Cannon}}
    {{formatbitlbl |label=0x50 |value=STS Photon Cannon}}
    {{formatbitlbl |label=0x51 |value=STA Photon Cannon}}
    {{formatbitlbl |label=0x52 |value=Scarab}}
    {{formatbitlbl |label=0x53 |value=Stasis Field}}
    {{formatbitlbl |label=0x54 |value=Psi Storm}}
    {{formatbitlbl |label=0x55 |value=Warp Blades (Zeratul)}}
    {{formatbitlbl |label=0x56 |value=Warp Blades (Dark Templar Hero)}}
    {{formatbitlbl |label=0x57 |value=Missiles (Unused)}}
    {{formatbitlbl |label=0x58 |value=Laser Battery1 (Unused)}}
    {{formatbitlbl |label=0x59 |value=Tormentor Missiles (Unused)}}
    {{formatbitlbl |label=0x5A |value=Bombs (Unused)}}
    {{formatbitlbl |label=0x5B |value=Raider Gun (Unused)}}
    {{formatbitlbl |label=0x5C |value=Laser Battery2 (Unused)}}
    {{formatbitlbl |label=0x5D |value=Laser Battery3 (Unused)}}
    {{formatbitlbl |label=0x5E |value=Dual Photon Blasters (Unused)}}
    {{formatbitlbl |label=0x5F |value=Flechette Grenade (Unused)}}
    {{formatbitlbl |label=0x60 |value=Twin Autocannons (Floor Trap)}}
    {{formatbitlbl |label=0x61 |value=Hellfire Missile Pack (Wall Trap)}}
    {{formatbitlbl |label=0x62 |value=Flame Thrower (Wall Trap)}}
    {{formatbitlbl |label=0x63 |value=Hellfire Missile Pack (Floor Trap)}}
    {{formatbitlbl |label=0x64 |value=Neutron Flare}}
    {{formatbitlbl |label=0x65 |value=Disruption Web}}
    {{formatbitlbl |label=0x66 |value=Restoration}}
    {{formatbitlbl |label=0x67 |value=Halo Rockets}}
    {{formatbitlbl |label=0x68 |value=Corrosive Acid}}
    {{formatbitlbl |label=0x69 |value=Mind Control}}
    {{formatbitlbl |label=0x6A |value=Feedback}}
    {{formatbitlbl |label=0x6B |value=Optical Flare}}
    {{formatbitlbl |label=0x6C |value=Maelstrom}}
    {{formatbitlbl |label=0x6D |value=Subterranean Spines}}
    {{formatbitlbl |label=0x6E |value=Gauss Rifle0 (Unused)}}
    {{formatbitlbl |label=0x6F |value=Warp Blades (Normal)}}
    {{formatbitlbl |label=0x70 |value=C-10 Concussion Rifle (Samir Duran)}}
    {{formatbitlbl |label=0x71 |value=C-10 Concussion Rifle (Infested Duran)}}
    {{formatbitlbl |label=0x72 |value=Dual Photon Blasters (Artanis)}}
    {{formatbitlbl |label=0x73 |value=Anti-matter Missiles (Artanis)}}
    {{formatbitlbl |label=0x74 |value=C-10 Concussion Rifle (Alexei Stukov)}}
    {{formatbitlbl |label=0x75 |value=Unknown117}}
    {{formatbitlbl |label=0x76 |value=Unknown118}}
    {{formatbitlbl |label=0x77 |value=Unknown119}}
    {{formatbitlbl |label=0x78 |value=Unknown120}}
    {{formatbitlbl |label=0x79 |value=Unknown121}}
    {{formatbitlbl |label=0x7A |value=Unknown122}}
    {{formatbitlbl |label=0x7B |value=Unknown123}}
    {{formatbitlbl |label=0x7C |value=Unknown124}}
    {{formatbitlbl |label=0x7D |value=Unknown125}}
    {{formatbitlbl |label=0x7E |value=Unknown126}}
    {{formatbitlbl |label=0x7F |value=Unknown127}}
    {{formatbitlbl |label=0x80 |value=Unknown128}}
    {{formatbitlbl |label=0x81 |value=Unknown129}}
  {{end-bittable}} }}
{{end-formattable}}

