# units.dat Format

## Graphic
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Graphic of unit. Corresponds to an entry in the Images data file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Subunit 1
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x00E4}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Subunit 1 for this unit. Corresponds to another entry in this file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Subunit 2
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x02AC}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Subunit 2 for this unit. Corresponds to another entry in this file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Subunit 3
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0474}}
  {{formatlbl |label=Length |value=192 bytes (2 bytes / Unit) (First 96 Units only)}}
  {{formatlbl |label=Description |value=Subunit 3 for this unit. Corresponds to another entry in this file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Construction Animation
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0534}}
  {{formatlbl |label=Length |value=912 bytes (4 bytes / Unit)}}
  {{formatlbl |label=Description |value=Construction Animation for this unit.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0 |value=None}}
    {{formatbitlbl |label=2 |value=Zerg Scourge}}
    {{formatbitlbl |label=15 |value=Zerg Defiler}}
    {{formatbitlbl |label=19 |value=Zerg Drone}}
    {{formatbitlbl |label=27 |value=Zerg Guardian}}
    {{formatbitlbl |label=31 |value=Zerg Hydralisk}}
    {{formatbitlbl |label=40 |value=Zerg Mutalisk}}
    {{formatbitlbl |label=44 |value=Zerg Overlord}}
    {{formatbitlbl |label=49 |value=Zerg Queen}}
    {{formatbitlbl |label=52 |value=Zerg Ultralisk}}
    {{formatbitlbl |label=56 |value=Zerg Zergling}}
    {{formatbitlbl |label=101 |value=Infested Command Center}}
    {{formatbitlbl |label=102 |value=Zerg Extractor}}
    {{formatbitlbl |label=103 |value=Zerg Building Upgrade}}
    {{formatbitlbl |label=104 |value=Zerg Large Construction}}
    {{formatbitlbl |label=105 |value=Zerg Small Construction}}
    {{formatbitlbl |label=200 |value=Protoss Stargate}}
    {{formatbitlbl |label=325 |value=Terran Large Construction}}
    {{formatbitlbl |label=327 |value=Terram Small Construction}}
    {{formatbitlbl |label=329 |value=Terran Missile Tower}}
    {{formatbitlbl |label=330 |value=Terran Addon Construction}}
  {{end-bittable}} }}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x08C4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 255}}
{{end-formattable}}

## Shield Enable
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x09A8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Enables shields.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0 |value=false}}
    {{formatbitlbl |label=1 |value=true}}
  {{end-bittable}} }}
{{end-formattable}}

## Shield Amount
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0A8C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Shield Amount.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535.}}
{{end-formattable}}

## Hitpoints
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0C54}}
  {{formatlbl |label=Length |value=912 bytes (4 bytes / Unit)}}
  {{formatlbl |label=Description |value=Hitpoint Amount. Lower 24 bits are the hitpoint value. The 4 high bits are unknown.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 4294967295}}
{{end-formattable}}

## Animation Level
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0FE4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Animation level this unit is drawn at. Basically Z-Order.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0 |value=Below Ground (Can walk under everything but Buildings)}}
    {{formatbitlbl |label=1 |value=Below Ground (Can walk under everything but Buildings)}}
    {{formatbitlbl |label=2 |value=Low Ground (Can walk under corners of buildings/units)}}
    {{formatbitlbl |label=3 |value=Low Ground (Can walk under corners of buildings/units)}}
    {{formatbitlbl |label=4 |value=Ground (Normal ground unit elevation level)}}
    {{formatbitlbl |label=5 |value=Low Air}}
    {{formatbitlbl |label=6 |value=Low Air}}
    {{formatbitlbl |label=7 |value=Low Air}}
    {{formatbitlbl |label=8 |value=Low Air}}
    {{formatbitlbl |label=9 |value=Air}}
    {{formatbitlbl |label=10 |value=Air}}
    {{formatbitlbl |label=11 |value=Air}}
    {{formatbitlbl |label=12 |value=Air}}
    {{formatbitlbl |label=13 |value=High Air}}
    {{formatbitlbl |label=14 |value=High Air}}
    {{formatbitlbl |label=15 |value=High Air}}
    {{formatbitlbl |label=16 |value=High Air}}
    {{formatbitlbl |label=17 |value=Orbital}}
    {{formatbitlbl |label=18 |value=Orbital}}
  {{end-bittable}} }}
{{end-formattable}}

## Movement Type
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x10C8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Movement type for this unit.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0 |value=None}}
    {{formatbitlbl |label=64 |value=Creep}}
    {{formatbitlbl |label=65 |value=Walk}}
    {{formatbitlbl |label=193 |value=Hover}}
    {{formatbitlbl |label=197 |value=Fly}}
  {{end-bittable}} }}
{{end-formattable}}

## StarEdit: Order/SubLabel
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x11AC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The sub-label (rank, etc) displayed in StarCraft, and the Order this unit is displayed in its folder in StarEdit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Computer AI Idle
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1290}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs when it's Idle. Used when under Computer AI control. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Human AI Idle
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1374}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs when it's Idle. Used when under Human AI control. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Unknown
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1458}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs at some unknown time. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Ground Attack
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x153C}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs when attacking Ground units. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Air Attack
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1620}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs when attacking Air units. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Weapon: Ground
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1704}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Weapon this unit uses to attack Ground units. Corresponds to entry in Weapons data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Max Hit: Ground
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x17E8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Max # of times unit hits its target per Ground attack. This value is for statistics purposes only. Changing it only effects the value displayed in StarEdit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Weapon: Air
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x18CC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Weapon this unit uses to attack Air units. Corresponds to entry in Weapons data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Max Hit: Air
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x19B0}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Max # of times unit hits its target per Air attack. This value is for statistics purposes only. Changing it only effects the value displayed in StarEdit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1A94}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Special Ability Flags
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1B78}}
  {{formatlbl |label=Length |value=912 bytes (4 bytes / Unit)}}
  {{formatlbl |label=Description |value=Special Ability Flags. Add any of these together.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00000001 |value=Building}}
    {{formatbitlbl |label=0x00000002 |value=Add-on}}
    {{formatbitlbl |label=0x00000004 |value=Flyer}}
    {{formatbitlbl |label=0x00000008 |value=Worker}}
    {{formatbitlbl |label=0x00000010 |value=Sub-Unit (Turret)}}
    {{formatbitlbl |label=0x00000020 |value=Flying Building}}
    {{formatbitlbl |label=0x00000040 |value=Hero}}
    {{formatbitlbl |label=0x00000080 |value=Regenerates HP}}
    {{formatbitlbl |label=0x00000100 |value=Animated Idle}}
    {{formatbitlbl |label=0x00000200 |value=Cloakable}}
    {{formatbitlbl |label=0x00000400 |value=2 Units in 1 Egg}}
    {{formatbitlbl |label=0x00000800 |value=Neutral accessories}}
    {{formatbitlbl |label=0x00001000 |value=Resource Depot}}
    {{formatbitlbl |label=0x00002000 |value=Contains gas}}
    {{formatbitlbl |label=0x00004000 |value=Robotic Unit}}
    {{formatbitlbl |label=0x00008000 |value=Detector}}
    {{formatbitlbl |label=0x00010000 |value=Organic unit}}
    {{formatbitlbl |label=0x00020000 |value=Creep Building}}
    {{formatbitlbl |label=0x00040000 |value=Unused}}
    {{formatbitlbl |label=0x00080000 |value=Requires PSI}}
    {{formatbitlbl |label=0x00100000 |value=Burrowable}}
    {{formatbitlbl |label=0x00200000 |value=Mana bar}}
    {{formatbitlbl |label=0x00400000 |value=Permanent cloak}}
    {{formatbitlbl |label=0x00800000 |value=NPC / accessories}}
    {{formatbitlbl |label=0x01000000 |value=Morph from other unit}}
    {{formatbitlbl |label=0x02000000 |value=Large Unit ???}}
    {{formatbitlbl |label=0x04000000 |value=Huge Unit ???}}
    {{formatbitlbl |label=0x08000000 |value=Auto attack and move}}
    {{formatbitlbl |label=0x10000000 |value=Attack}}
    {{formatbitlbl |label=0x20000000 |value=Invincible}}
    {{formatbitlbl |label=0x40000000 |value=Mechanical}}
    {{formatbitlbl |label=0x80000000 |value=Produces Units}}
  {{end-bittable}} }}
{{end-formattable}}

## Subunit (Turret) Attack Range
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1F08}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Subunit Attack Range. Only valid for units with subunits.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 255.}}
{{end-formattable}}

## Sight Range
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1FEC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Sight range for this unit.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 225 (anything above 11 crashes the game).}}
{{end-formattable}}

## Armor Upgrade Group
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x20D0}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Upgrade groups that change the Armor for this unit.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=1 |value=Terran Infantry}}
    {{formatbitlbl |label=2 |value=Terran Vehicle}}
    {{formatbitlbl |label=3 |value=Terran Air}}
    {{formatbitlbl |label=4 |value=Zerg Ground}}
    {{formatbitlbl |label=5 |value=Zerg Air}}
    {{formatbitlbl |label=6 |value=Protoss Ground}}
    {{formatbitlbl |label=7 |value=Protoss Air}}
    {{formatbitlbl |label=60 |value=None}}
  {{end-bittable}} }}
{{end-formattable}}

## Size
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x21B4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Affects damage unit is dealt when attacked.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0 |value=Undefined}}
    {{formatbitlbl |label=1 |value=Small}}
    {{formatbitlbl |label=2 |value=Medium}}
    {{formatbitlbl |label=3 |value=Large}}
  {{end-bittable}} }}
{{end-formattable}}

## Armor
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x2298}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Amount of Armor this unit has.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x237C}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Sounds
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x2460}}
  {{formatlbl |label=Length |value=3268 bytes (? bytes / Unit)}}
  {{formatlbl |label=Description |value=Unit sound section...}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Width
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x3124}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Width of the unit. Used for movement purposes.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Height
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x32EC}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Height of the unit. Used for movement purposes.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Circle Width
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x34B4}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=I thought it determined the width of the circle, but apparently it doesn't...}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Circle Height
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x367C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=I thought it determined the height of the circle, but apparently it doesn't...}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Portrait
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x3844}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines portrait displayed.}}
  {{formatlbl |label=Values |value=Value corresponds to an entry in the Portraits data file.}}
{{end-formattable}}

## Cost: Minerals
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x3A0C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines minerals required to build.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x3BD4}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines vespene gas required to build.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Cost: Build Time
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x3D9C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines time to build. Value here is in seconds.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Restrictions
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x3F64}}
  {{formatlbl |label=Length |value=456 bytes (2 byte / Unit)}}
  {{formatlbl |label=Description |value=Might determine the default Player Settings for this unit (whether it's enabled or not, etc).}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535}}
{{end-formattable}}

## StarEdit: Group Flags
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x412C}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Combinations of the values below determine the StarEdit folder the unit appears in.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x01 |value=Zerg}}
    {{formatbitlbl |label=0x02 |value=Terran}}
    {{formatbitlbl |label=0x04 |value=Protoss}}
    {{formatbitlbl |label=0x08 |value=Unit}}
    {{formatbitlbl |label=0x10 |value=Building}}
    {{formatbitlbl |label=0x20 |value=Factory}}
    {{formatbitlbl |label=0x40 |value=Independent}}
    {{formatbitlbl |label=0x80 |value=Neutral}}
  {{end-bittable}} }}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x4210}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Food Produced
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x42F4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Amount of food produced by this unit.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Cost: Food
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x43D8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Amount of food required to produce unit. Actual value is this value / 2, because the Zergling and Scourge are 2 for 1.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Transport/Bunker Space
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x44BC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Space this unit has for storing units (i.e. Bunkers and Transports).}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Score: Build
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x45A0}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Point value awarded for constructing this unit.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 65535.}}
{{end-formattable}}

## Score: Destroy
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x4768}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Point value awarded for destroying this unit.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 65535.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x4930}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Brood War Unit
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x4AF8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Flag to determine if the unit is a Brood War (Expansion) Unit or not.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0 |value=false}}
    {{formatbitlbl |label=1 |value=true}}
  {{end-bittable}} }}
{{end-formattable}}

## StarEdit: Availability Flags
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x4BDC}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines the availability of the unit in StarEdit.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0001 |value=Owned (Not Neutral)}}
    {{formatbitlbl |label=0x0002 |value=Placeable (With Map Editor or Trigger)}}
    {{formatbitlbl |label=0x0004 |value=Mission Briefing}}
    {{formatbitlbl |label=0x0008 |value=Removed from Player Settings}}
    {{formatbitlbl |label=0x0010 |value=Race Restricted}}
    {{formatbitlbl |label=0x0020 |value=Part of Terrain (Traps)}}
    {{formatbitlbl |label=0x0040 |value=Unknown}}
    {{formatbitlbl |label=0x0080 |value=Special Effect/Nuke}}
    {{formatbitlbl |label=0x0100 |value=Unknown}}
    {{formatbitlbl |label=0x0200 |value=Brood War}}
    {{formatbitlbl |label=0x0400 |value=Unknown}}
    {{formatbitlbl |label=0x0800 |value=Unknown}}
    {{formatbitlbl |label=0x1000 |value=Unknown}}
    {{formatbitlbl |label=0x2000 |value=Unknown}}
    {{formatbitlbl |label=0x4000 |value=Unknown}}
    {{formatbitlbl |label=0x8000 |value=Unknown}}
  {{end-bittable}} }}
{{end-formattable}}

