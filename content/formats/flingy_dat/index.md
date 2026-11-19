# flingy.dat Format

flingy.dat holds the movement data of everything that moves or can move: units (each unit type's flingy is set by Graphics in units.dat) and bullets (set by Graphics in weapons.dat). Each entry gives the sprite to create and how it accelerates, how fast it may go, when it starts braking and how fast it turns. It is the file arr\flingy.dat in the game's MPQ archives and is 3135 bytes long. Each field below is a list with one entry for each of the 209 flingies, and the lists are stored one after another with nothing in between, so the offsets are from the start of the file. StarEdit also reads the file, for the Sprite field only. The layout is the same in every version from 1.04 to 1.17, of both StarCraft and Brood War. StarCraft 1.00 to 1.03 used an older layout with 184 entries (2760 bytes); the older file is still in StarDat.mpq in later versions but is never loaded, because the copy in BrooDat.mpq (or patch_rt.mpq) is found first. The game loads the file again each time a game starts. Fields are read in order, and the game stops with a file error if the file is longer than the layout. A shorter file that ends exactly where a field ends loads without an error; the fields after the end then keep whatever they held before. No field is checked when the game uses it, so an out-of-range value reads whatever follows the table it points into.

The game copies the movement fields into each unit or bullet when it is created, so changes to these values only affect new ones. Positions are kept in 1/256 pixels, and the movement values use the same scale: a speed of 256 is one pixel per game frame.

patch_rt.mpq has its own copy from 1.08 to 1.17, which differs from the one in BrooDat.mpq in two entries: the Dropship's top speed went from 1133 to 1400, and the Valkyrie's from 1450 to 1690, with its acceleration from 48 to 65. Their Halt Distance was left at the old values.

## Sprite
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=418 bytes (2 bytes / Flingy)}}
  {{formatlbl |label=Description |value=The sprites.dat entry created for this flingy. StarEdit uses it to draw units on the map.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 516.}}
{{end-formattable}}

## Top Speed
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x01A2}}
  {{formatlbl |label=Length |value=836 bytes (4 bytes / Flingy)}}
  {{formatlbl |label=Description |value=Highest speed, in 1/256 pixels per frame (1280 is 5 pixels per frame). For Movement Control 0 and 1, speed upgrades and Stim Packs raise it by half (to at least 853; the Scout gets 1707) and Ensnare halves it. For Movement Control 2 the value is only a starting point: when a unit is created, the game works out its speed from the distances its walking animation moves over 32 frames, so walking units have the placeholder 1 here. 0 means the flingy never moves.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 2147483647.}}
{{end-formattable}}

## Acceleration
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x04E6}}
  {{formatlbl |label=Length |value=418 bytes (2 bytes / Flingy)}}
  {{formatlbl |label=Description |value=How much the speed changes each frame when speeding up or braking, in 1/256 pixels per frame. Doubled with speed upgrades or Stim Packs and reduced to 3/4 by Ensnare. Movement Control 2 does not use it. With Movement Control 0 or 1, 0 means the flingy never gets going.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Halt Distance
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0688}}
  {{formatlbl |label=Length |value=836 bytes (4 bytes / Flingy)}}
  {{formatlbl |label=Description |value=Distance from the target, in 1/256 pixels, at which a flingy with Movement Control 0 starts braking. It is only a stored shortcut for speed² ÷ (2 × acceleration): the game uses it only while the unit moves at exactly Top Speed with exactly Acceleration, and works the distance out itself otherwise. A few shipped values don't match the formula (Science Vessel, Corsair, and the Dropship and Valkyrie since 1.08), so those units brake later than the formula says when at full speed.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 4294967295.}}
{{end-formattable}}

## Turn Rate
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x09CC}}
  {{formatlbl |label=Length |value=209 bytes (1 byte / Flingy)}}
  {{formatlbl |label=Description |value=How far the flingy may turn in one frame, in 256ths of a full turn (40 turns half way round in 4 frames). With Movement Control 0 and 1 the direction of travel follows the facing at half this rate. Speed upgrades and Stim Packs double it and Ensnare reduces it to 3/4. The game compares it as a signed number, so 128 to 255 act as negative values and the flingy never settles on a direction. A moving flingy with Movement Control 0 or 1 and a turn rate of 0 crashes the game (a division by zero) when it comes within 32 pixels of a target it is not facing. Homing bullets of flingies 141 to 171 and 201 to 206 turn one step faster each frame they turn.}}
  {{formatlbl |label=Values |value=Integer value between 1 and 127.}}
{{end-formattable}}

## Unused
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0A9D}}
  {{formatlbl |label=Length |value=209 bytes (1 byte / Flingy)}}
  {{formatlbl |label=Description |value=Not used: no code in StarCraft or StarEdit reads this field, in any version from 1.04 to 1.17. The shipped values (30 for most flyers, 24, 20 and 60 for some, 127 for the rest) look like a banking angle for flyers that was never used.}}
  {{formatlbl |label=Values |value=Any value; ignored.}}
{{end-formattable}}

## Movement Control
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0B6E}}
  {{formatlbl |label=Length |value=209 bytes (1 byte / Flingy)}}
  {{formatlbl |label=Description |value=How the flingy's speed is controlled.}}
  {{formatlbl |label=Values |value=Values above 2 have no case of their own: the flingy accelerates like 1 but never stops on arrival, and speed upgrades do not apply.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Flingy control: accelerates to Top Speed, brakes when Halt Distance from the target, and stops once slower than 192 at the target. Most flying units and workers}}
    {{formatbitlbl |label=0x01 |value=Accelerate without braking: stops dead on arrival. Most moving bullets, and the High Templar, the Terran buildings that lift off and the Nuclear Missile}}
    {{formatbitlbl |label=0x02 |value=Animation control: the unit moves by the distances its animation script gives each frame, without acceleration or braking, and only once it faces where it is going. Walking units, buildings and stationary effects}}
  {{end-bittable}} }}
{{end-formattable}}

---

## Appendix: Flingy list
{{begin-formattable}}
  {{formatlbl |label=Description |value=Every flingy, with the units (units.dat) or weapons (weapons.dat) that use it, its sprite and the GRP file of that sprite's image (from arr\images.tbl). All taken from the shipped data files.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Zerg Scourge (sprite 130, zerg\avenger.grp)}}
    {{formatbitlbl |label=0x01 |value=Zerg Broodling (sprite 133, zerg\brood.grp)}}
    {{formatbitlbl |label=0x02 |value=Infested Terran (sprite 135, zerg\bugguy.grp)}}
    {{formatbitlbl |label=0x03 |value=Mutalisk Cocoon (sprite 137, zerg\cocoon.grp)}}
    {{formatbitlbl |label=0x04 |value=Zerg Defiler, Unclean One (Defiler) (sprite 138, zerg\defiler.grp)}}
    {{formatbitlbl |label=0x05 |value=Zerg Drone (sprite 140, zerg\drone.grp)}}
    {{formatbitlbl |label=0x06 |value=Zerg Egg (sprite 142, zerg\egg.grp)}}
    {{formatbitlbl |label=0x07 |value=Zerg Guardian, Kukulza (Guardian) (sprite 144, zerg\guardian.grp)}}
    {{formatbitlbl |label=0x08 |value=Zerg Hydralisk, Hunter Killer (Hydralisk) (sprite 146, zerg\hydra.grp)}}
    {{formatbitlbl |label=0x09 |value=Infested Kerrigan (Infested Terran) (sprite 148, zerg\uikerr.grp)}}
    {{formatbitlbl |label=0x0A |value=Zerg Larva (sprite 149, zerg\larva.grp)}}
    {{formatbitlbl |label=0x0B |value=Zerg Mutalisk, Kukulza (Mutalisk) (sprite 151, zerg\mutalid.grp)}}
    {{formatbitlbl |label=0x0C |value=Zerg Overlord, Yggdrasill (Overlord) (sprite 153, zerg\overlord.grp)}}
    {{formatbitlbl |label=0x0D |value=Zerg Queen, Matriarch (Queen) (sprite 155, zerg\queen.grp)}}
    {{formatbitlbl |label=0x0E |value=Zerg Ultralisk, Torrasque (Ultralisk) (sprite 157, zerg\ultra.grp)}}
    {{formatbitlbl |label=0x0F |value=Zerg Zergling, Devouring One (Zergling) (sprite 159, zerg\zergling.grp)}}
    {{formatbitlbl |label=0x10 |value=Zerg Cerebrate, Zerg Cerebrate Daggoth (sprite 161, zerg\UCereb.grp)}}
    {{formatbitlbl |label=0x11 |value=Infested Command Center (sprite 162, terran\control.grp)}}
    {{formatbitlbl |label=0x12 |value=Zerg Spawning Pool (sprite 163, zerg\chrysal.grp)}}
    {{formatbitlbl |label=0x13 |value=Mature Chrysalis (sprite 164, neutral\kerrChry.grp)}}
    {{formatbitlbl |label=0x14 |value=Zerg Evolution Chamber (sprite 165, zerg\cerebrat.grp)}}
    {{formatbitlbl |label=0x15 |value=Zerg Creep Colony (sprite 166, zerg\fcolony.grp)}}
    {{formatbitlbl |label=0x16 |value=Zerg Hatchery (sprite 167, zerg\hatchery.grp)}}
    {{formatbitlbl |label=0x17 |value=Zerg Hive (sprite 168, Zerg\Hive.grp)}}
    {{formatbitlbl |label=0x18 |value=Zerg Lair (sprite 169, zerg\Lair.grp)}}
    {{formatbitlbl |label=0x19 |value=Zerg Sunken Colony (sprite 170, zerg\Lurker.grp)}}
    {{formatbitlbl |label=0x1A |value=Zerg Greater Spire (sprite 171, zerg\MutaCham.grp)}}
    {{formatbitlbl |label=0x1B |value=Zerg Defiler Mound (sprite 172, zerg\Mutapit.grp)}}
    {{formatbitlbl |label=0x1C |value=Zerg Queen's Nest (sprite 173, zerg\nest.grp)}}
    {{formatbitlbl |label=0x1D |value=Zerg Nydus Canal (sprite 174, zerg\NydusPit.grp)}}
    {{formatbitlbl |label=0x1E |value=Zerg Overmind (With Shell) (sprite 175, zerg\Over1.grp)}}
    {{formatbitlbl |label=0x1F |value=Zerg Overmind (sprite 176, zerg\Over2.grp)}}
    {{formatbitlbl |label=0x20 |value=Zerg Ultralisk Cavern (sprite 177, zerg\RCluster.grp)}}
    {{formatbitlbl |label=0x21 |value=Zerg Extractor (sprite 178, zerg\Extract.grp)}}
    {{formatbitlbl |label=0x22 |value=Zerg Hydralisk Den (sprite 179, zerg\Snakey.grp)}}
    {{formatbitlbl |label=0x23 |value=Zerg Spire (sprite 180, zerg\spire.grp)}}
    {{formatbitlbl |label=0x24 |value=Zerg Spore Colony (sprite 181, zerg\SColony.grp)}}
    {{formatbitlbl |label=0x25 |value=Protoss Arbiter, Danimoth (Arbiter) (sprite 188, protoss\arbiter.grp)}}
    {{formatbitlbl |label=0x26 |value=Protoss Archon, Tassadar/Zeratul (Archon) (sprite 189, protoss\archon.grp)}}
    {{formatbitlbl |label=0x27 |value=Protoss Carrier, Gantrithor (Carrier) (sprite 190, protoss\carrier.grp)}}
    {{formatbitlbl |label=0x28 |value=Protoss Dragoon, Fenix (Dragoon) (sprite 191, protoss\dragoon.grp)}}
    {{formatbitlbl |label=0x29 |value=Protoss Interceptor (sprite 193, protoss\Intercep.grp)}}
    {{formatbitlbl |label=0x2A |value=Protoss Probe (sprite 194, protoss\probe.grp)}}
    {{formatbitlbl |label=0x2B |value=Protoss Scout, Mojo (Scout), Artanis (Scout), … (sprite 195, protoss\scout.grp)}}
    {{formatbitlbl |label=0x2C |value=Protoss Shuttle (sprite 196, protoss\shuttle.grp)}}
    {{formatbitlbl |label=0x2D |value=Protoss High Templar, Tassadar (Templar), Aldaris (Templar) (sprite 197, protoss\templar.grp)}}
    {{formatbitlbl |label=0x2E |value=Protoss Dark Templar (Hero), Zeratul (Dark Templar) (sprite 198, protoss\dtemplar.grp)}}
    {{formatbitlbl |label=0x2F |value=Warbringer (Reaver), Protoss Reaver (sprite 199, protoss\trilob.grp)}}
    {{formatbitlbl |label=0x30 |value=Protoss Scarab (sprite 200, protoss\sapper.grp)}}
    {{formatbitlbl |label=0x31 |value=Protoss Zealot, Fenix (Zealot) (sprite 201, protoss\zealot.grp)}}
    {{formatbitlbl |label=0x32 |value=Protoss Observer (sprite 202, protoss\witness.grp)}}
    {{formatbitlbl |label=0x33 |value=Protoss Templar Archives (sprite 203, protoss\archives.grp)}}
    {{formatbitlbl |label=0x34 |value=Protoss Assimilator (sprite 204, protoss\assim.grp)}}
    {{formatbitlbl |label=0x35 |value=Protoss Observatory (sprite 205, protoss\beacon.grp)}}
    {{formatbitlbl |label=0x36 |value=Protoss Citadel of Adun (sprite 206, protoss\citadel.grp)}}
    {{formatbitlbl |label=0x37 |value=Protoss Forge (sprite 207, protoss\forge.grp)}}
    {{formatbitlbl |label=0x38 |value=Protoss Gateway (sprite 208, protoss\gateway.grp)}}
    {{formatbitlbl |label=0x39 |value=Protoss Cybernetics Core (sprite 209, protoss\gencore.grp)}}
    {{formatbitlbl |label=0x3A |value=Khaydarin Crystal Formation (sprite 210, neutral\Khyad01.grp)}}
    {{formatbitlbl |label=0x3B |value=Protoss Nexus (sprite 211, protoss\nexus.grp)}}
    {{formatbitlbl |label=0x3C |value=Protoss Photon Cannon (sprite 212, protoss\photon.grp)}}
    {{formatbitlbl |label=0x3D |value=Protoss Arbiter Tribunal (sprite 213, protoss\prism.grp)}}
    {{formatbitlbl |label=0x3E |value=Protoss Pylon (sprite 214, protoss\pylon.grp)}}
    {{formatbitlbl |label=0x3F |value=Protoss Robotics Facility (sprite 215, protoss\robotic.grp)}}
    {{formatbitlbl |label=0x40 |value=Protoss Shield Battery (sprite 216, protoss\sbattery.grp)}}
    {{formatbitlbl |label=0x41 |value=Protoss Stargate (sprite 217, protoss\stargate.grp)}}
    {{formatbitlbl |label=0x42 |value=Stasis Cell/Prison (sprite 218, neutral\stasis.grp)}}
    {{formatbitlbl |label=0x43 |value=Protoss Robotics Support Bay (sprite 219, protoss\stasis.grp)}}
    {{formatbitlbl |label=0x44 |value=Protoss Temple (sprite 220, neutral\temple.grp)}}
    {{formatbitlbl |label=0x45 |value=Protoss Fleet Beacon (sprite 221, protoss\warp.grp)}}
    {{formatbitlbl |label=0x46 |value=Terran Battlecruiser, Arcturus Mengsk (Battlecruiser), Hyperion (Battlecruiser), … (sprite 225, terran\BattleCr.grp)}}
    {{formatbitlbl |label=0x47 |value=Terran Civilian (sprite 226, neutral\civilian.grp)}}
    {{formatbitlbl |label=0x48 |value=Terran Dropship (sprite 227, terran\dropship.grp)}}
    {{formatbitlbl |label=0x49 |value=Gui Montag (Firebat), Terran Firebat (sprite 228, terran\firebat.grp)}}
    {{formatbitlbl |label=0x4A |value=Terran Ghost, Samir Duran (Ghost), Alexei Stukov (Ghost), … (sprite 229, terran\ghost.grp)}}
    {{formatbitlbl |label=0x4B |value=Terran Goliath, Alan Schezar (Goliath) (sprite 232, terran\goliath.grp)}}
    {{formatbitlbl |label=0x4C |value=Goliath Turret, Alan Schezar Turret (sprite 233, terran\goliathT.grp)}}
    {{formatbitlbl |label=0x4D |value=Sarah Kerrigan (Ghost) (sprite 234, terran\ughost.grp)}}
    {{formatbitlbl |label=0x4E |value=Terran Marine, Jim Raynor (Marine) (sprite 235, terran\marine.grp)}}
    {{formatbitlbl |label=0x4F |value=Scanner Sweep (sprite 237, terran\marine.grp)}}
    {{formatbitlbl |label=0x50 |value=Terran Wraith, Tom Kazansky (Wraith) (sprite 238, terran\phoenix.grp)}}
    {{formatbitlbl |label=0x51 |value=Terran SCV (sprite 239, terran\SCV.grp)}}
    {{formatbitlbl |label=0x52 |value=Terran Siege Tank (Tank Mode), Edmund Duke (Tank Mode) (sprite 240, terran\tank.grp)}}
    {{formatbitlbl |label=0x53 |value=Siege Tank Turret (Tank Mode), Edmund Duke Turret (Tank Mode) (sprite 241, terran\tankt.grp)}}
    {{formatbitlbl |label=0x54 |value=Edmund Duke (Siege Mode), Terran Siege Tank (Siege Mode) (sprite 242, terran\stank.grp)}}
    {{formatbitlbl |label=0x55 |value=Edmund Duke Turret (Siege Mode), Siege Tank Turret (Siege Mode) (sprite 243, terran\stankt.grp)}}
    {{formatbitlbl |label=0x56 |value=Terran Science Vessel, Magellan (Science Vessel) (sprite 246, terran\wessel.grp)}}
    {{formatbitlbl |label=0x57 |value=Not used by units or weapons (sprite 247, terran\wesselt.grp)}}
    {{formatbitlbl |label=0x58 |value=Terran Vulture, Jim Raynor (Vulture) (sprite 244, terran\Vulture.grp)}}
    {{formatbitlbl |label=0x59 |value=Spider Mine (sprite 245, terran\Spider.grp)}}
    {{formatbitlbl |label=0x5A |value=Terran Academy (sprite 248, terran\Academy.grp)}}
    {{formatbitlbl |label=0x5B |value=Terran Barracks (sprite 249, terran\TBarrack.grp)}}
    {{formatbitlbl |label=0x5C |value=Terran Armory (sprite 250, terran\chemlab.grp)}}
    {{formatbitlbl |label=0x5D |value=Terran Comsat Station (sprite 251, terran\ComSat.grp)}}
    {{formatbitlbl |label=0x5E |value=Terran Command Center (sprite 252, terran\control.grp)}}
    {{formatbitlbl |label=0x5F |value=Terran Supply Depot (sprite 253, terran\Depot.grp)}}
    {{formatbitlbl |label=0x60 |value=Terran Control Tower (sprite 254, terran\DryDocks.grp)}}
    {{formatbitlbl |label=0x61 |value=Terran Factory (sprite 255, terran\factory.grp)}}
    {{formatbitlbl |label=0x62 |value=Terran Covert Ops (sprite 256, terran\GeneLab.grp)}}
    {{formatbitlbl |label=0x63 |value=Ion Cannon (sprite 257, neutral\ion.grp)}}
    {{formatbitlbl |label=0x64 |value=Terran Machine Shop (sprite 258, terran\machines.grp)}}
    {{formatbitlbl |label=0x65 |value=Terran Missile Turret (sprite 259, terran\missile.grp)}}
    {{formatbitlbl |label=0x66 |value=Norad II (Crashed) (sprite 260, neutral\Cbattle.grp)}}
    {{formatbitlbl |label=0x67 |value=Terran Physics Lab (sprite 261, terran\physics.grp)}}
    {{formatbitlbl |label=0x68 |value=Terran Bunker (sprite 262, terran\PillBox.grp)}}
    {{formatbitlbl |label=0x69 |value=Terran Refinery (sprite 263, terran\refinery.grp)}}
    {{formatbitlbl |label=0x6A |value=Not used by units or weapons (sprite 249, terran\TBarrack.grp)}}
    {{formatbitlbl |label=0x6B |value=Terran Science Facility (sprite 264, terran\research.grp)}}
    {{formatbitlbl |label=0x6C |value=Terran Nuclear Silo (sprite 265, terran\nukesilo.grp)}}
    {{formatbitlbl |label=0x6D |value=Nuclear Missile (sprite 266, terran\nukemiss.grp)}}
    {{formatbitlbl |label=0x6E |value=Terran Starport (sprite 268, terran\starport.grp)}}
    {{formatbitlbl |label=0x6F |value=Terran Engineering Bay (sprite 269, terran\weaponpl.grp)}}
    {{formatbitlbl |label=0x70 |value=Not used by units or weapons (sprite 270, terran\TBldLrg.grp)}}
    {{formatbitlbl |label=0x71 |value=Not used by units or weapons (sprite 271, terran\TBldSml.grp)}}
    {{formatbitlbl |label=0x72 |value=Ragnasaur (Ashworld Critter) (sprite 276, neutral\Acritter.grp)}}
    {{formatbitlbl |label=0x73 |value=Rhynadon (Badlands Critter) (sprite 277, neutral\Bcritter.grp)}}
    {{formatbitlbl |label=0x74 |value=Bengalaas (Jungle Critter) (sprite 278, neutral\Jcritter.grp)}}
    {{formatbitlbl |label=0x75 |value=Vespene Geyser (sprite 275, neutral\geyser.grp)}}
    {{formatbitlbl |label=0x76 |value=Mineral Field (Type 1) (sprite 279, neutral\min01.grp)}}
    {{formatbitlbl |label=0x77 |value=Mineral Field (Type 2) (sprite 280, neutral\min02.grp)}}
    {{formatbitlbl |label=0x78 |value=Mineral Field (Type 3) (sprite 281, neutral\min03.grp)}}
    {{formatbitlbl |label=0x79 |value=Independent Starport (Unused) (sprite 282, protoss\scout.grp)}}
    {{formatbitlbl |label=0x7A |value=Zerg Beacon, Zerg Flag Beacon (sprite 283, zerg\zmarker.grp)}}
    {{formatbitlbl |label=0x7B |value=Terran Beacon, Terran Flag Beacon (sprite 284, terran\tMarker.grp)}}
    {{formatbitlbl |label=0x7C |value=Protoss Beacon, Protoss Flag Beacon (sprite 285, protoss\pMarker.grp)}}
    {{formatbitlbl |label=0x7D |value=Dark Swarm (sprite 286, thingy\Dswarm.grp)}}
    {{formatbitlbl |label=0x7E |value=Flag (sprite 287, neutral\Flag.grp)}}
    {{formatbitlbl |label=0x7F |value=Young Chrysalis (sprite 288, neutral\KerrEgg.grp)}}
    {{formatbitlbl |label=0x80 |value=Psi Emitter (sprite 289, neutral\PsiEmit.grp)}}
    {{formatbitlbl |label=0x81 |value=Data Disc (sprite 290, neutral\DataDisk.grp)}}
    {{formatbitlbl |label=0x82 |value=Khaydarin Crystal (sprite 291, neutral\KhChunk.grp)}}
    {{formatbitlbl |label=0x83 |value=Mineral Cluster Type 1 (sprite 292, neutral\OreChunk.grp)}}
    {{formatbitlbl |label=0x84 |value=Mineral Cluster Type 2 (sprite 293, neutral\OreChunk.grp)}}
    {{formatbitlbl |label=0x85 |value=Protoss Vespene Gas Orb Type 1 (sprite 294, neutral\GasOrb.grp)}}
    {{formatbitlbl |label=0x86 |value=Protoss Vespene Gas Orb Type 2 (sprite 295, neutral\GasOrb.grp)}}
    {{formatbitlbl |label=0x87 |value=Zerg Vespene Gas Sac Type 1 (sprite 296, neutral\GasSac.grp)}}
    {{formatbitlbl |label=0x88 |value=Zerg Vespene Gas Sac Type 2 (sprite 297, neutral\GasSac.grp)}}
    {{formatbitlbl |label=0x89 |value=Terran Vespene Gas Tank Type 1 (sprite 298, neutral\GasTank.grp)}}
    {{formatbitlbl |label=0x8A |value=Terran Vespene Gas Tank Type 2 (sprite 299, neutral\GasTank.grp)}}
    {{formatbitlbl |label=0x8B |value=Map Revealer (sprite 302, neutral\maprev.grp)}}
    {{formatbitlbl |label=0x8C |value=Start Location (sprite 301, thingy\StartLoc.grp)}}
    {{formatbitlbl |label=0x8D |value=Fusion Cutter, Fusion Cutter (Harvest) (sprite 340, bullet\scvspark.grp)}}
    {{formatbitlbl |label=0x8E |value=Gauss Rifle (Normal), Gauss Rifle (Jim Raynor-Marine), Twin Autocannons (Normal) … (sprite 341, bullet\tspark.grp)}}
    {{formatbitlbl |label=0x8F |value=C-10 Concussion Rifle (Normal), C-10 Concussion Rifle (Sarah Kerrigan), Arclite Cannon (Normal) … (sprite 346, thingy\ecaHit.grp)}}
    {{formatbitlbl |label=0x90 |value=Gemini Missiles (Normal), Gemini Missiles (Tom Kazansky), Tormentor Missiles (Unused) (sprite 342, bullet\gemini.grp)}}
    {{formatbitlbl |label=0x91 |value=Fragmentation Grenade (Normal), Fragmentation Grenade (Jim Raynor-Vulture), Flechette Grenade (Unused) (sprite 343, bullet\grenade.grp)}}
    {{formatbitlbl |label=0x92 |value=Hellfire Missile Pack (Normal), Hellfire Missile Pack (Alan Schezar), Longbolt Missiles … (sprite 345, bullet\missile.grp)}}
    {{formatbitlbl |label=0x93 |value=Not used by units or weapons (sprite 344, thingy\eldFire.grp)}}
    {{formatbitlbl |label=0x94 |value=ATS Laser Battery (Normal), ATA Laser Battery (Normal), ATS Laser Battery (Norad II+Mengsk+DuGalle) … (sprite 347, thingy\elbfire.grp)}}
    {{formatbitlbl |label=0x95 |value=Burst Lasers (Normal), Burst Lasers (Tom Kazansky) (sprite 348, thingy\elbfireW.grp)}}
    {{formatbitlbl |label=0x96 |value=Arclite Shock Cannon (Normal), Arclite Shock Cannon (Edmund Duke) (sprite 349, thingy\mushroom.grp)}}
    {{formatbitlbl |label=0x97 |value=EMP Shockwave (sprite 352, bullet\missile.grp)}}
    {{formatbitlbl |label=0x98 |value=Unknown72, Dual Photon Blasters (Normal), Dual Photon Blasters (Mojo) … (sprite 333, bullet\pspark.grp)}}
    {{formatbitlbl |label=0x99 |value=Particle Beam, Particle Beam (Harvest) (sprite 334, bullet\ephFire.grp)}}
    {{formatbitlbl |label=0x9A |value=Anti-matter Missiles (Normal), Anti-matter Missiles (Mojo), Anti-matter Missiles (Artanis) (sprite 335, bullet\hks.grp)}}
    {{formatbitlbl |label=0x9B |value=Pulse Cannon (sprite 336, bullet\blastcan.grp)}}
    {{formatbitlbl |label=0x9C |value=Psionic Shockwave (Normal), Psionic Shockwave (Tassadar/Zeratul Archon) (sprite 366, thingy\emsHit.grp)}}
    {{formatbitlbl |label=0x9D |value=Psi Storm, Feedback (sprite 339, thingy\psiStorm.grp)}}
    {{formatbitlbl |label=0x9E |value=Yamato Gun (sprite 350, bullet\eycBull.grp)}}
    {{formatbitlbl |label=0x9F |value=Phase Disruptor (Normal), Phase Disruptor (Fenix-Dragoon), Phase Disruptor Cannon (Normal) … (sprite 337, bullet\dragbull.grp)}}
    {{formatbitlbl |label=0xA0 |value=STS Photon Cannon, STA Photon Cannon (sprite 338, bullet\epbBul.grp)}}
    {{formatbitlbl |label=0xA1 |value=Subterranean Tentacle (sprite 355, bullet\Tentacle.grp)}}
    {{formatbitlbl |label=0xA2 |value=Venom (Unused-Defiler), Venom (Unused-Defiler Hero) (sprite 356, thingy\ep2Fire.grp)}}
    {{formatbitlbl |label=0xA3 |value=Acid Spore (Normal), Acid Spore (Kukulza-Guardian) (sprite 357, thingy\ep3Shot.grp)}}
    {{formatbitlbl |label=0xA4 |value=Not used by units or weapons (sprite 354, bullet\PDripHit.grp)}}
    {{formatbitlbl |label=0xA5 |value=Glave Wurm (Normal), Glave Wurm (Kukulza-Mutalisk) (sprite 358, bullet\spores.grp)}}
    {{formatbitlbl |label=0xA6 |value=Seeker Spores (sprite 359, bullet\Spore2.grp)}}
    {{formatbitlbl |label=0xA7 |value=Parasite, Spawn Broodlings, Ensnare (sprite 360, bullet\parasite.grp)}}
    {{formatbitlbl |label=0xA8 |value=Plague (sprite 362, thingy\ebbCloud.grp)}}
    {{formatbitlbl |label=0xA9 |value=Consume (sprite 363, thingy\consume.grp)}}
    {{formatbitlbl |label=0xAA |value=Not used by units or weapons (sprite 364, thingy\Ensnare.grp)}}
    {{formatbitlbl |label=0xAB |value=Needle Spines (Normal), Needle Spines (Hunter Killer), Spines … (sprite 353, bullet\zspark.grp)}}
    {{formatbitlbl |label=0xAC |value=Spider Mines, Flame Thrower (Normal), Flame Thrower (Gui Montag) … (sprite 370, bullet\circle14.grp)}}
    {{formatbitlbl |label=0xAD |value=Left Upper Level Door (sprite 381, thingy\tileset\install\CRDoor1.grp)}}
    {{formatbitlbl |label=0xAE |value=Right Upper Level Door (sprite 382, thingy\tileset\install\CRDoor1.grp)}}
    {{formatbitlbl |label=0xAF |value=Left Pit Door (sprite 383, thingy\tileset\install\DIDoor1.grp)}}
    {{formatbitlbl |label=0xB0 |value=Right Pit Door (sprite 384, thingy\tileset\install\DIDoor1.grp)}}
    {{formatbitlbl |label=0xB1 |value=Floor Hatch (Unused) (sprite 385, thingy\tileset\install\DIHatc1.grp)}}
    {{formatbitlbl |label=0xB2 |value=Floor Gun Trap (sprite 303, thingy\tileset\install\CLPlate2.grp)}}
    {{formatbitlbl |label=0xB3 |value=Floor Missile Trap (sprite 308, thingy\tileset\install\CLPlate1.grp)}}
    {{formatbitlbl |label=0xB4 |value=Left Wall Missile Trap (sprite 304, thingy\tileset\install\DCGun1.grp)}}
    {{formatbitlbl |label=0xB5 |value=Right Wall Missile Trap (sprite 305, thingy\tileset\install\DCGun1.grp)}}
    {{formatbitlbl |label=0xB6 |value=Left Wall Flame Trap (sprite 306, thingy\tileset\install\DCGun2.grp)}}
    {{formatbitlbl |label=0xB7 |value=Right Wall Flame Trap (sprite 307, thingy\tileset\install\DCGun2.grp)}}
    {{formatbitlbl |label=0xB8 |value=Lurker Egg (sprite 481, zerg\Lurkegg.grp)}}
    {{formatbitlbl |label=0xB9 |value=Zerg Devourer (sprite 482, zerg\devour.grp)}}
    {{formatbitlbl |label=0xBA |value=Zerg Lurker (sprite 485, zerg\Zlurker.grp)}}
    {{formatbitlbl |label=0xBB |value=Protoss Dark Archon (sprite 486, protoss\darchn.grp)}}
    {{formatbitlbl |label=0xBC |value=Protoss Dark Templar (Unit) (sprite 488, protoss\dtemplar.grp)}}
    {{formatbitlbl |label=0xBD |value=Terran Medic (sprite 489, terran\medic.grp)}}
    {{formatbitlbl |label=0xBE |value=Terran Valkyrie (sprite 491, terran\bomber.grp)}}
    {{formatbitlbl |label=0xBF |value=Protoss Corsair, Raszagal (Corsair) (sprite 487, protoss\corsair.grp)}}
    {{formatbitlbl |label=0xC0 |value=Disruption Web (sprite 503, thingy\Disrupt.grp)}}
    {{formatbitlbl |label=0xC1 |value=Overmind Cocoon (sprite 495, zerg\XOvermnd.grp)}}
    {{formatbitlbl |label=0xC2 |value=Psi Disrupter (sprite 498, neutral\PsiDisr.grp)}}
    {{formatbitlbl |label=0xC3 |value=Warp Gate (sprite 499, protoss\XwarpGat.grp)}}
    {{formatbitlbl |label=0xC4 |value=Power Generator (sprite 496, neutral\Generate.grp)}}
    {{formatbitlbl |label=0xC5 |value=Xel'Naga Temple (sprite 497, protoss\XelTempl.grp)}}
    {{formatbitlbl |label=0xC6 |value=Scantid (Desert Critter) (sprite 492, neutral\Kcritter.grp)}}
    {{formatbitlbl |label=0xC7 |value=Kakaru (Twilight Critter) (sprite 493, neutral\Scritter.grp)}}
    {{formatbitlbl |label=0xC8 |value=Ursadon (Ice World Critter) (sprite 494, neutral\Icritter.grp)}}
    {{formatbitlbl |label=0xC9 |value=Optical Flare (sprite 508, bullet\grenade.grp)}}
    {{formatbitlbl |label=0xCA |value=Halo Rockets (sprite 509, bullet\SMmissle.grp)}}
    {{formatbitlbl |label=0xCB |value=Subterranean Spines (sprite 510, zerg\zmarker.grp)}}
    {{formatbitlbl |label=0xCC |value=Corrosive Acid (sprite 512, thingy\ZDvPuke.grp)}}
    {{formatbitlbl |label=0xCD |value=Not used by units or weapons (sprite 513, thingy\ZDvHit.grp)}}
    {{formatbitlbl |label=0xCE |value=Neutron Flare (sprite 506, thingy\PcsSplsh.grp)}}
    {{formatbitlbl |label=0xCF |value=Uraj Crystal (sprite 515, neutral\Uraj.grp)}}
    {{formatbitlbl |label=0xD0 |value=Khalis Crystal (sprite 516, neutral\Khalis.grp)}}
  {{end-bittable}} }}
{{end-formattable}}

