# udta Format

## Graphics: Group
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=220 bytes (2 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=Graphics group this unit uses. To be honest I sort of forgot what this does :)}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Graphics: General
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x00DC}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=The graphic this unit uses in general. Most units (except the critter) specify this value as their only graphic. All buildings (and the critter) use graphics specific to tileset.}}
  {{formatlbl |label=Values |value=Bits 0 to 12 store the entry in the .war archives. There's probably a table somewhere that converts this to MPQ files.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0D |value=Flag #2}}
    {{formatbitlbl |label=0x0E |value=Flag #1}}
    {{formatbitlbl |label=0x0F |value=Repeat (used if this unit uses another's GFX)}}
  {{end-bittable}} }}
{{end-formattable}}

## Graphics: Forest
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x01DA}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=The graphic this unit uses for Forest maps.}}
  {{formatlbl |label=Values |value=Bits 0 to 12 store the entry in the .war archives. There's probably a table somewhere that converts this to MPQ files.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0D |value=Flag #2}}
    {{formatbitlbl |label=0x0E |value=Flag #1}}
    {{formatbitlbl |label=0x0F |value=Repeat (used if this unit uses another's GFX)}}
  {{end-bittable}} }}
{{end-formattable}}

## Graphics: Winter
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x02D8}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=The graphic this unit uses for Winter maps.}}
  {{formatlbl |label=Values |value=Bits 0 to 12 store the entry in the .war archives. There's probably a table somewhere that converts this to MPQ files.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0D |value=Flag #2}}
    {{formatbitlbl |label=0x0E |value=Flag #1}}
    {{formatbitlbl |label=0x0F |value=Repeat (used if this unit uses another's GFX)}}
  {{end-bittable}} }}
{{end-formattable}}

## Graphics: Wasteland
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x03D6}}
  {{formatlbl |label=Length |value=254 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=The graphic this unit uses for Wasteland maps.}}
  {{formatlbl |label=Values |value=Bits 0 to 12 store the entry in the .war archives. There's probably a table somewhere that converts this to MPQ files.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0D |value=Flag #2}}
    {{formatbitlbl |label=0x0E |value=Flag #1}}
    {{formatbitlbl |label=0x0F |value=Repeat (used if this unit uses another's GFX)}}
  {{end-bittable}} }}
{{end-formattable}}

## Range: Sight
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x04D4}}
  {{formatlbl |label=Length |value=440 bytes (1 long / First 110 Units)}}
  {{formatlbl |label=Description |value=Sight range (in tiles) of this unit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 2^32}}
{{end-formattable}}

## Hitpoints
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x068C}}
  {{formatlbl |label=Length |value=220 bytes (2 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=Hitpoints for this Unit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Magic Flag
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0768}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Flag to determine whether this unit is a spell user.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (not a magic user)}}
    {{formatbitlbl |label=0x01 |value=true (magic user)}}
  {{end-bittable}} }}
{{end-formattable}}

## Cost: Build Time
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x07D6}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Time required to build this Unit. Multiply by 6 to obtain seconds.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Cost: Gold
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0844}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=The amount of Gold required to build this Unit. Multiply by 10 to get actual value.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Cost: Lumber
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x08B2}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Amount of Lumber required to build this Unit. Multiply by 10 to obtain actual value.}}
  {{formatlbl |label=Values |value=Integer values between 0 and 255.}}
{{end-formattable}}

## Cost: Oil
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0920}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Amount of oil required to build this unit. Multiply by 10 to obtain actual value.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Size: Unit
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x098E}}
  {{formatlbl |label=Length |value=440 bytes (4 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=First two bytes are the X size (width), second two are the Y size (height).}}
  {{formatlbl |label=Values |value=Two integer values between 0 and 65535.}}
{{end-formattable}}

## Size: Box
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0B46}}
  {{formatlbl |label=Length |value=440 bytes (4 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=First two bytes are the X size (width), second two are the Y size (height).}}
  {{formatlbl |label=Values |value=Two integer values between 0 and 65535.}}
{{end-formattable}}

## Attack Range
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0CF3}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Minimum range this unit must be from its target to attack.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## React Range: Computer AI
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0D6C}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Minimum range that computer units must be from this unit in order to react to it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## React Range: Human AI
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0DDA}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Minimum range this unit must be from an enemy before it reacts to the enemy.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Armor
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0E48}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Amount of armor this unit has.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Multiselectable Flag
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0EB6}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Flag which determines whether the unit can be selected with other units.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (not multiselectable)}}
    {{formatbitlbl |label=0x01 |value=true (multiselecatble)}}
  {{end-bittable}} }}
{{end-formattable}}

## Priority / AI Treatment
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0F24}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Priority value / AI Treatment for this unit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Damage: Basic
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0F92}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Basic damage dealt by this unit when it attacks.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Damage: Piercing
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1000}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Unis)}}
  {{formatlbl |label=Description |value=Piercing damage dealt by this unit when it attacks.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Weapon Upgrade Flag
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x106E}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Flag which determines whether this unit upgrades its weapon.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (no weapon upgrade)}}
    {{formatbitlbl |label=0x01 |value=true (weapon upgrade)}}
  {{end-bittable}} }}
{{end-formattable}}

## Armor Upgrade Flag
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x10DC}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Flag which determines whether this unit upgrades its armor.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=false (no armor upgrade)}}
    {{formatbitlbl |label=0x01 |value=true (armor upgrade)}}
  {{end-bittable}} }}
{{end-formattable}}

## Weapon Missile
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x114A}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Missile type this unit uses when it attacks.}}
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
    {{formatbitlbl |label=0x0C |value=Whirlwind}}
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
    {{formatbitlbl |label=0x18 |value=Small Cannon}}
    {{formatbitlbl |label=0x19 |value=Cannon Explosion}}
    {{formatbitlbl |label=0x1A |value=Cannon Tower Explosion}}
    {{formatbitlbl |label=0x1B |value=Daemon Fire}}
    {{formatbitlbl |label=0x1C |value=Green Cross}}
    {{formatbitlbl |label=0x1D |value=None}}
  {{end-bittable}} }}
{{end-formattable}}

## Unit Type
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x11B8}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Domain unit resides in (visual only).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Land}}
    {{formatbitlbl |label=0x01 |value=Air}}
    {{formatbitlbl |label=0x02 |value=Sea}}
  {{end-bittable}} }}
{{end-formattable}}

## Decay Rate
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1226}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Rate at which this unit decays. Multiply by 6 to get seconds. Decay rates only apply to units created during the game, not those placed on the map at design time.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. 0 means the unit never decays.}}
{{end-formattable}}

## Computer Annoy Factor
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1294}}
  {{formatlbl |label=Length |value=}}
  {{formatlbl |label=Description |value=How much this unit annoys the computer (likelihood it will be attacked).}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Right Click Action
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1302}}
  {{formatlbl |label=Length |value=58 bytes (1 byte / First 58 Units)}}
  {{formatlbl |label=Description |value=Action this unit performs when you have it selected and right click with it.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=None}}
    {{formatbitlbl |label=0x01 |value=Attack}}
    {{formatbitlbl |label=0x02 |value=Move}}
    {{formatbitlbl |label=0x03 |value=Harvest}}
    {{formatbitlbl |label=0x04 |value=Haul Oil}}
    {{formatbitlbl |label=0x05 |value=Demolish}}
    {{formatbitlbl |label=0x06 |value=Sail}}
  {{end-bittable}} }}
{{end-formattable}}

## Point Value
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x133C}}
  {{formatlbl |label=Length |value=220 bytes (2 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=Point value awarded towards total score for a player which destroys this unit.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Weapon Attack Domain
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1418}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / First 110 Units)}}
  {{formatlbl |label=Description |value=Domain whose units this unit can attack.}}
  {{formatlbl |label=Values |value=(Any combination of these are valid - just add them together)}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=None}}
    {{formatbitlbl |label=0x01 |value=Land}}
    {{formatbitlbl |label=0x02 |value=Sea}}
    {{formatbitlbl |label=0x03 |value=Air}}
  {{end-bittable}} }}
{{end-formattable}}

## Unit Flags
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x1486}}
  {{formatlbl |label=Length |value=440 bytes (4 bytes / First 110 Units)}}
  {{formatlbl |label=Description |value=Flags which determine special properties this unit has.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Land Unit}}
    {{formatbitlbl |label=0x01 |value=Air Unit}}
    {{formatbitlbl |label=0x02 |value=Exploding Death}}
    {{formatbitlbl |label=0x03 |value=Sea Unit}}
    {{formatbitlbl |label=0x04 |value=Critter}}
    {{formatbitlbl |label=0x05 |value=Building}}
    {{formatbitlbl |label=0x06 |value=Submarine}}
    {{formatbitlbl |label=0x07 |value=Submarine Spotter}}
    {{formatbitlbl |label=0x08 |value=Peon}}
    {{formatbitlbl |label=0x09 |value=Tanker}}
    {{formatbitlbl |label=0x0A |value=Transport}}
    {{formatbitlbl |label=0x0B |value=Oil Platform}}
    {{formatbitlbl |label=0x0C |value=Gold Storage}}
    {{formatbitlbl |label=0x0D |value=Not used}}
    {{formatbitlbl |label=0x0E |value=Attack Ground}}
    {{formatbitlbl |label=0x0F |value=Undead}}
    {{formatbitlbl |label=0x10 |value=Shore Building}}
    {{formatbitlbl |label=0x11 |value=Spellcaster}}
    {{formatbitlbl |label=0x12 |value=Lumber Storage}}
    {{formatbitlbl |label=0x13 |value=Attacks}}
    {{formatbitlbl |label=0x14 |value=Tower}}
    {{formatbitlbl |label=0x15 |value=Oil Patch}}
    {{formatbitlbl |label=0x16 |value=Gold Mine}}
    {{formatbitlbl |label=0x17 |value=Hero}}
    {{formatbitlbl |label=0x18 |value=Oil Storage}}
    {{formatbitlbl |label=0x19 |value=Volatile}}
    {{formatbitlbl |label=0x1A |value=Mage (runs when attacked)}}
    {{formatbitlbl |label=0x1B |value=Organic}}
    {{formatbitlbl |label=0x1C |value=Not used}}
    {{formatbitlbl |label=0x1D |value=Not used}}
    {{formatbitlbl |label=0x1E |value=Not used}}
    {{formatbitlbl |label=0x1F |value=Not used}}
  {{end-bittable}} }}
{{end-formattable}}

## Graphics: Swamp
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x163E}}
  {{formatlbl |label=Length |value=252 bytes (2 bytes / Unit)}}
  {{formatlbl |label=Description |value=The graphic this unit uses for Swamp maps.}}
  {{formatlbl |label=Values |value=Bits 0 to 12 store the entry in the .war archives. There's probably a table somewhere that converts this to MPQ files.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x0D |value=Flag #2}}
    {{formatbitlbl |label=0x0E |value=Flag #1}}
    {{formatbitlbl |label=0x0F |value=Repeat (used if this unit uses another's GFX)}}
  {{end-bittable}} }}
{{end-formattable}}

