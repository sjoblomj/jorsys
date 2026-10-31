# weapons.dat Format

## Label
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Label displayed for this weapon in unit's status bar. Corresponds to an entry in the rez\stat_txt.tbl file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to the last index of the rez\stat_txt.tbl file.}}
{{end-formattable}}

## Missile Sprite
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0104}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Sprite displayed when the weapon is fired. Corresponds to an entry in the flingy.dat file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the # of entries in flingy.dat}}
{{end-formattable}}

## Special Attack
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x030C}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Spell/special effect to use with this weapon.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Nothing}}
    {{formatbitlbl |label=0x01 |value=Lockdown}}
    {{formatbitlbl |label=0x02 |value=EMP Shockwave}}
    {{formatbitlbl |label=0x03 |value=Spider Mines}}
    {{formatbitlbl |label=0x04 |value=Normal}}
    {{formatbitlbl |label=0x05 |value=No Damage}}
    {{formatbitlbl |label=0x06 |value=No Damage}}
    {{formatbitlbl |label=0x07 |value=Irradiate}}
    {{formatbitlbl |label=0x08 |value=Yamato Gun}}
    {{formatbitlbl |label=0x09 |value=No Damage}}
    {{formatbitlbl |label=0x0A |value=No Damage}}
    {{formatbitlbl |label=0x0B |value=No Damage}}
    {{formatbitlbl |label=0x0C |value=No Damage}}
    {{formatbitlbl |label=0x0D |value=Broodling}}
    {{formatbitlbl |label=0x0E |value=Dark Swarm}}
    {{formatbitlbl |label=0x0F |value=Plague}}
    {{formatbitlbl |label=0x10 |value=Consume}}
    {{formatbitlbl |label=0x11 |value=Ensnare}}
    {{formatbitlbl |label=0x12 |value=Parasite}}
    {{formatbitlbl |label=0x13 |value=Psi Storm}}
    {{formatbitlbl |label=0x14 |value=Normal}}
    {{formatbitlbl |label=0x15 |value=Normal}}
    {{formatbitlbl |label=0x16 |value=Stasis}}
    {{formatbitlbl |label=0x17 |value=1/4 Damage}}
    {{formatbitlbl |label=0x18 |value=Restoration}}
    {{formatbitlbl |label=0x19 |value=Disruption Web}}
    {{formatbitlbl |label=0x1A |value=Unknown}}
    {{formatbitlbl |label=0x1B |value=Unknown}}
    {{formatbitlbl |label=0x1C |value=Unknown}}
    {{formatbitlbl |label=0x1D |value=Feedback}}
    {{formatbitlbl |label=0x1E |value=Optical Flare}}
    {{formatbitlbl |label=0x1F |value=Maelstrom/Spines}}
    {{formatbitlbl |label=0x20 |value=Unknown}}
    {{formatbitlbl |label=0x21 |value=Unknown}}
    {{formatbitlbl |label=0x22 |value=Unknown}}
    {{formatbitlbl |label=0x23 |value=Unknown}}
    {{formatbitlbl |label=0x24 |value=Unknown}}
    {{formatbitlbl |label=0x25 |value=Unknown}}
    {{formatbitlbl |label=0x26 |value=Unknown}}
    {{formatbitlbl |label=0x27 |value=Unknown}}
    {{formatbitlbl |label=0x28 |value=Unknown}}
    {{formatbitlbl |label=0x29 |value=Unknown}}
    {{formatbitlbl |label=0x2A |value=Unknown}}
    {{formatbitlbl |label=0x2B |value=Unknown}}
    {{formatbitlbl |label=0x2C |value=None}}
  {{end-bittable}} }}
{{end-formattable}}

## Attack Type
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x038E}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Restrictions for where the weapon can be used.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0001 |value=Air Only}}
    {{formatbitlbl |label=0x0002 |value=Ground Only}}
    {{formatbitlbl |label=0x0003 |value=Air and Ground}}
    {{formatbitlbl |label=0x0004 |value=Units Only (No Buildings)}}
    {{formatbitlbl |label=0x0012 |value=Ground Units (No Hover or Buildings)}}
    {{formatbitlbl |label=0x0013 |value=Ground Units Only (No Buildings}}
    {{formatbitlbl |label=0x0019 |value=Mechanical Only}}
    {{formatbitlbl |label=0x0043 |value=Non-mechanical Only}}
    {{formatbitlbl |label=0x0053 |value=Ground, Ground Units}}
    {{formatbitlbl |label=0x00B2 |value=Ground Units (No Buildings, No Archon)}}
    {{formatbitlbl |label=0x011B |value=Owned Units (Consume)}}
  {{end-bittable}} }}
{{end-formattable}}

## Minimum Range
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0492}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Minimum range required for this weapon.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Maximum Range
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x069A}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Maximum range required to use this weapon.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Upgrade Group
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x08A2}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Upgrade group which applies to this weapon.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of the Upgrades.dat file. Common values are:}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x07 |value=Terran Infantry}}
    {{formatbitlbl |label=0x08 |value=Terran Vehicle}}
    {{formatbitlbl |label=0x09 |value=Terran Ship}}
    {{formatbitlbl |label=0x0A |value=Zerg Melee}}
    {{formatbitlbl |label=0x0B |value=Zerg Missile}}
    {{formatbitlbl |label=0x0C |value=Zerg Flyer}}
    {{formatbitlbl |label=0x0D |value=Protoss Ground}}
    {{formatbitlbl |label=0x0E |value=Protoss Air}}
    {{formatbitlbl |label=0x23 |value=Scarab}}
    {{formatbitlbl |label=0x3C |value=No upgrades}}
  {{end-bittable}} }}
{{end-formattable}}

## Weapon Type
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0924}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The type of this weapon.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Unknown}}
    {{formatbitlbl |label=0x01 |value=Explosive}}
    {{formatbitlbl |label=0x02 |value=Concussive}}
    {{formatbitlbl |label=0x03 |value=Normal}}
    {{formatbitlbl |label=0x04 |value=Special}}
  {{end-bittable}} }}
{{end-formattable}}

## Weapon Behavior
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x09A6}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The behavior this weapon uses.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Flies to target}}
    {{formatbitlbl |label=0x01 |value=Seeks Target}}
    {{formatbitlbl |label=0x02 |value=Appears on Target}}
    {{formatbitlbl |label=0x03 |value=Unknown}}
    {{formatbitlbl |label=0x04 |value=Persistant Explosion}}
    {{formatbitlbl |label=0x05 |value=Normal hit}}
    {{formatbitlbl |label=0x06 |value=Suicide}}
    {{formatbitlbl |label=0x07 |value=Bounce}}
    {{formatbitlbl |label=0x08 |value=Spin around (Halo)}}
    {{formatbitlbl |label=0x09 |value=Bursts thru ground (Sub. Spines)}}
  {{end-bittable}} }}
{{end-formattable}}

## Missile Type
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0A28}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The type of missile this Weapon emulates.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x1E |value=Homing}}
    {{formatbitlbl |label=0x3C |value=Bouncing}}
    {{formatbitlbl |label=0xFF |value=Normal}}
  {{end-bittable}} }}
{{end-formattable}}

## Explosion Type
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0AAA}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Type of explosion which occurs after the weapon hits its target.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=None}}
    {{formatbitlbl |label=0x01 |value=Normal}}
    {{formatbitlbl |label=0x02 |value=Radial Splash}}
    {{formatbitlbl |label=0x03 |value=Line Splash}}
    {{formatbitlbl |label=0x04 |value=Lockdown}}
    {{formatbitlbl |label=0x05 |value=Unknown}}
    {{formatbitlbl |label=0x06 |value=Parasite}}
    {{formatbitlbl |label=0x07 |value=Spawn Broodlings}}
    {{formatbitlbl |label=0x08 |value=EMP Shockwave}}
    {{formatbitlbl |label=0x09 |value=Irradiate}}
    {{formatbitlbl |label=0x0A |value=Ensnare}}
    {{formatbitlbl |label=0x0B |value=Plague}}
    {{formatbitlbl |label=0x0C |value=Stasis}}
    {{formatbitlbl |label=0x0D |value=Dark Swarm}}
    {{formatbitlbl |label=0x0E |value=Radial Splash}}
    {{formatbitlbl |label=0x0F |value=Line Splash}}
    {{formatbitlbl |label=0x10 |value=Restoration}}
    {{formatbitlbl |label=0x11 |value=Disruption Web}}
    {{formatbitlbl |label=0x12 |value=Corrosive Acid}}
    {{formatbitlbl |label=0x13 |value=Mind Control}}
    {{formatbitlbl |label=0x14 |value=Feedback}}
    {{formatbitlbl |label=0x15 |value=Optical Flare}}
    {{formatbitlbl |label=0x16 |value=Maelstrom}}
    {{formatbitlbl |label=0x17 |value=Unknown}}
    {{formatbitlbl |label=0x18 |value=Air Splash}}
  {{end-bittable}} }}
{{end-formattable}}

## Splash Value 1
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0B2C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Smallest of 3 radii which the Explosion Type uses to deal damage.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Splash Value 2
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0C30}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Middle of 3 radii which the Explosion Type uses to deal damage.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Splash Value 3
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0D34}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Largest of 3 radii which the Explosion Type uses to deal damage.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Damage Amount
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0E38}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Amount of damage dealt to target. May be adjusted based on the type of unit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Damage Bonus
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0F3C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Amount added to damage when the weapon is upgraded.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cooldown Delay
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1040}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Delay between attacks with this weapon. Lower values make the weapon attack faster, and higher values make the weapon attack slower.}}
  {{formatlbl |label=Values |value=Integer value between 1 and 255.}}
{{end-formattable}}

## Damage Factor
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x10C2}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The number of "copies" of this weapon a unit assigned this weapon has. To get the actual damage amount for units with more than 1 in the factor category, multiply this value by the Damage Amount.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 255.}}
{{end-formattable}}

## Coordinate Group 1
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1144}}
  {{formatlbl |label=Length |value=260 Bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Actually an x-y pair of values. The first byte is actually the X coordinate, and the second is the Y coordinate.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 255 for both the X and Y parts of the coordinate.}}
{{end-formattable}}

## Coordinate Group 2
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1248}}
  {{formatlbl |label=Length |value=260 Bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Actually an x-y pair of values. The first byte is actually the X coordinate, and the second is the Y coordinate.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 255 for both the X and Y parts of the coordinate.}}
{{end-formattable}}

## Error Message
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x134C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Index in the rez\stat_txt.tbl file which this weapon displays if it cannot be used for some reason.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index in rez\stat_txt.tbl}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1450}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Icon displayed for this weapon in the unit's status bar.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

---

## Appendix: Weapons list
{{begin-formattable}}
  {{formatlbl |label=Description |value=List of weapons.}}
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

