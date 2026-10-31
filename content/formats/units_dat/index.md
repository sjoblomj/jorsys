# units.dat Format

## Graphic
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Graphic of unit. Corresponds to an entry in the Images data file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Subunit 1
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x00E4}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Subunit 1 for this unit. Corresponds to another entry in this file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Subunit 2
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x02AC}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Subunit 2 for this unit. Corresponds to another entry in this file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Subunit 3
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0474}}
  {{formatlbl |label=Length |value=192 bytes (2 bytes / Unit) (First 96 Units only)}}
  {{formatlbl |label=Description |value=Subunit 3 for this unit. Corresponds to another entry in this file.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Construction Animation
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0534}}
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
  {{formathexlbl |label=Offset |value=0x08C4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 255}}
{{end-formattable}}

## Shield Enable
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x09A8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Enables shields.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0 |value=false}}
    {{formatbitlbl |label=1 |value=true}}
  {{end-bittable}} }}
{{end-formattable}}

## Shield Amount
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0A8C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Shield Amount.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535.}}
{{end-formattable}}

## Hitpoints
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0C54}}
  {{formatlbl |label=Length |value=912 bytes (4 bytes / Unit)}}
  {{formatlbl |label=Description |value=Hitpoint Amount. Lower 24 bits are the hitpoint value. The 4 high bits are unknown.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 4294967295}}
{{end-formattable}}

## Animation Level
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0FE4}}
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
  {{formathexlbl |label=Offset |value=0x10C8}}
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
  {{formathexlbl |label=Offset |value=0x11AC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=The sub-label (rank, etc) displayed in StarCraft, and the Order this unit is displayed in its folder in StarEdit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Computer AI Idle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1290}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs when it's Idle. Used when under Computer AI control. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Human AI Idle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1374}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs when it's Idle. Used when under Human AI control. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Unknown
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1458}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs at some unknown time. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Ground Attack
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x153C}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs when attacking Ground units. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Action: Air Attack
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1620}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Action/Order this unit performs when attacking Air units. Corresponds to entry in Orders data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Weapon: Ground
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1704}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Weapon this unit uses to attack Ground units. Corresponds to entry in Weapons data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Max Hit: Ground
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x17E8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Max # of times unit hits its target per Ground attack. This value is for statistics purposes only. Changing it only effects the value displayed in StarEdit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Weapon: Air
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x18CC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Weapon this unit uses to attack Air units. Corresponds to entry in Weapons data file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Max Hit: Air
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x19B0}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Max # of times unit hits its target per Air attack. This value is for statistics purposes only. Changing it only effects the value displayed in StarEdit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1A94}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Special Ability Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1B78}}
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
  {{formathexlbl |label=Offset |value=0x1F08}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Subunit Attack Range. Only valid for units with subunits.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 255.}}
{{end-formattable}}

## Sight Range
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1FEC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Sight range for this unit.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 225 (anything above 11 crashes the game).}}
{{end-formattable}}

## Armor Upgrade Group
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x20D0}}
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
  {{formathexlbl |label=Offset |value=0x21B4}}
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
  {{formathexlbl |label=Offset |value=0x2298}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Amount of Armor this unit has.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x237C}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Sounds
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2460}}
  {{formatlbl |label=Length |value=3268 bytes (? bytes / Unit)}}
  {{formatlbl |label=Description |value=Unit sound section...}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Width
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3124}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Width of the unit. Used for movement purposes.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Height
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x32EC}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Height of the unit. Used for movement purposes.}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Circle Width
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x34B4}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=I thought it determined the width of the circle, but apparently it doesn't...}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Circle Height
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x367C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=I thought it determined the height of the circle, but apparently it doesn't...}}
  {{formatlbl |label=Values |value=Integer value from 0 to 65535}}
{{end-formattable}}

## Portrait
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3844}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines portrait displayed.}}
  {{formatlbl |label=Values |value=Value corresponds to an entry in the Portraits data file.}}
{{end-formattable}}

## Cost: Minerals
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3A0C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines minerals required to build.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Cost: Vespene Gas
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3BD4}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines vespene gas required to build.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Cost: Build Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3D9C}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Determines time to build. Value here is in seconds.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535.}}
{{end-formattable}}

## Restrictions
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x3F64}}
  {{formatlbl |label=Length |value=456 bytes (2 byte / Unit)}}
  {{formatlbl |label=Description |value=Might determine the default Player Settings for this unit (whether it's enabled or not, etc).}}
  {{formatlbl |label=Values |value=Integer values between 0 and 65535}}
{{end-formattable}}

## StarEdit: Group Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x412C}}
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
  {{formathexlbl |label=Offset |value=0x4210}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Food Produced
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x42F4}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Amount of food produced by this unit.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Cost: Food
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x43D8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Amount of food required to produce unit. Actual value is this value / 2, because the Zergling and Scourge are 2 for 1.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Transport/Bunker Space
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x44BC}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Space this unit has for storing units (i.e. Bunkers and Transports).}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Score: Build
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x45A0}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Point value awarded for constructing this unit.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 65535.}}
{{end-formattable}}

## Score: Destroy
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4768}}
  {{formatlbl |label=Length |value=456 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=Point value awarded for destroying this unit.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 65535.}}
{{end-formattable}}

## Unknown
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4930}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Unknown function.}}
  {{formatlbl |label=Values |value=Integer values from 0 to 255.}}
{{end-formattable}}

## Brood War Unit
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4AF8}}
  {{formatlbl |label=Length |value=228 bytes (1 byte / Unit)}}
  {{formatlbl |label=Description |value=Flag to determine if the unit is a Brood War (Expansion) Unit or not.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0 |value=false}}
    {{formatbitlbl |label=1 |value=true}}
  {{end-bittable}} }}
{{end-formattable}}

## StarEdit: Availability Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x4BDC}}
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

---

## Appendix: Units list
{{begin-formattable}}
  {{formatlbl |label=Description |value=List of units. Most fields have one entry per unit, 228 in all (0x00 to 0xE3). Subunit 3 only has entries for the first 96 units (0x00 to 0x5F).}}
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

