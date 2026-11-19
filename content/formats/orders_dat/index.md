# orders.dat Format

orders.dat holds the data of the orders: the things a unit can be doing, such as moving, attacking, harvesting, casting a spell or building (see Appendix: Orders list). units.dat's order fields, the command buttons and the game's own code start orders by number, and this file gives each order's properties: how it is queued and interrupted, what it targets, the weapon and technology of a spell, the button it highlights and its requirements. It is the file arr\orders.dat in the game's MPQ archives and is 4158 bytes long. Each field below is a list with one entry for each of the 189 orders, and the lists are stored one after another with nothing in between, so the offsets are from the start of the file. StarEdit does not use it. The layout is the same in every version from 1.04 to 1.17, of both StarCraft and Brood War. StarCraft 1.00 to 1.03 used an older layout with 176 orders (3872 bytes); the older file is still in StarDat.mpq in later versions but is never loaded, because the copy in BrooDat.mpq (or patch_rt.mpq) is found first. The game loads the file again each time a game starts, together with units.dat. Fields are read in order, and the game stops with a file error if the file is longer than the layout. A shorter file that ends exactly where a field ends loads without an error; the fields after the end then keep whatever they held before. No field is checked when the game uses it, so an out-of-range value reads whatever follows the table it points into.

Five fields are read by no code in any version from 1.04 to 1.17 (Label and four flags); they are marked Unused below.

## Label
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=378 bytes (2 bytes / Order)}}
  {{formatlbl |label=Description |value=Not used by the game. It holds the order's name as a string number in rez\stat_txt.tbl, counting from 1 (order 0 is string 903, "Die"); seven spell orders point at button strings instead.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in rez\stat_txt.tbl; ignored.}}
{{end-formattable}}

## Attack Order
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x017A}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=Marks an order that attacks its target. For spells and target clicks, the target is checked with the order's Weapon if this is set, and with the technology's target rules otherwise. An attacking unit also drops a target that becomes allied, keeps its current target when choosing targets, and is not counted as idle by the computer AI.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=No}}
    {{formatbitlbl |label=0x01 and up |value=Yes}}
  {{end-bittable}} }}
{{end-formattable}}

## Unused
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0237}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=Not used: no code reads it. Shipped 1 for orders that run while the unit does something else (Train, Build Add-on, Cloak and others).}}
  {{formatlbl |label=Values |value=Any value; ignored.}}
{{end-formattable}}

## Unused
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02F4}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=Not used: no code reads it. Shipped 0 only for the turret orders.}}
  {{formatlbl |label=Values |value=Any value; ignored.}}
{{end-formattable}}

## Pass to Turret
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x03B1}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=When a unit with a turret (subunit) starts this order from its queue, the turret gets the same order and target. The unit's own guard and attack orders (units.dat) are always passed on as the turret's guard and attack orders, whatever this says.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=The turret keeps its order}}
    {{formatbitlbl |label=0x01 and up |value=The turret gets the same order}}
  {{end-bittable}} }}
{{end-formattable}}

## Unused
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x046E}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=Not used: no code reads it.}}
  {{formatlbl |label=Values |value=Any value; ignored.}}
{{end-formattable}}

## Interruptible
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x052B}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=0 makes the order run until it ends by itself: orders given in the meantime wait in the queue, except Die. When a new order is given, interruptible orders at the end of the queue are removed; a non-interruptible one stays and the new order goes after it. Shipped 0 for, among others, Die, Lift Off, Siege Mode, Burrow and the harvesting steps.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Not interruptible}}
    {{formatbitlbl |label=0x01 and up |value=Interruptible}}
  {{end-bittable}} }}
{{end-formattable}}

## Brake Before
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x05E8}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=Read for the next order in a unit's queue each time the unit gets a move target: if that order has 0, the unit does not brake at the end of its move but goes through the point at speed. Shipped 0 for Move, so a chain of queued moves is not slowed at each point. With nothing queued the unit always brakes.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=The unit keeps its speed into this order}}
    {{formatbitlbl |label=0x01 and up |value=The unit brakes before this order}}
  {{end-bittable}} }}
{{end-formattable}}

## Queueable
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x06A5}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=Whether the order can be queued with Shift. A queued order is added after the current one, unless the unit is guarding, doing nothing, picking up, patrolling or acting as a Medic, in which case it replaces it. A unit can have at most 8 queued orders that have an Icon.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Always replaces the current order}}
    {{formatbitlbl |label=0x01 and up |value=Can be queued}}
  {{end-bittable}} }}
{{end-formattable}}

## Keep Target When Disabled
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0762}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=When the unit is hit by Lockdown, Stasis Field or Maelstrom, it forgets the target unit of its order unless this is set. Shipped 1 for building, repairing, entering a Nydus Canal, harvesting and healing.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Forget the target}}
    {{formatbitlbl |label=0x01 and up |value=Keep the target}}
  {{end-bittable}} }}
{{end-formattable}}

## Obstructable
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x081F}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=For a target on the ground, the clicked point is moved to a nearby place where the unit, or the group, fits. 0 keeps the exact point: spells and attacks on the ground use 0.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Exact point}}
    {{formatbitlbl |label=0x01 and up |value=Moved to where the units fit}}
  {{end-bittable}} }}
{{end-formattable}}

## Flee When Attacked
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x08DC}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=A unit doing this order that is attacked by something it cannot fight back (or a worker under attack) moves away from the attacker. Shipped 1 for guarding, patrolling, Carrier and critter orders and a few others.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Stays}}
    {{formatbitlbl |label=0x01 and up |value=Flees}}
  {{end-bittable}} }}
{{end-formattable}}

## Unused
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0999}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=Not used: no code reads it. Shipped 1 for most orders that move the unit.}}
  {{formatlbl |label=Values |value=Any value; ignored.}}
{{end-formattable}}

## Weapon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0A56}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=The weapon (weapons.dat) of a spell or ability: the weapon fired by the animation script command castspell, and the range and cooldown when the spell is cast. 130 means none. With Attack Order set, any value other than 130 is used as a weapon without a check.}}
  {{formatlbl |label=Values |value=A weapon, or 130 for none.}}
{{end-formattable}}

## Technology
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0B13}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=The technology (techdata.dat) of a spell or ability. 44 means none. It sets the energy the order costs, the target rules of spells without Attack Order, and replaces this order's own requirements with the technology's use requirements. A value from 45 to 255 makes the order impossible to give by clicking a target.}}
  {{formatlbl |label=Values |value=A technology, or 44 for none.}}
{{end-formattable}}

## Animation
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0BD0}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=The animation (entry of the unit's animation script) played when the spell is cast. Shipped 7 (CastSpell) for the 19 spell orders and 28 for the rest, which never use it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 27.}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0C8D}}
  {{formatlbl |label=Length |value=378 bytes (2 bytes / Order)}}
  {{formatlbl |label=Description |value=The command button lit up while a unit does this order: the visible button with this icon (frame of cmdicons.grp) is drawn highlighted. 0xFFFF means none, and the turret's order is used instead (also when the value is 229, Stop, and the turret's order has an icon). Only orders with an icon count towards the limit of 8 queued orders.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last frame of cmdicons.grp, or 0xFFFF for none.}}
{{end-formattable}}

## Requirements
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0E07}}
  {{formatlbl |label=Length |value=378 bytes (2 bytes / Order)}}
  {{formatlbl |label=Description |value=Where this order's requirements (what must be true for a unit to be given it) start in the game's built-in requirement list (the order requirements, inside the executable, not in any data file), as a position in that list. 0 means the order has no requirements entry and is never allowed. The game fills this field in itself: whenever it checks a order whose entry holds 0xFFFF, it walks the built-in list, stores the position for every order listed there (replacing what the file had), and sets every entry still 0xFFFF to 0. So a value other than 0xFFFF only survives for orders that have no entry in the built-in list, or if the file has no 0xFFFF at all, and it then picks (part of) an existing entry of the list; nothing checks it. The shipped file has 0xFFFF everywhere, so the game always uses its built-in list. Orders with a Technology use that technology's requirements instead.}}
  {{formatlbl |label=Values |value=0xFFFF (let the game fill it in).}}
{{end-formattable}}

## Obscured Order
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0F81}}
  {{formatlbl |label=Length |value=189 bytes (1 byte / Order)}}
  {{formatlbl |label=Description |value=For the orders a unit gets when it is told to act on a unit hidden by the fog of war (Attack, Repair, Gather and so on, chosen by the button): once the unit gets there and sees the target, it is given this order on it (for Attack, its own attack order from units.dat). 189 means the order cannot target a unit under the fog, so the click counts as a click on the ground. In the shipped file every order holds its own number, except the fog orders, which hold the order they turn into.}}
  {{formatlbl |label=Values |value=An order, or 189 for none.}}
{{end-formattable}}

---

## Appendix: Orders list
{{begin-formattable}}
  {{formatlbl |label=Description |value=Every order, with the name the game's Label field points to (rez\stat_txt.tbl). Some names are misleading: order 6, "Ignore", is the Move order.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Die}}
    {{formatbitlbl |label=0x01 |value=Stop}}
    {{formatbitlbl |label=0x02 |value=Guard}}
    {{formatbitlbl |label=0x03 |value=Player Guard}}
    {{formatbitlbl |label=0x04 |value=Turret Guard}}
    {{formatbitlbl |label=0x05 |value=Bunker Guard}}
    {{formatbitlbl |label=0x06 |value=Ignore}}
    {{formatbitlbl |label=0x07 |value=Reaver Stop}}
    {{formatbitlbl |label=0x08 |value=Attack}}
    {{formatbitlbl |label=0x09 |value=Attack}}
    {{formatbitlbl |label=0x0A |value=Attack Unit}}
    {{formatbitlbl |label=0x0B |value=Attack Fixed Range}}
    {{formatbitlbl |label=0x0C |value=Attack Tile}}
    {{formatbitlbl |label=0x0D |value=Hover}}
    {{formatbitlbl |label=0x0E |value=Attack Move}}
    {{formatbitlbl |label=0x0F |value=Infest Mine}}
    {{formatbitlbl |label=0x10 |value=Nothing}}
    {{formatbitlbl |label=0x11 |value=Powerup}}
    {{formatbitlbl |label=0x12 |value=Tower}}
    {{formatbitlbl |label=0x13 |value=Tower}}
    {{formatbitlbl |label=0x14 |value=Vulture Mine}}
    {{formatbitlbl |label=0x15 |value=Stay In Range}}
    {{formatbitlbl |label=0x16 |value=Turret Attack}}
    {{formatbitlbl |label=0x17 |value=Nothing}}
    {{formatbitlbl |label=0x18 |value=Nothing}}
    {{formatbitlbl |label=0x19 |value=Drone Start Build}}
    {{formatbitlbl |label=0x1A |value=Drone Build}}
    {{formatbitlbl |label=0x1B |value=Infest Mine}}
    {{formatbitlbl |label=0x1C |value=Infest Mine}}
    {{formatbitlbl |label=0x1D |value=Infest Mine}}
    {{formatbitlbl |label=0x1E |value=Build}}
    {{formatbitlbl |label=0x1F |value=Build}}
    {{formatbitlbl |label=0x20 |value=Build}}
    {{formatbitlbl |label=0x21 |value=Build}}
    {{formatbitlbl |label=0x22 |value=Repair}}
    {{formatbitlbl |label=0x23 |value=Repair}}
    {{formatbitlbl |label=0x24 |value=Place Add-On}}
    {{formatbitlbl |label=0x25 |value=Build Add-On}}
    {{formatbitlbl |label=0x26 |value=Train}}
    {{formatbitlbl |label=0x27 |value=Rally Point}}
    {{formatbitlbl |label=0x28 |value=Rally Point}}
    {{formatbitlbl |label=0x29 |value=Zerg Birth}}
    {{formatbitlbl |label=0x2A |value=Morph}}
    {{formatbitlbl |label=0x2B |value=Morph}}
    {{formatbitlbl |label=0x2C |value=Build Self}}
    {{formatbitlbl |label=0x2D |value=Zerg Build Self}}
    {{formatbitlbl |label=0x2E |value=Build}}
    {{formatbitlbl |label=0x2F |value=Enter Nydus Canal}}
    {{formatbitlbl |label=0x30 |value=Build Self}}
    {{formatbitlbl |label=0x31 |value=Follow}}
    {{formatbitlbl |label=0x32 |value=Carrier}}
    {{formatbitlbl |label=0x33 |value=Carrier Ignore}}
    {{formatbitlbl |label=0x34 |value=Carrier Stop}}
    {{formatbitlbl |label=0x35 |value=Carrier Attack}}
    {{formatbitlbl |label=0x36 |value=Carrier Attack}}
    {{formatbitlbl |label=0x37 |value=Carrier Ignore}}
    {{formatbitlbl |label=0x38 |value=Carrier Fight}}
    {{formatbitlbl |label=0x39 |value=Hold Position}}
    {{formatbitlbl |label=0x3A |value=Reaver}}
    {{formatbitlbl |label=0x3B |value=Reaver Attack}}
    {{formatbitlbl |label=0x3C |value=Reaver Attack}}
    {{formatbitlbl |label=0x3D |value=Reaver Fight}}
    {{formatbitlbl |label=0x3E |value=Reaver Hold}}
    {{formatbitlbl |label=0x3F |value=Train Fighter}}
    {{formatbitlbl |label=0x40 |value=Strafe Unit}}
    {{formatbitlbl |label=0x41 |value=Strafe Unit}}
    {{formatbitlbl |label=0x42 |value=Recharge Shields}}
    {{formatbitlbl |label=0x43 |value=Recharge Shields}}
    {{formatbitlbl |label=0x44 |value=Shield Battery}}
    {{formatbitlbl |label=0x45 |value=Return}}
    {{formatbitlbl |label=0x46 |value=Drone Land}}
    {{formatbitlbl |label=0x47 |value=Building Land}}
    {{formatbitlbl |label=0x48 |value=Building Lift Off}}
    {{formatbitlbl |label=0x49 |value=Drone Lift Off}}
    {{formatbitlbl |label=0x4A |value=Lift Off}}
    {{formatbitlbl |label=0x4B |value=Reasearch Tech}}
    {{formatbitlbl |label=0x4C |value=Upgrade}}
    {{formatbitlbl |label=0x4D |value=Larva}}
    {{formatbitlbl |label=0x4E |value=Spawning Larva}}
    {{formatbitlbl |label=0x4F |value=Harvest}}
    {{formatbitlbl |label=0x50 |value=Harvest}}
    {{formatbitlbl |label=0x51 |value=Harvest Gas}}
    {{formatbitlbl |label=0x52 |value=Harvest Gas}}
    {{formatbitlbl |label=0x53 |value=Harvest Gas}}
    {{formatbitlbl |label=0x54 |value=Return Gas}}
    {{formatbitlbl |label=0x55 |value=Harvest Minerals}}
    {{formatbitlbl |label=0x56 |value=Harvest Minerals}}
    {{formatbitlbl |label=0x57 |value=Harvest Minerals}}
    {{formatbitlbl |label=0x58 |value=Harvest}}
    {{formatbitlbl |label=0x59 |value=Harvest}}
    {{formatbitlbl |label=0x5A |value=Return Minerals}}
    {{formatbitlbl |label=0x5B |value=Harvest}}
    {{formatbitlbl |label=0x5C |value=Enter Transport}}
    {{formatbitlbl |label=0x5D |value=Pick Up}}
    {{formatbitlbl |label=0x5E |value=Pick Up}}
    {{formatbitlbl |label=0x5F |value=Pick Up}}
    {{formatbitlbl |label=0x60 |value=Pick Up}}
    {{formatbitlbl |label=0x61 |value=Powerup}}
    {{formatbitlbl |label=0x62 |value=Siege Mode}}
    {{formatbitlbl |label=0x63 |value=Tank Mode}}
    {{formatbitlbl |label=0x64 |value=Watch Target}}
    {{formatbitlbl |label=0x65 |value=Initing Creep Growth}}
    {{formatbitlbl |label=0x66 |value=Spread Creep}}
    {{formatbitlbl |label=0x67 |value=Stopping Creep Growth}}
    {{formatbitlbl |label=0x68 |value=Guardian Aspect}}
    {{formatbitlbl |label=0x69 |value=Warping Archon}}
    {{formatbitlbl |label=0x6A |value=Completing Archon Summon}}
    {{formatbitlbl |label=0x6B |value=Hold Position}}
    {{formatbitlbl |label=0x6C |value=Hold Position}}
    {{formatbitlbl |label=0x6D |value=Cloak}}
    {{formatbitlbl |label=0x6E |value=Decloak}}
    {{formatbitlbl |label=0x6F |value=Unload}}
    {{formatbitlbl |label=0x70 |value=Move Unload}}
    {{formatbitlbl |label=0x71 |value=Fire Yamato Gun}}
    {{formatbitlbl |label=0x72 |value=Fire Yamato Gun}}
    {{formatbitlbl |label=0x73 |value=Magna Pulse}}
    {{formatbitlbl |label=0x74 |value=Burrow}}
    {{formatbitlbl |label=0x75 |value=Burrowed}}
    {{formatbitlbl |label=0x76 |value=Unburrow}}
    {{formatbitlbl |label=0x77 |value=Dark Swarm}}
    {{formatbitlbl |label=0x78 |value=Cast Parasite}}
    {{formatbitlbl |label=0x79 |value=Summon Broodlings}}
    {{formatbitlbl |label=0x7A |value=EMP Shockwave}}
    {{formatbitlbl |label=0x7B |value=Nuke Wait}}
    {{formatbitlbl |label=0x7C |value=Nuke Train}}
    {{formatbitlbl |label=0x7D |value=Nuke Launch}}
    {{formatbitlbl |label=0x7E |value=Nuke Paint}}
    {{formatbitlbl |label=0x7F |value=Nuke Unit}}
    {{formatbitlbl |label=0x80 |value=Nuke Ground}}
    {{formatbitlbl |label=0x81 |value=Nuke Track}}
    {{formatbitlbl |label=0x82 |value=Initializing Arbiter}}
    {{formatbitlbl |label=0x83 |value=Cloaking nearby units}}
    {{formatbitlbl |label=0x84 |value=Place Mine}}
    {{formatbitlbl |label=0x85 |value=Right Click Action}}
    {{formatbitlbl |label=0x86 |value=Sap Unit}}
    {{formatbitlbl |label=0x87 |value=Sap Location}}
    {{formatbitlbl |label=0x88 |value=Hold Position}}
    {{formatbitlbl |label=0x89 |value=Teleport}}
    {{formatbitlbl |label=0x8A |value=Teleport to Location}}
    {{formatbitlbl |label=0x8B |value=Place Scanner}}
    {{formatbitlbl |label=0x8C |value=Scanner}}
    {{formatbitlbl |label=0x8D |value=Defensive Matrix}}
    {{formatbitlbl |label=0x8E |value=Psionic Storm}}
    {{formatbitlbl |label=0x8F |value=Irradiate}}
    {{formatbitlbl |label=0x90 |value=Plague}}
    {{formatbitlbl |label=0x91 |value=Consume}}
    {{formatbitlbl |label=0x92 |value=Ensnare}}
    {{formatbitlbl |label=0x93 |value=Stasis Field}}
    {{formatbitlbl |label=0x94 |value=Hallucination}}
    {{formatbitlbl |label=0x95 |value=Hallucination}}
    {{formatbitlbl |label=0x96 |value=Reset Collision}}
    {{formatbitlbl |label=0x97 |value=Reset Collision}}
    {{formatbitlbl |label=0x98 |value=Patrol}}
    {{formatbitlbl |label=0x99 |value=CTF COP Init}}
    {{formatbitlbl |label=0x9A |value=CTF COP}}
    {{formatbitlbl |label=0x9B |value=CTF COP}}
    {{formatbitlbl |label=0x9C |value=Computer AI}}
    {{formatbitlbl |label=0x9D |value=Atk Move EP}}
    {{formatbitlbl |label=0x9E |value=Harass Move}}
    {{formatbitlbl |label=0x9F |value=AI Patrol}}
    {{formatbitlbl |label=0xA0 |value=Guard Post}}
    {{formatbitlbl |label=0xA1 |value=Rescue Passive}}
    {{formatbitlbl |label=0xA2 |value=Neutral}}
    {{formatbitlbl |label=0xA3 |value=Computer Return}}
    {{formatbitlbl |label=0xA4 |value=Initing Psi Provider}}
    {{formatbitlbl |label=0xA5 |value=Self Destructing}}
    {{formatbitlbl |label=0xA6 |value=Critter}}
    {{formatbitlbl |label=0xA7 |value=Hidden Gun}}
    {{formatbitlbl |label=0xA8 |value=Open Door}}
    {{formatbitlbl |label=0xA9 |value=Close Door}}
    {{formatbitlbl |label=0xAA |value=Hide Trap}}
    {{formatbitlbl |label=0xAB |value=Reveal Trap}}
    {{formatbitlbl |label=0xAC |value=Enable Doodad}}
    {{formatbitlbl |label=0xAD |value=Disable Doodad}}
    {{formatbitlbl |label=0xAE |value=Warp In}}
    {{formatbitlbl |label=0xAF |value=Medic}}
    {{formatbitlbl |label=0xB0 |value=Medic Heal}}
    {{formatbitlbl |label=0xB1 |value=Heal Move}}
    {{formatbitlbl |label=0xB2 |value=Medic Hold Position}}
    {{formatbitlbl |label=0xB3 |value=Medic Heal}}
    {{formatbitlbl |label=0xB4 |value=Restoration}}
    {{formatbitlbl |label=0xB5 |value=Cast Disruption Web}}
    {{formatbitlbl |label=0xB6 |value=Cast Mind Control}}
    {{formatbitlbl |label=0xB7 |value=Warping Dark Archon}}
    {{formatbitlbl |label=0xB8 |value=Cast Feedback}}
    {{formatbitlbl |label=0xB9 |value=Cast Optical Flare}}
    {{formatbitlbl |label=0xBA |value=Cast Shockwave}}
    {{formatbitlbl |label=0xBB |value=Junk Yard Dog}}
    {{formatbitlbl |label=0xBC |value=Fatal}}
  {{end-bittable}} }}
{{end-formattable}}

