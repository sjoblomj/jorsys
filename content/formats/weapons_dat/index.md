# weapons.dat Format

## Label
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Label displayed for this weapon in unit's status bar. Corresponds to an entry in the rez\stat_txt.tbl file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to the last index of the rez\stat_txt.tbl file.}}
{{end-formattable}}

## Missile Sprite
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0104}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Sprite displayed when the weapon is fired. Corresponds to an entry in the flingy.dat file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the # of entries in flingy.dat}}
{{end-formattable}}

## Special Attack
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x030C}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Spell/special effect to use with this weapon.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x00 |value=Nothing}}      {{formatbitlbl |label=0x01 |value=Lockdown}}      {{formatbitlbl |label=0x02 |value=EMP Shockwave}}      {{formatbitlbl |label=0x03 |value=Spider Mines}}      {{formatbitlbl |label=0x04 |value=Normal}}      {{formatbitlbl |label=0x05 |value=No Damage}}      {{formatbitlbl |label=0x06 |value=No Damage}}      {{formatbitlbl |label=0x07 |value=Irradiate}}      {{formatbitlbl |label=0x08 |value=Yamato Gun}}      {{formatbitlbl |label=0x09 |value=No Damage}}      {{formatbitlbl |label=0x0A |value=No Damage}}      {{formatbitlbl |label=0x0B |value=No Damage}}      {{formatbitlbl |label=0x0C |value=No Damage}}      {{formatbitlbl |label=0x0D |value=Broodling}}      {{formatbitlbl |label=0x0E |value=Dark Swarm}}      {{formatbitlbl |label=0x0F |value=Plague}}      {{formatbitlbl |label=0x10 |value=Consume}}      {{formatbitlbl |label=0x11 |value=Ensnare}}      {{formatbitlbl |label=0x12 |value=Parasite}}      {{formatbitlbl |label=0x13 |value=Psi Storm}}      {{formatbitlbl |label=0x14 |value=Normal}}      {{formatbitlbl |label=0x15 |value=Normal}}      {{formatbitlbl |label=0x16 |value=Stasis}}      {{formatbitlbl |label=0x17 |value=1/4 Damage}}      {{formatbitlbl |label=0x18 |value=Restoration}}      {{formatbitlbl |label=0x19 |value=Disruption Web}}      {{formatbitlbl |label=0x1A |value=Unknown}}      {{formatbitlbl |label=0x1B |value=Unknown}}      {{formatbitlbl |label=0x1C |value=Unknown}}      {{formatbitlbl |label=0x1D |value=Feedback}}      {{formatbitlbl |label=0x1E |value=Optical Flare}}      {{formatbitlbl |label=0x1F |value=Maelstrom/Spines}}      {{formatbitlbl |label=0x20 |value=Unknown}}      {{formatbitlbl |label=0x21 |value=Unknown}}      {{formatbitlbl |label=0x22 |value=Unknown}}      {{formatbitlbl |label=0x23 |value=Unknown}}      {{formatbitlbl |label=0x24 |value=Unknown}}      {{formatbitlbl |label=0x25 |value=Unknown}}      {{formatbitlbl |label=0x26 |value=Unknown}}      {{formatbitlbl |label=0x27 |value=Unknown}}      {{formatbitlbl |label=0x28 |value=Unknown}}      {{formatbitlbl |label=0x29 |value=Unknown}}      {{formatbitlbl |label=0x2A |value=Unknown}}      {{formatbitlbl |label=0x2B |value=Unknown}}      {{formatbitlbl |label=0x2C |value=None}}    {{end-bittable}}  }}
{{end-formattable}}

## Attack Type
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x038E}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Restrictions for where the weapon can be used.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x0001 |value=Air Only}}      {{formatbitlbl |label=0x0002 |value=Ground Only}}      {{formatbitlbl |label=0x0003 |value=Air and Ground}}      {{formatbitlbl |label=0x0004 |value=Units Only (No Buildings)}}      {{formatbitlbl |label=0x0012 |value=Ground Units (No Hover or Buildings)}}      {{formatbitlbl |label=0x0013 |value=Ground Units Only (No Buildings}}      {{formatbitlbl |label=0x0019 |value=Mechanical Only}}      {{formatbitlbl |label=0x0043 |value=Non-mechanical Only}}      {{formatbitlbl |label=0x0053 |value=Ground, Ground Units}}      {{formatbitlbl |label=0x00B2 |value=Ground Units (No Buildings, No Archon)}}      {{formatbitlbl |label=0x011B |value=Owned Units (Consume)}}    {{end-bittable}}  }}
{{end-formattable}}

## Minimum Range
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0492}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Minimum range required for this weapon.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Maximum Range
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x069A}}
  {{formatlbl |label=Length |value=520 bytes (4 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Maximum range required to use this weapon.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Upgrade Group
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x08A2}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Upgrade group which applies to this weapon.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index of the Upgrades.dat file. Common values are:}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x07 |value=Terran Infantry}}      {{formatbitlbl |label=0x08 |value=Terran Vehicle}}      {{formatbitlbl |label=0x09 |value=Terran Ship}}      {{formatbitlbl |label=0x0A |value=Zerg Melee}}      {{formatbitlbl |label=0x0B |value=Zerg Missile}}      {{formatbitlbl |label=0x0C |value=Zerg Flyer}}      {{formatbitlbl |label=0x0D |value=Protoss Ground}}      {{formatbitlbl |label=0x0E |value=Protoss Air}}      {{formatbitlbl |label=0x23 |value=Scarab}}      {{formatbitlbl |label=0x3C |value=No upgrades}}    {{end-bittable}}  }}
{{end-formattable}}

## Weapon Type
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0924}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The type of this weapon.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x00 |value=Unknown}}      {{formatbitlbl |label=0x01 |value=Explosive}}      {{formatbitlbl |label=0x02 |value=Concussive}}      {{formatbitlbl |label=0x03 |value=Normal}}      {{formatbitlbl |label=0x04 |value=Special}}    {{end-bittable}}  }}
{{end-formattable}}

## Weapon Behavior
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x09A6}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The behavior this weapon uses.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x00 |value=Flies to target}}      {{formatbitlbl |label=0x01 |value=Seeks Target}}      {{formatbitlbl |label=0x02 |value=Appears on Target}}      {{formatbitlbl |label=0x03 |value=Unknown}}      {{formatbitlbl |label=0x04 |value=Persistant Explosion}}      {{formatbitlbl |label=0x05 |value=Normal hit}}      {{formatbitlbl |label=0x06 |value=Suicide}}      {{formatbitlbl |label=0x07 |value=Bounce}}      {{formatbitlbl |label=0x08 |value=Spin around (Halo)}}      {{formatbitlbl |label=0x09 |value=Bursts thru ground (Sub. Spines)}}    {{end-bittable}}  }}
{{end-formattable}}

## Missile Type
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0A28}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The type of missile this Weapon emulates.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x1E |value=Homing}}      {{formatbitlbl |label=0x3C |value=Bouncing}}      {{formatbitlbl |label=0xFF |value=Normal}}    {{end-bittable}}  }}
{{end-formattable}}

## Explosion Type
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0AAA}}
  {{formatlbl |label=Length |value=}}
  {{formatlbl |label=Description |value=Type of explosion which occurs after the weapon hits its target.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}      {{formatbitlbl |label=0x00 |value=None}}      {{formatbitlbl |label=0x01 |value=Normal}}      {{formatbitlbl |label=0x02 |value=Radial Splash}}      {{formatbitlbl |label=0x03 |value=Line Splash}}      {{formatbitlbl |label=0x04 |value=Lockdown}}      {{formatbitlbl |label=0x05 |value=Unknown}}      {{formatbitlbl |label=0x06 |value=Parasite}}      {{formatbitlbl |label=0x07 |value=Spawn Broodlings}}      {{formatbitlbl |label=0x08 |value=EMP Shockwave}}      {{formatbitlbl |label=0x09 |value=Irradiate}}      {{formatbitlbl |label=0x0A |value=Ensnare}}      {{formatbitlbl |label=0x0B |value=Plague}}      {{formatbitlbl |label=0x0C |value=Stasis}}      {{formatbitlbl |label=0x0D |value=Dark Swarm}}      {{formatbitlbl |label=0x0E |value=Radial Splash}}      {{formatbitlbl |label=0x0F |value=Line Splash}}      {{formatbitlbl |label=0x10 |value=Restoration}}      {{formatbitlbl |label=0x11 |value=Disruption Web}}      {{formatbitlbl |label=0x12 |value=Corrosive Acid}}      {{formatbitlbl |label=0x13 |value=Mind Control}}      {{formatbitlbl |label=0x14 |value=Feedback}}      {{formatbitlbl |label=0x15 |value=Optical Flare}}      {{formatbitlbl |label=0x16 |value=Maelstrom}}      {{formatbitlbl |label=0x17 |value=Unknown}}      {{formatbitlbl |label=0x18 |value=Air Splash}}    {{end-bittable}}  }}
{{end-formattable}}

## Splash Value 1
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0B2C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Smallest of 3 radii which the Explosion Type uses to deal damage.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Splash Value 2
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0C30}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Middle of 3 radii which the Explosion Type uses to deal damage.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Splash Value 3
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0D34}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Largest of 3 radii which the Explosion Type uses to deal damage.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Damage Amount
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0E38}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Amount of damage dealt to target. May be adjusted based on the type of unit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Damage Bonus
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0F3C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Amount added to damage when the weapon is upgraded.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cooldown Delay
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1040}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=Delay between attacks with this weapon. Lower values make the weapon attack faster, and higher values make the weapon attack slower.}}
  {{formatlbl |label=Values |value=Integer value between 1 and 255.}}
{{end-formattable}}

## Damage Factor
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x10C2}}
  {{formatlbl |label=Length |value=130 bytes (1 byte / Weapon)}}
  {{formatlbl |label=Description |value=The number of "copies" of this weapon a unit assigned this weapon has. To get the actual damage amount for units with more than 1 in the factor category, multiply this value by the Damage Amount.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 255.}}
{{end-formattable}}

## Coordinate Group 1
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1144}}
  {{formatlbl |label=Length |value=260 Bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Actually an x-y pair of values. The first byte is actually the X coordinate, and the second is the Y coordinate.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 255 for both the X and Y parts of the coordinate.}}
{{end-formattable}}

## Coordinate Group 2
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1248}}
  {{formatlbl |label=Length |value=260 Bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Actually an x-y pair of values. The first byte is actually the X coordinate, and the second is the Y coordinate.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 255 for both the X and Y parts of the coordinate.}}
{{end-formattable}}

## Error Message
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x134C}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Index in the rez\stat_txt.tbl file which this weapon displays if it cannot be used for some reason.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the last index in rez\stat_txt.tbl}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1450}}
  {{formatlbl |label=Length |value=260 bytes (2 bytes / Weapon)}}
  {{formatlbl |label=Description |value=Icon displayed for this weapon in the unit's status bar.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

