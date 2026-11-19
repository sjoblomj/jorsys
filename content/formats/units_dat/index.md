# units.dat Format

units.dat holds the data for every unit type: units, buildings, turrets, spell effects, resources, critters, doodads and other map objects (see Appendix: Units list). It gives each type's graphics, hit points, shields, armor, weapons, orders, flags, sounds, sizes, costs, supply, transport space, score and editor settings. It is the file arr\units.dat in the game's MPQ archives and is 19876 bytes long. Each field below is a list with one entry per unit type, and the lists are stored one after another with nothing in between, so the offsets are from the start of the file. Most fields have 228 entries, one for each type (0x00 to 0xE3). The fields marked "First 106 Units" only have entries for types 0 to 105, the units; Infestation and Add-on Position only have entries for types 106 to 201, the buildings. The layout is the same in every version from 1.04 to 1.17, of both StarCraft and Brood War, and StarEdit reads the file in the same layout. StarCraft 1.00 to 1.03 used an older layout (19192 bytes). That older file is still in StarDat.mpq in later versions, but it is never loaded: the newer copy in patch_rt.mpq (or, in 1.05 to 1.07, BrooDat.mpq) is found first. The patch_rt.mpq copy is the same in 1.08 to 1.17. The game loads the file again each time a game starts, and for mission briefings. Fields are read in order, and the game stops with a file error if the file is longer than the layout. A shorter file that ends exactly where a field ends loads without an error; the fields after the end then keep whatever they held before. None of the fields that point into another table (flingy.dat, images.dat, weapons.dat, orders.dat and so on) is checked when the game uses it, so an out-of-range value reads whatever follows that table in memory.

A map can replace some fields. Its unit settings (the CHK section UNIS in StarCraft maps and UNIx in Brood War maps) hold hit points, shields, armor, build time, mineral and gas cost and a name for each unit, and for every unit whose "use default settings" flag is clear these replace Hit Points, Shield Amount, Armor, Build Time, Cost: Minerals, Cost: Vespene Gas and Unit Name for that game (the same section also replaces the damage of the unit's weapons in weapons.dat). Saved games store those fields as well.

## Graphics
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The unit's flingy.dat entry, which gives its sprite and therefore its images, and its top speed, acceleration and turning. The game reads speed and turning through it while the unit moves.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last entry of flingy.dat.}}
{{end-formattable}}

## Subunit 1
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x00E4}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=The turret attached to this unit, a unit type (for example the Goliath Turret on the Goliath). 228 means none. The game only creates subunits for types 0 to 105, and if it cannot create the subunit, the unit dies. A unit with a subunit uses the subunit's weapons when it has none of its own (130), and the subunit's Target Acquisition Range.}}
  {{formatlbl |label=Values |value=A unit type, or 228 for none.}}
{{end-formattable}}

## Subunit 2
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02AC}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Not used: no code in StarCraft or StarEdit reads this field (checked in 1.05, 1.15.0 and 1.17). It is 228 for every unit in the shipped file.}}
  {{formatlbl |label=Values |value=Any value; ignored.}}
{{end-formattable}}

## Infestation
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0474}}
  {{formatlbl |label=Length |value=192 bytes (2 bytes / Units 106 to 201)}}
  {{formatlbl |label=Description |value=For buildings only: the unit type the building becomes when a Queen infests it. The first entry is for type 106 (the Command Center), the second for 107 and so on. The game only lets a Queen infest a Command Center, so only the first entry matters; it is 130, the Infested Command Center. The hit points become the new type's, and its button set is used.}}
  {{formatlbl |label=Values |value=A unit type.}}
{{end-formattable}}

## Construction Graphic
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0534}}
  {{formatlbl |label=Length |value=912 bytes (4 bytes / Unit)}}
  {{formatlbl |label=Description |value=An images.dat entry shown on the unit while it is being built, or while a Zerg unit morphs in its egg. 0 means the unit's own image is shown while it is being built.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last entry of images.dat.}}
{{end-formattable}}

## Unit Direction
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x08C4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The direction a unit (with flag Can Turn) faces when it is completed, in 32 steps from 0 (up) clockwise. 32 means a random direction. Siege Tanks and their turrets also turn to this direction when they change mode.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 32.}}
{{end-formattable}}

## Shield Enable
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x09A8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Whether the unit has shields. Without this, Shield Amount is ignored: shields do not absorb damage, regenerate or show.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=No shields}}
    {{formatbitlbl |label=0x01 and up |value=Shields}}
  {{end-bittable}} }}
{{end-formattable}}

## Shield Amount
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0A8C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Maximum shields, in whole points. Shields regenerate 7/256 of a point each update and absorb damage before hit points (see weapons.dat). A building under construction starts with a tenth of its shields. The status panel hides the numbers when this is above 9999. A map's unit settings can replace it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Hit Points
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0C54}}
  {{formatlbl |label=Length |value=912 bytes (4 bytes / Unit)}}
  {{formatlbl |label=Description |value=Maximum hit points, in 1/256 points: 256 is one hit point, and the lowest byte is the fraction. The status panel shows the value divided by 256 (and hides the numbers above 9999). A unit being built starts at a tenth of it. A map's unit settings can replace it (in the same 1/256 units).}}
  {{formatlbl |label=Values |value=Integer value between 1 and 2147483647 (the game treats it as signed). The shipped values go up to 25600000 (100000 hit points).}}
{{end-formattable}}

## Elevation Level
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0FE4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Sets the order in which sprites are drawn (higher in front) and whether the unit is a ground or an air unit for movement: below 12 it moves and collides like a ground unit, from 12 up like an air unit. At 4 and below, sprites are also drawn in order of their position from top to bottom. Some orders change it for a while and restore it afterwards (building, landing, burrowing).}}
  {{formatlbl |label=Values |value=Integer value between 0 and 31 (higher values wrap round in the drawing order). Shipped: 0 to 4 on the ground (4 for most units and buildings), 16 to 19 in the air.}}
{{end-formattable}}

## Movement Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x10C8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The game only tests for the value 0xC1: Spider Mines never go after units with it, and a unit with it hatches 7 pixels higher from an egg. StarEdit uses bit 0x01: a unit with it must be placed where every tile under it can be walked on.}}
  {{formatlbl |label=Values |value=Shipped: 0x00 (buildings and other fixed objects), 0x40 (Larva, Egg, Sunken Colony), 0x41 (most ground units), 0xC1 (Vulture, SCV, Drone, Probe, Spider Mine, Archons), 0xC5 (air units).}}
{{end-formattable}}

## Rank/Subtitle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x11AC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=For Terran units, the rank shown under the name in the status panel: the value (plus the unit's promotions) picks one of the rank strings. For all units it decides which unit of a selection the status panel shows (the highest). StarEdit does not use it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Order: Computer Idle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1290}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The first order of a unit that belongs to a computer player, when it is completed or given to that player.}}
  {{formatlbl |label=Values |value=An entry of orders.dat. Not checked.}}
{{end-formattable}}

## Order: Human Idle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1374}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The first order of a unit that belongs to any other player (not neutral or rescuable), when it is completed or given to that player. Powerups always start with it.}}
  {{formatlbl |label=Values |value=An entry of orders.dat. Not checked.}}
{{end-formattable}}

## Order: Return to Idle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1458}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The order a unit goes back to when an order ends and nothing else is queued (in a Bunker, the Bunker guard order instead). Turrets of the unit get the turret type's order.}}
  {{formatlbl |label=Values |value=An entry of orders.dat. Not checked.}}
{{end-formattable}}

## Order: Attack Unit
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x153C}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The order a unit uses to attack a unit, on the ground or in the air: when told to attack a unit, when right-clicking an enemy, and when it picks a target by itself. 23 (Nothing) means the unit cannot attack.}}
  {{formatlbl |label=Values |value=An entry of orders.dat. Not checked.}}
{{end-formattable}}

## Order: Attack Location
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1620}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The order a unit uses when told to attack a place on the ground rather than a unit. 23 (Nothing) means it cannot.}}
  {{formatlbl |label=Values |value=An entry of orders.dat. Not checked.}}
{{end-formattable}}

## Ground Weapon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1704}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The weapon (weapons.dat) used against units on the ground. 130 means none; the unit then uses its subunit's ground weapon, if it has a subunit. The Lurker only has its ground weapon while burrowed.}}
  {{formatlbl |label=Values |value=A weapon, or 130 for none.}}
{{end-formattable}}

## Max Hits: Ground
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x17E8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Only used by StarEdit, which shows the ground weapon's damage times this value times the weapon's Damage Factor (using the subunit's values if the unit has a subunit). The game never reads it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Air Weapon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x18CC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The weapon (weapons.dat) used against flying units. 130 means none; the unit then uses its subunit's air weapon, if it has a subunit.}}
  {{formatlbl |label=Values |value=A weapon, or 130 for none.}}
{{end-formattable}}

## Max Hits: Air
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x19B0}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Only used by StarEdit, like Max Hits: Ground, for the air weapon. The game never reads it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## AI Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1A94}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Flags for the computer AI. Shipped values are 0 for ordinary combat units and 3 for workers, heroes, buildings, Overlords, Larva, turrets, critters and other special units.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x01 |value=The AI leaves the unit out of the groups it attacks and harasses with}}
    {{formatbitlbl |label=0x02 |value=A unit that comes under a computer player's control joins its town, instead of guarding the place where it is}}
    {{formatbitlbl |label=0x04 to 0x80 |value=Not used}}
  {{end-bittable}} }}
{{end-formattable}}

## Special Ability Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1B78}}
  {{formatlbl |label=Length |value=912 bytes (4 bytes / Unit)}}
  {{formatlbl |label=Description |value=Flags that give the unit type its basic properties. Add the values together. The names here describe what the game does with each flag; several common older names (Animated Idle, Contains Gas, Morph from Other Unit, Large/Huge Unit, Auto Attack and Move, Attack, Produces Units) do not match what the flags do.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00000001 |value=Building: the unit is a building. It is created on the ground (grounded structure), cannot be selected with other units, uses building placement and queues, and cannot be hit by weapons with target flag 0x10.}}
    {{formatbitlbl |label=0x00000002 |value=Add-on: placed and attached as a Terran add-on.}}
    {{formatbitlbl |label=0x00000004 |value=Flyer: the unit is created in the air. Only read when the unit is created, so changing it does not affect existing units.}}
    {{formatbitlbl |label=0x00000008 |value=Worker: can harvest, carry resources, powerups and flags, and gets the worker command card in a mixed selection.}}
    {{formatbitlbl |label=0x00000010 |value=Subunit: a turret on another unit (see Subunit 1); it shares the parent's position, range and orders.}}
    {{formatbitlbl |label=0x00000020 |value=Flying Building: the building can lift off. A damaged Terran unit with this flag burns like a building.}}
    {{formatbitlbl |label=0x00000040 |value=Hero: 250 maximum energy, full Carrier and Reaver hangars without the upgrades, +2 armor for the Ultralisk without Chitinous Plating, hero wireframe colours; the computer does not target heroes with some spells.}}
    {{formatbitlbl |label=0x00000080 |value=Regenerates HP: a completed unit gains 4/256 of a hit point each update (any race).}}
    {{formatbitlbl |label=0x00000100 |value=Click on any image: the unit can be clicked on any clickable image of its sprite, not only its main image (Science Vessel, Archons, Missile Turret). Nothing to do with idle animations.}}
    {{formatbitlbl |label=0x00000200 |value=Cloakable: only used for the cloak command card when every selected unit has it, by the computer AI to decloak its units, and by StarEdit to allow the Cloaked property. Whether a unit can cloak is decided by its buttons, not by this flag.}}
    {{formatbitlbl |label=0x00000400 |value=Two units in one egg: the unit costs twice its supply and two units hatch from the egg (Zergling, Scourge). Minerals and gas are paid once.}}
    {{formatbitlbl |label=0x00000800 |value=Powerup: an item a worker can carry. Excluded from group selection, collision, attacks, cloaking and giving to another player.}}
    {{formatbitlbl |label=0x00001000 |value=Resource Depot: workers return resources here.}}
    {{formatbitlbl |label=0x00002000 |value=Resource Container: holds minerals or gas (mineral fields too, not only gas). Gives the unit a resource amount.}}
    {{formatbitlbl |label=0x00004000 |value=Robotic: weapons with target flag 0x20 cannot hit it.}}
    {{formatbitlbl |label=0x00008000 |value=Detector: detects cloaked and burrowed units while completed and not disabled, locked down, in stasis, in a Maelstrom or blinded.}}
    {{formatbitlbl |label=0x00010000 |value=Organic: for weapon target flags 0x08 and 0x80, Medic healing, Maelstrom and Irradiate.}}
    {{formatbitlbl |label=0x00020000 |value=Requires Creep: the building can only be placed on creep, and creep is filled in under it when it is created.}}
    {{formatbitlbl |label=0x00040000 |value=Unused: no code tests it.}}
    {{formatbitlbl |label=0x00080000 |value=Requires Psi: the building must be placed in a Pylon's power field and is unpowered outside it.}}
    {{formatbitlbl |label=0x00100000 |value=Burrowable: can burrow (with Burrowing).}}
    {{formatbitlbl |label=0x00200000 |value=Has Energy: the unit has energy, regenerates it and shows an energy bar.}}
    {{formatbitlbl |label=0x00400000 |value=Permanent Cloak: the unit cloaks when it is completed or warped in.}}
    {{formatbitlbl |label=0x00800000 |value=Unused: no code tests it (set on the pickups 216 to 227).}}
    {{formatbitlbl |label=0x01000000 |value=No Supply Check: the unit is made without checking supply (morphed units such as the Guardian, and Zerg buildings).}}
    {{formatbitlbl |label=0x02000000 |value=Medium Overlay: spell overlays (Irradiate, Defensive Matrix, Lockdown, Ensnare, Plague and others) are drawn medium-sized. Not the size used for damage (see Size).}}
    {{formatbitlbl |label=0x04000000 |value=Large Overlay: spell overlays are drawn large. If both overlay flags are set, Medium wins; with neither, they are small.}}
    {{formatbitlbl |label=0x08000000 |value=Can Move: the unit can move (it is not a stationary object for pathing).}}
    {{formatbitlbl |label=0x10000000 |value=Can Turn: the unit can turn: it gets a starting direction (see Unit Direction) and turns to face its target. Turrets and static defences have it without Can Move.}}
    {{formatbitlbl |label=0x20000000 |value=Invincible: the unit cannot be hit or targeted.}}
    {{formatbitlbl |label=0x40000000 |value=Mechanical: for weapon target flags 0x04 and 0x80, and the unit can be repaired.}}
    {{formatbitlbl |label=0x80000000 |value=Larger Creep: a Zerg town hall gets a larger first creep patch when placed. Nothing to do with producing units.}}
  {{end-bittable}} }}
{{end-formattable}}

## Target Acquisition Range
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1F08}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=How far, in tiles of 32 pixels, the unit looks for targets to attack by itself. Used by every unit, not only turrets. When the file is loaded, the game raises it to at least the maximum range of the unit's weapons divided by 32, and a unit with a subunit gets the subunit's value. The range upgrades add to it, units in a Bunker look 2 tiles further, and computer players' units use their sight range if that is larger. Cloaked Ghosts do not look for targets.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Sight Range
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1FEC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=How far the unit sees, in tiles. Buildings under construction see 4 and blinded units 2, and the sight upgrades give 11. The game looks the value up in a table of 12 sight shapes without checking it, so values above 11 read past that table and can crash the game.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 11.}}
{{end-formattable}}

## Armor Upgrade
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x20D0}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The upgrade (upgrades.dat) whose level is added to Armor. Any upgrade works. The status panel shows that upgrade's icon and name for the armor, except for upgrade 60, which hides the armor icon.}}
  {{formatlbl |label=Values |value=An upgrade. Shipped values:}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Terran Infantry Armor}}
    {{formatbitlbl |label=0x01 |value=Terran Vehicle Plating}}
    {{formatbitlbl |label=0x02 |value=Terran Ship Plating}}
    {{formatbitlbl |label=0x03 |value=Zerg Carapace}}
    {{formatbitlbl |label=0x04 |value=Zerg Flyer Carapace}}
    {{formatbitlbl |label=0x05 |value=Protoss Armor}}
    {{formatbitlbl |label=0x06 |value=Protoss Plating}}
    {{formatbitlbl |label=0x3C |value=None}}
  {{end-bittable}} }}
{{end-formattable}}

## Size
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x21B4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The unit's size, which together with the attacking weapon's Damage Class (weapons.dat) sets how much of the damage it takes. Size 0 takes 0% from every weapon, so each hit only deals the minimum of half a hit point (or nothing, if shields took part of it).}}
  {{formatlbl |label=Values |value=Values above 3 are not checked and read the factors from whatever follows the table.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Independent (0% from all weapons)}}
    {{formatbitlbl |label=0x01 |value=Small: Explosive 50%, Concussive 100%}}
    {{formatbitlbl |label=0x02 |value=Medium: Explosive 75%, Concussive 50%}}
    {{formatbitlbl |label=0x03 |value=Large: Explosive 100%, Concussive 25%}}
  {{end-bittable}} }}
{{end-formattable}}

## Armor
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2298}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Armor, in whole points: subtracted from each hit that gets past the shields, together with the Armor Upgrade level. Weapons with Damage Class 4 ignore it. A map's unit settings can replace it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Right-Click Action
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x237C}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=What the unit does when it is selected and you right-click. A burrowed Lurker always acts as 3. From 1.12 on, a building with the value 0 that can set a rally point acts as 2. Units with 0 or 3 also get no Move or Patrol buttons and cannot move by right-clicking.}}
  {{formatlbl |label=Values |value=Values above 6 crash the game when you right-click, because the game uses the value in a table of 7 entries without checking it.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=None}}
    {{formatbitlbl |label=0x01 |value=Attack enemies; otherwise follow the unit or enter an own transport}}
    {{formatbitlbl |label=0x02 |value=Move or follow, never attack; transports pick up units, buildings set their rally point, Queens infest, Medics heal}}
    {{formatbitlbl |label=0x03 |value=Attack enemies only (static defences and sieged tanks)}}
    {{formatbitlbl |label=0x04 |value=Harvest and return resources (Drone, Probe); otherwise as 1}}
    {{formatbitlbl |label=0x05 |value=Harvest, return, repair and finish buildings (SCV); otherwise as 1}}
    {{formatbitlbl |label=0x06 |value=Does nothing, but counts as having a right-click action (Comsat Station)}}
  {{end-bittable}} }}
{{end-formattable}}

## Sound: Ready
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2460}}
  {{formatlbl |label=Length |value=212 bytes (2 bytes / First 106 Units)}}
  {{formatlbl |label=Description |value=The sound (sfxdata.dat) played when your unit is completed, also making its portrait talk. 0 means none. Buildings, Interceptors and Scarabs never play it. Only the first 106 types have an entry; the game does not check this, so a unit of a later type that gets here reads past the field.}}
  {{formatlbl |label=Values |value=An entry of sfxdata.dat, or 0 for none.}}
{{end-formattable}}

## Sound: What Start
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2534}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=First of the sounds (sfxdata.dat) played when you select your unit; one from What Start to What End is picked at random, never the same one twice in a row. 0 and 0 means none. The doors (types 205 to 208) play What Start when they open and What End when they close.}}
  {{formatlbl |label=Values |value=An entry of sfxdata.dat.}}
{{end-formattable}}

## Sound: What End
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x26FC}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Last of the sounds played when you select your unit (see Sound: What Start).}}
  {{formatlbl |label=Values |value=An entry of sfxdata.dat.}}
{{end-formattable}}

## Sound: Annoyed Start
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x28C4}}
  {{formatlbl |label=Length |value=212 bytes (2 bytes / First 106 Units)}}
  {{formatlbl |label=Description |value=First of the sounds played when you keep clicking the same unit: from the fifth click on, the game plays them in order from Annoyed Start to Annoyed End, then starts again with the What sounds. 0 means none. Buildings never play them.}}
  {{formatlbl |label=Values |value=An entry of sfxdata.dat, or 0 for none.}}
{{end-formattable}}

## Sound: Annoyed End
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2998}}
  {{formatlbl |label=Length |value=212 bytes (2 bytes / First 106 Units)}}
  {{formatlbl |label=Description |value=Last of the annoyed sounds (see Sound: Annoyed Start).}}
  {{formatlbl |label=Values |value=An entry of sfxdata.dat.}}
{{end-formattable}}

## Sound: Yes Start
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2A6C}}
  {{formatlbl |label=Length |value=212 bytes (2 bytes / First 106 Units)}}
  {{formatlbl |label=Description |value=First of the sounds played when you give your unit an order; one from Yes Start to Yes End is picked at random. 0 means none.}}
  {{formatlbl |label=Values |value=An entry of sfxdata.dat, or 0 for none.}}
{{end-formattable}}

## Sound: Yes End
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2B40}}
  {{formatlbl |label=Length |value=212 bytes (2 bytes / First 106 Units)}}
  {{formatlbl |label=Description |value=Last of the sounds played when you give your unit an order (see Sound: Yes Start).}}
  {{formatlbl |label=Values |value=An entry of sfxdata.dat.}}
{{end-formattable}}

## Placement Box
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2C14}}
  {{formatlbl |label=Length |value=912 bytes (4 bytes / Unit)}}
  {{formatlbl |label=Description |value=Width, then height, in pixels (2 bytes each), of the box centred on the unit used to place it. For buildings it is divided by 32 to give the tiles the building takes up on the map, which placement, collision and creep use, so buildings use multiples of 32. For other units, a click on several overlapping units picks the one with the smallest box.}}
  {{formatlbl |label=Values |value=Two signed integer values between 0 and 32767.}}
{{end-formattable}}

## Add-on Position
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2FA4}}
  {{formatlbl |label=Length |value=384 bytes (4 bytes / Units 106 to 201)}}
  {{formatlbl |label=Description |value=For add-ons only: where the add-on sits next to its building, as x, then y, in pixels (2 bytes each), from the top left corner of the building's placement box to that of the add-on's. The first entry is for type 106 (Command Center), the second for 107 and so on. All Terran add-ons have (128, 32).}}
  {{formatlbl |label=Values |value=Two signed integer values between −32768 and 32767.}}
{{end-formattable}}

## Unit Dimensions
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3124}}
  {{formatlbl |label=Length |value=1824 bytes (8 bytes / Unit)}}
  {{formatlbl |label=Description |value=The unit's real size: how far it extends left, up, right and down from its position, in pixels (2 bytes each, in that order). The box is left + right + 1 pixels wide and up + down + 1 pixels high. It is used for collision, movement, keeping units inside the map, and weapon ranges, which are measured between the edges of the two units' boxes. The game widens every search for units by the largest box of all types, so one very large box slows all searches down.}}
  {{formatlbl |label=Values |value=Four signed integer values between 0 and 32767.}}
{{end-formattable}}

## Portrait
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3844}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=The portrait (portdata.dat) shown in the status panel. 0xFFFF means none. A few values are replaced in some campaign missions, and the Flag uses its owner's colour.}}
  {{formatlbl |label=Values |value=An entry of portdata.dat, or 0xFFFF for none.}}
{{end-formattable}}

## Cost: Minerals
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3A0C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Minerals needed to train, build or morph into this unit. Paired units (Zergling, Scourge) pay once for the pair. Cancelling a unit in training or an egg gives it all back; cancelling a building under construction or a Zerg building morph gives back 3/4. A map's unit settings can replace it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3BD4}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Vespene gas needed to train, build or morph into this unit, paid and refunded like Cost: Minerals. A map's unit settings can replace it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Build Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3D9C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Time it takes to train or build the unit, in game frames (not seconds). A building under construction gains its hit points and shields over this time, from a tenth up. 0 is treated as 1, but a progress bar for a type with time 0 divides by zero. StarEdit shows the time divided by 15, as seconds. A map's unit settings can replace it.}}
  {{formatlbl |label=Values |value=Integer value between 1 and 65535.}}
{{end-formattable}}

## Requirements
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3F64}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Where this unit's requirements (what is needed to train or build it, and what trains or builds it) start in the game's built-in requirement list (the unit requirements, inside the executable, not in any data file), as a position in that list. 0 means the unit has no requirements entry and is never allowed. The game fills this field in itself: whenever it checks a unit whose entry holds 0xFFFF, it walks the built-in list, stores the position for every unit listed there (replacing what the file had), and sets every entry still 0xFFFF to 0. So a value other than 0xFFFF only survives for units that have no entry in the built-in list, or if the file has no 0xFFFF at all, and it then picks (part of) an existing entry of the list; nothing checks it. The shipped file has 0xFFFF everywhere, so the game always uses its built-in list.}}
  {{formatlbl |label=Values |value=0xFFFF (let the game fill it in).}}
{{end-formattable}}

## Group Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x412C}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The unit's race and the groups it counts in. The game uses the race bits to find the unit's race (and so its supply pool, sounds and status panel graphics) and the Men, Building and Factory bits for the trigger unit groups and the score. StarEdit uses the race bits and Independent to decide which players may own the unit.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x01 |value=Zerg}}
    {{formatbitlbl |label=0x02 |value=Terran}}
    {{formatbitlbl |label=0x04 |value=Protoss}}
    {{formatbitlbl |label=0x08 |value=Men (trigger group and unit score)}}
    {{formatbitlbl |label=0x10 |value=Building (trigger group and structure score)}}
    {{formatbitlbl |label=0x20 |value=Factory (trigger group)}}
    {{formatbitlbl |label=0x40 |value=Independent (only read by StarEdit)}}
    {{formatbitlbl |label=0x80 |value=Neutral: in a game that uses the map's settings, a preplaced unit of a player whose race can be chosen is only created if it has this bit, so the map's resources and critters stay while the players' other units are left out}}
  {{end-bittable}} }}
{{end-formattable}}

## Supply Provided
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4210}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Supply this unit provides for its race, in half units: 16 is 8 supply. Added when the unit is completed and taken away when it is lost; a race can have at most 200 supply.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Supply Required
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x42F4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Supply this unit uses, in half units: 2 is 1 supply, and the Zergling's 1 is half (the pair from one egg uses 2). Not checked for units with flag 0x01000000. The status panel shows (value + 1) / 2.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Transport Space Required
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x43D8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Space the unit takes up in a transport. A Bunker only takes Terran units that need 1. The transport's status panel only shows passengers that need 1, 2 or 4. 255 is used for units that cannot be loaded.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Transport Space Provided
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x44BC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Space this unit has for passengers; any value above 0 makes it a transport (the Overlord also needs Ventral Sacs). Values above 8 are unsafe: a transport can only hold 8 passengers, and larger values make the game read past them.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 8.}}
{{end-formattable}}

## Score: Build
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x45A0}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Points the owner gets when the unit is completed, as unit score (Men) or structure score (Building).}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Score: Destroy
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4768}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Points another player gets for destroying the unit. Hallucinations and subunits give none.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Unit Name
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4930}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=0 means the unit uses its standard name, string type + 1 of rez\stat_txt.tbl. Any other value is a string number in the map's own string table, counting from 1; a map's unit settings set it. The shipped file has 0 for every unit.}}
  {{formatlbl |label=Values |value=0, or a string number in the map.}}
{{end-formattable}}

## Brood War Flag
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4AF8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Only used by StarEdit, which offers the units marked 1 only on Brood War maps and warns about them otherwise. The game itself uses bit 0x0200 of StarEdit Availability Flags instead.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=StarCraft and Brood War}}
    {{formatbitlbl |label=0x01 |value=Brood War only}}
    {{formatbitlbl |label=0x02 and up |value=Never offered by StarEdit}}
  {{end-bittable}} }}
{{end-formattable}}

## StarEdit Availability Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4BDC}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Where StarEdit offers the unit. The game itself reads three of the bits (0x0001, 0x0002 and 0x0200).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0001 |value=Has an owner: StarEdit shows it in the player's colour and gives it the owner property. The game uses it to decide which sprites need the visibility check}}
    {{formatbitlbl |label=0x0002 |value=Can be placed in StarEdit and created by the Create Unit trigger; the game refuses to create other types that way}}
    {{formatbitlbl |label=0x0004 |value=Listed for the portrait in triggers (such as Transmission)}}
    {{formatbitlbl |label=0x0008 |value=Listed in Player Settings (unit availability)}}
    {{formatbitlbl |label=0x0010 |value=Any race may own it; without it, only players of the unit's race}}
    {{formatbitlbl |label=0x0020 |value=Listed for Set Doodad State in triggers}}
    {{formatbitlbl |label=0x0040 |value=Listed as a unit in trigger conditions and actions}}
    {{formatbitlbl |label=0x0080 |value=Listed in Unit Settings}}
    {{formatbitlbl |label=0x0100 |value=Listed as a unit at a location in trigger conditions and actions}}
    {{formatbitlbl |label=0x0200 |value=Brood War: the game does not create preplaced units of this type in a game without the expansion}}
    {{formatbitlbl |label=0x0400 to 0x8000 |value=Not used}}
  {{end-bittable}} }}
{{end-formattable}}

---

## Appendix: Units list
{{begin-formattable}}
  {{formatlbl |label=Description |value=The unit list. Most fields have one entry per type, 228 in all (0x00 to 0xE3). The "First 106 Units" fields cover 0x00 to 0x69, and Infestation and Add-on Position cover 0x6A to 0xC9. Unit type 228 (0xE4) means "no unit", for example in Subunit 1.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Terran Marine}}
    {{formatbitlbl |label=0x01 |value=Terran Ghost}}
    {{formatbitlbl |label=0x02 |value=Terran Vulture}}
    {{formatbitlbl |label=0x03 |value=Terran Goliath}}
    {{formatbitlbl |label=0x04 |value=Goliath Turret}}
    {{formatbitlbl |label=0x05 |value=Terran Siege Tank (Tank Mode)}}
    {{formatbitlbl |label=0x06 |value=Siege Tank Turret (Tank Mode)}}
    {{formatbitlbl |label=0x07 |value=Terran SCV}}
    {{formatbitlbl |label=0x08 |value=Terran Wraith}}
    {{formatbitlbl |label=0x09 |value=Terran Science Vessel}}
    {{formatbitlbl |label=0x0A |value=Gui Montag (Firebat)}}
    {{formatbitlbl |label=0x0B |value=Terran Dropship}}
    {{formatbitlbl |label=0x0C |value=Terran Battlecruiser}}
    {{formatbitlbl |label=0x0D |value=Spider Mine}}
    {{formatbitlbl |label=0x0E |value=Nuclear Missile}}
    {{formatbitlbl |label=0x0F |value=Terran Civilian}}
    {{formatbitlbl |label=0x10 |value=Sarah Kerrigan (Ghost)}}
    {{formatbitlbl |label=0x11 |value=Alan Schezar (Goliath)}}
    {{formatbitlbl |label=0x12 |value=Alan Schezar Turret}}
    {{formatbitlbl |label=0x13 |value=Jim Raynor (Vulture)}}
    {{formatbitlbl |label=0x14 |value=Jim Raynor (Marine)}}
    {{formatbitlbl |label=0x15 |value=Tom Kazansky (Wraith)}}
    {{formatbitlbl |label=0x16 |value=Magellan (Science Vessel)}}
    {{formatbitlbl |label=0x17 |value=Edmund Duke (Tank Mode)}}
    {{formatbitlbl |label=0x18 |value=Edmund Duke Turret (Tank Mode)}}
    {{formatbitlbl |label=0x19 |value=Edmund Duke (Siege Mode)}}
    {{formatbitlbl |label=0x1A |value=Edmund Duke Turret (Siege Mode)}}
    {{formatbitlbl |label=0x1B |value=Arcturus Mengsk (Battlecruiser)}}
    {{formatbitlbl |label=0x1C |value=Hyperion (Battlecruiser)}}
    {{formatbitlbl |label=0x1D |value=Norad II (Battlecruiser)}}
    {{formatbitlbl |label=0x1E |value=Terran Siege Tank (Siege Mode)}}
    {{formatbitlbl |label=0x1F |value=Siege Tank Turret (Siege Mode)}}
    {{formatbitlbl |label=0x20 |value=Terran Firebat}}
    {{formatbitlbl |label=0x21 |value=Scanner Sweep}}
    {{formatbitlbl |label=0x22 |value=Terran Medic}}
    {{formatbitlbl |label=0x23 |value=Zerg Larva}}
    {{formatbitlbl |label=0x24 |value=Zerg Egg}}
    {{formatbitlbl |label=0x25 |value=Zerg Zergling}}
    {{formatbitlbl |label=0x26 |value=Zerg Hydralisk}}
    {{formatbitlbl |label=0x27 |value=Zerg Ultralisk}}
    {{formatbitlbl |label=0x28 |value=Zerg Broodling}}
    {{formatbitlbl |label=0x29 |value=Zerg Drone}}
    {{formatbitlbl |label=0x2A |value=Zerg Overlord}}
    {{formatbitlbl |label=0x2B |value=Zerg Mutalisk}}
    {{formatbitlbl |label=0x2C |value=Zerg Guardian}}
    {{formatbitlbl |label=0x2D |value=Zerg Queen}}
    {{formatbitlbl |label=0x2E |value=Zerg Defiler}}
    {{formatbitlbl |label=0x2F |value=Zerg Scourge}}
    {{formatbitlbl |label=0x30 |value=Torrasque (Ultralisk)}}
    {{formatbitlbl |label=0x31 |value=Matriarch (Queen)}}
    {{formatbitlbl |label=0x32 |value=Infested Terran}}
    {{formatbitlbl |label=0x33 |value=Infested Kerrigan (Infested Terran)}}
    {{formatbitlbl |label=0x34 |value=Unclean One (Defiler)}}
    {{formatbitlbl |label=0x35 |value=Hunter Killer (Hydralisk)}}
    {{formatbitlbl |label=0x36 |value=Devouring One (Zergling)}}
    {{formatbitlbl |label=0x37 |value=Kukulza (Mutalisk)}}
    {{formatbitlbl |label=0x38 |value=Kukulza (Guardian)}}
    {{formatbitlbl |label=0x39 |value=Yggdrasill (Overlord)}}
    {{formatbitlbl |label=0x3A |value=Terran Valkyrie}}
    {{formatbitlbl |label=0x3B |value=Mutalisk Cocoon}}
    {{formatbitlbl |label=0x3C |value=Protoss Corsair}}
    {{formatbitlbl |label=0x3D |value=Protoss Dark Templar (Unit)}}
    {{formatbitlbl |label=0x3E |value=Zerg Devourer}}
    {{formatbitlbl |label=0x3F |value=Protoss Dark Archon}}
    {{formatbitlbl |label=0x40 |value=Protoss Probe}}
    {{formatbitlbl |label=0x41 |value=Protoss Zealot}}
    {{formatbitlbl |label=0x42 |value=Protoss Dragoon}}
    {{formatbitlbl |label=0x43 |value=Protoss High Templar}}
    {{formatbitlbl |label=0x44 |value=Protoss Archon}}
    {{formatbitlbl |label=0x45 |value=Protoss Shuttle}}
    {{formatbitlbl |label=0x46 |value=Protoss Scout}}
    {{formatbitlbl |label=0x47 |value=Protoss Arbiter}}
    {{formatbitlbl |label=0x48 |value=Protoss Carrier}}
    {{formatbitlbl |label=0x49 |value=Protoss Interceptor}}
    {{formatbitlbl |label=0x4A |value=Protoss Dark Templar (Hero)}}
    {{formatbitlbl |label=0x4B |value=Zeratul (Dark Templar)}}
    {{formatbitlbl |label=0x4C |value=Tassadar/Zeratul (Archon)}}
    {{formatbitlbl |label=0x4D |value=Fenix (Zealot)}}
    {{formatbitlbl |label=0x4E |value=Fenix (Dragoon)}}
    {{formatbitlbl |label=0x4F |value=Tassadar (Templar)}}
    {{formatbitlbl |label=0x50 |value=Mojo (Scout)}}
    {{formatbitlbl |label=0x51 |value=Warbringer (Reaver)}}
    {{formatbitlbl |label=0x52 |value=Gantrithor (Carrier)}}
    {{formatbitlbl |label=0x53 |value=Protoss Reaver}}
    {{formatbitlbl |label=0x54 |value=Protoss Observer}}
    {{formatbitlbl |label=0x55 |value=Protoss Scarab}}
    {{formatbitlbl |label=0x56 |value=Danimoth (Arbiter)}}
    {{formatbitlbl |label=0x57 |value=Aldaris (Templar)}}
    {{formatbitlbl |label=0x58 |value=Artanis (Scout)}}
    {{formatbitlbl |label=0x59 |value=Rhynadon (Badlands Critter)}}
    {{formatbitlbl |label=0x5A |value=Bengalaas (Jungle Critter)}}
    {{formatbitlbl |label=0x5B |value=Cargo Ship (Unused)}}
    {{formatbitlbl |label=0x5C |value=Mercenary Gunship (Unused)}}
    {{formatbitlbl |label=0x5D |value=Scantid (Desert Critter)}}
    {{formatbitlbl |label=0x5E |value=Kakaru (Twilight Critter)}}
    {{formatbitlbl |label=0x5F |value=Ragnasaur (Ashworld Critter)}}
    {{formatbitlbl |label=0x60 |value=Ursadon (Ice World Critter)}}
    {{formatbitlbl |label=0x61 |value=Lurker Egg}}
    {{formatbitlbl |label=0x62 |value=Raszagal (Corsair)}}
    {{formatbitlbl |label=0x63 |value=Samir Duran (Ghost)}}
    {{formatbitlbl |label=0x64 |value=Alexei Stukov (Ghost)}}
    {{formatbitlbl |label=0x65 |value=Map Revealer}}
    {{formatbitlbl |label=0x66 |value=Gerard DuGalle (BattleCruiser)}}
    {{formatbitlbl |label=0x67 |value=Zerg Lurker}}
    {{formatbitlbl |label=0x68 |value=Infested Duran (Infested Terran)}}
    {{formatbitlbl |label=0x69 |value=Disruption Web}}
    {{formatbitlbl |label=0x6A |value=Terran Command Center}}
    {{formatbitlbl |label=0x6B |value=Terran Comsat Station}}
    {{formatbitlbl |label=0x6C |value=Terran Nuclear Silo}}
    {{formatbitlbl |label=0x6D |value=Terran Supply Depot}}
    {{formatbitlbl |label=0x6E |value=Terran Refinery}}
    {{formatbitlbl |label=0x6F |value=Terran Barracks}}
    {{formatbitlbl |label=0x70 |value=Terran Academy}}
    {{formatbitlbl |label=0x71 |value=Terran Factory}}
    {{formatbitlbl |label=0x72 |value=Terran Starport}}
    {{formatbitlbl |label=0x73 |value=Terran Control Tower}}
    {{formatbitlbl |label=0x74 |value=Terran Science Facility}}
    {{formatbitlbl |label=0x75 |value=Terran Covert Ops}}
    {{formatbitlbl |label=0x76 |value=Terran Physics Lab}}
    {{formatbitlbl |label=0x77 |value=Starbase (Unused)}}
    {{formatbitlbl |label=0x78 |value=Terran Machine Shop}}
    {{formatbitlbl |label=0x79 |value=Repair Bay (Unused)}}
    {{formatbitlbl |label=0x7A |value=Terran Engineering Bay}}
    {{formatbitlbl |label=0x7B |value=Terran Armory}}
    {{formatbitlbl |label=0x7C |value=Terran Missile Turret}}
    {{formatbitlbl |label=0x7D |value=Terran Bunker}}
    {{formatbitlbl |label=0x7E |value=Norad II (Crashed)}}
    {{formatbitlbl |label=0x7F |value=Ion Cannon}}
    {{formatbitlbl |label=0x80 |value=Uraj Crystal}}
    {{formatbitlbl |label=0x81 |value=Khalis Crystal}}
    {{formatbitlbl |label=0x82 |value=Infested Command Center}}
    {{formatbitlbl |label=0x83 |value=Zerg Hatchery}}
    {{formatbitlbl |label=0x84 |value=Zerg Lair}}
    {{formatbitlbl |label=0x85 |value=Zerg Hive}}
    {{formatbitlbl |label=0x86 |value=Zerg Nydus Canal}}
    {{formatbitlbl |label=0x87 |value=Zerg Hydralisk Den}}
    {{formatbitlbl |label=0x88 |value=Zerg Defiler Mound}}
    {{formatbitlbl |label=0x89 |value=Zerg Greater Spire}}
    {{formatbitlbl |label=0x8A |value=Zerg Queen's Nest}}
    {{formatbitlbl |label=0x8B |value=Zerg Evolution Chamber}}
    {{formatbitlbl |label=0x8C |value=Zerg Ultralisk Cavern}}
    {{formatbitlbl |label=0x8D |value=Zerg Spire}}
    {{formatbitlbl |label=0x8E |value=Zerg Spawning Pool}}
    {{formatbitlbl |label=0x8F |value=Zerg Creep Colony}}
    {{formatbitlbl |label=0x90 |value=Zerg Spore Colony}}
    {{formatbitlbl |label=0x91 |value=Unused Zerg Building1}}
    {{formatbitlbl |label=0x92 |value=Zerg Sunken Colony}}
    {{formatbitlbl |label=0x93 |value=Zerg Overmind (With Shell)}}
    {{formatbitlbl |label=0x94 |value=Zerg Overmind}}
    {{formatbitlbl |label=0x95 |value=Zerg Extractor}}
    {{formatbitlbl |label=0x96 |value=Mature Chrysalis}}
    {{formatbitlbl |label=0x97 |value=Zerg Cerebrate}}
    {{formatbitlbl |label=0x98 |value=Zerg Cerebrate Daggoth}}
    {{formatbitlbl |label=0x99 |value=Unused Zerg Building2}}
    {{formatbitlbl |label=0x9A |value=Protoss Nexus}}
    {{formatbitlbl |label=0x9B |value=Protoss Robotics Facility}}
    {{formatbitlbl |label=0x9C |value=Protoss Pylon}}
    {{formatbitlbl |label=0x9D |value=Protoss Assimilator}}
    {{formatbitlbl |label=0x9E |value=Unused Protoss Building1}}
    {{formatbitlbl |label=0x9F |value=Protoss Observatory}}
    {{formatbitlbl |label=0xA0 |value=Protoss Gateway}}
    {{formatbitlbl |label=0xA1 |value=Unused Protoss Building2}}
    {{formatbitlbl |label=0xA2 |value=Protoss Photon Cannon}}
    {{formatbitlbl |label=0xA3 |value=Protoss Citadel of Adun}}
    {{formatbitlbl |label=0xA4 |value=Protoss Cybernetics Core}}
    {{formatbitlbl |label=0xA5 |value=Protoss Templar Archives}}
    {{formatbitlbl |label=0xA6 |value=Protoss Forge}}
    {{formatbitlbl |label=0xA7 |value=Protoss Stargate}}
    {{formatbitlbl |label=0xA8 |value=Stasis Cell/Prison}}
    {{formatbitlbl |label=0xA9 |value=Protoss Fleet Beacon}}
    {{formatbitlbl |label=0xAA |value=Protoss Arbiter Tribunal}}
    {{formatbitlbl |label=0xAB |value=Protoss Robotics Support Bay}}
    {{formatbitlbl |label=0xAC |value=Protoss Shield Battery}}
    {{formatbitlbl |label=0xAD |value=Khaydarin Crystal Formation}}
    {{formatbitlbl |label=0xAE |value=Protoss Temple}}
    {{formatbitlbl |label=0xAF |value=Xel'Naga Temple}}
    {{formatbitlbl |label=0xB0 |value=Mineral Field (Type 1)}}
    {{formatbitlbl |label=0xB1 |value=Mineral Field (Type 2)}}
    {{formatbitlbl |label=0xB2 |value=Mineral Field (Type 3)}}
    {{formatbitlbl |label=0xB3 |value=Cave (Unused)}}
    {{formatbitlbl |label=0xB4 |value=Cave-in (Unused)}}
    {{formatbitlbl |label=0xB5 |value=Cantina (Unused)}}
    {{formatbitlbl |label=0xB6 |value=Mining Platform (Unused)}}
    {{formatbitlbl |label=0xB7 |value=Independent Command Center (Unused)}}
    {{formatbitlbl |label=0xB8 |value=Independent Starport (Unused)}}
    {{formatbitlbl |label=0xB9 |value=Independent Jump Gate (Unused)}}
    {{formatbitlbl |label=0xBA |value=Ruins (Unused)}}
    {{formatbitlbl |label=0xBB |value=Khaydarin Crystal Formation (Unused)}}
    {{formatbitlbl |label=0xBC |value=Vespene Geyser}}
    {{formatbitlbl |label=0xBD |value=Warp Gate}}
    {{formatbitlbl |label=0xBE |value=Psi Disrupter}}
    {{formatbitlbl |label=0xBF |value=Zerg Marker}}
    {{formatbitlbl |label=0xC0 |value=Terran Marker}}
    {{formatbitlbl |label=0xC1 |value=Protoss Marker}}
    {{formatbitlbl |label=0xC2 |value=Zerg Beacon}}
    {{formatbitlbl |label=0xC3 |value=Terran Beacon}}
    {{formatbitlbl |label=0xC4 |value=Protoss Beacon}}
    {{formatbitlbl |label=0xC5 |value=Zerg Flag Beacon}}
    {{formatbitlbl |label=0xC6 |value=Terran Flag Beacon}}
    {{formatbitlbl |label=0xC7 |value=Protoss Flag Beacon}}
    {{formatbitlbl |label=0xC8 |value=Power Generator}}
    {{formatbitlbl |label=0xC9 |value=Overmind Cocoon}}
    {{formatbitlbl |label=0xCA |value=Dark Swarm}}
    {{formatbitlbl |label=0xCB |value=Floor Missile Trap}}
    {{formatbitlbl |label=0xCC |value=Floor Hatch (Unused)}}
    {{formatbitlbl |label=0xCD |value=Left Upper Level Door}}
    {{formatbitlbl |label=0xCE |value=Right Upper Level Door}}
    {{formatbitlbl |label=0xCF |value=Left Pit Door}}
    {{formatbitlbl |label=0xD0 |value=Right Pit Door}}
    {{formatbitlbl |label=0xD1 |value=Floor Gun Trap}}
    {{formatbitlbl |label=0xD2 |value=Left Wall Missile Trap}}
    {{formatbitlbl |label=0xD3 |value=Left Wall Flame Trap}}
    {{formatbitlbl |label=0xD4 |value=Right Wall Missile Trap}}
    {{formatbitlbl |label=0xD5 |value=Right Wall Flame Trap}}
    {{formatbitlbl |label=0xD6 |value=Start Location}}
    {{formatbitlbl |label=0xD7 |value=Flag}}
    {{formatbitlbl |label=0xD8 |value=Young Chrysalis}}
    {{formatbitlbl |label=0xD9 |value=Psi Emitter}}
    {{formatbitlbl |label=0xDA |value=Data Disc}}
    {{formatbitlbl |label=0xDB |value=Khaydarin Crystal}}
    {{formatbitlbl |label=0xDC |value=Mineral Cluster Type 1}}
    {{formatbitlbl |label=0xDD |value=Mineral Cluster Type 2}}
    {{formatbitlbl |label=0xDE |value=Protoss Vespene Gas Orb Type 1}}
    {{formatbitlbl |label=0xDF |value=Protoss Vespene Gas Orb Type 2}}
    {{formatbitlbl |label=0xE0 |value=Zerg Vespene Gas Sac Type 1}}
    {{formatbitlbl |label=0xE1 |value=Zerg Vespene Gas Sac Type 2}}
    {{formatbitlbl |label=0xE2 |value=Terran Vespene Gas Tank Type 1}}
    {{formatbitlbl |label=0xE3 |value=Terran Vespene Gas Tank Type 2}}
  {{end-bittable}} }}
{{end-formattable}}

