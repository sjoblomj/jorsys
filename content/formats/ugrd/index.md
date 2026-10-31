# UGRD Format

UGRD holds the data for the upgrades and spells in WarCraft II: how long each one takes to research, what it costs, its icon, and what it gives. The layout is the same in all versions. UGRD data is found in three places:

1. The default copy: entry 1 of MAINDAT.WAR in the DOS versions (1.3, 1.33 and 1.5), and the file rez\upgrades.dat in War2Dat.mpq in the Battle.net Edition (2.00 and 2.02), holds the 780 bytes in the layout below, with nothing in front of them. It is the same in all five versions, and the game uses it whenever a map does not give its own upgrade data.
2. PUD files (maps): a PUD can have a UGRD section, but it does not need one. In a PUD the section starts with 2 bytes in front of the data (not counted in the offsets here), so the section is 782 bytes. If both bytes are 0, the game reads the data that follows and uses it instead of the default copy. Otherwise the game skips the data, even though it is there, and uses the default copy. A PUD without a UGRD section also gets the default copy. In the Battle.net Edition, the game skips the UGRD section of the map in a multiplayer game unless the game type is Use Map Settings; with the other game types that come with it (Melee, Free For All, One on One, Top vs. Bottom, Ladder and Iron Man Ladder) the default copy is used.
3. Saved games (.SAV files): when the game is saved, the 780 bytes in use at that moment are written to the save file, and when the save is loaded they replace the upgrade data from the map.

Every field in this section has one entry per upgrade, 52 in all (see Appendix: Upgrade and Spell types). The game handles the entries in two ways. Entries 0 to 31 are upgrades: when one is finished, the game adds one to the player's level counter chosen by Group, and that counter is what gives the bonus. Entries 32 to 51 are spells (and the Paladin and Ogre Mage upgrades): when one is finished, its Flags are added to the spells the player knows. Which way an entry is handled is decided by the command button that starts the research, not by this data.

## Upgrade Time
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=52 bytes (1 byte / Upgrade)}}
  {{formatlbl |label=Description |value=Time it takes to research this upgrade. It uses the same unit as Cost: Build Time in the UDTA section: the game doubles both, and the building's progress goes up by one each step until it reaches that.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. Entries 34 (Holy Vision), 38 (Fireball) and 43 (Eye of Kilrogg) are 0 in the default data. These three and Death Coil (46) have no research button in the game.}}
{{end-formattable}}

## Cost: Gold
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0034}}
  {{formatlbl |label=Length |value=104 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Gold it costs to research this upgrade. Unlike the costs in the UDTA section, this is the actual amount; it is not multiplied by 10. The cost is taken when the research starts and given back if it is cancelled.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Lumber
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x009C}}
  {{formatlbl |label=Length |value=104 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Lumber it costs to research this upgrade. This is the actual amount; it is not multiplied by 10.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Cost: Oil
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0104}}
  {{formatlbl |label=Length |value=104 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Oil it costs to research this upgrade. This is the actual amount; it is not multiplied by 10. Only the ship cannon upgrades (12 to 15) cost oil in the default data.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Icon
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x016C}}
  {{formatlbl |label=Length |value=104 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Icon shown in the panel of the selected building while it is researching this upgrade. The research button itself has its own icon in the command data of the game's executable, so this does not change the button. The Battle.net Edition shows icon 108 as icon 103, so in the default data Death and Decay (108) is shown with the Death Coil icon while it is being researched.}}
  {{formatlbl |label=Values |value=Icon number, the same numbering as the icons of units and command buttons. For example 6 and 7 are the Ranger and Berserker, 10 and 11 the Paladin and Ogre Mage.}}
{{end-formattable}}

## Group
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x01D4}}
  {{formatlbl |label=Length |value=104 bytes (2 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=Only used by upgrades 0 to 31: the level counter that goes up by one for the player when the upgrade is finished. Each counter is shared by all upgrades with the same group, so for example Swords 1 and 2 both use group 1, and the research buttons show level 1 or 2 depending on the counter. The upgrade data holds no bonus amounts. When an upgrade is finished, the counter is the only thing the game changes (apart from the unit changes described under Flags); the bonus amounts are built into the game's executable, which reads the counter wherever it needs them. So what an upgrade gives depends only on its Group, not on its name, icon or place in the list: if Swords 1 had Group 2, researching it would raise the Shields counter and give the Shields bonus. Version 2.02 adds a check when upgrades 0 to 23 are started, using a counter chosen by the upgrade's place in the list rather than by its Group (0 to 3 Swords and Axes, 4 to 7 Arrows and Throwing Axes, 8 to 11 Shields, 12 to 15 Ship Cannons, 16 to 19 Ship Armor, 20 to 23 Catapults and Ballistas): the even-numbered entries can only be started while that counter is 0, and the odd-numbered ones while it is 1. So in 2.02, in the example above, Swords 2 could never be started, and neither could Human Shield 1 once Swords 1 is finished. For entries 32 to 51 the game never reads this field; in the default data it holds the number of the spell's bit in Flags.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 10 for upgrades 0 to 31. The game has only 11 counters and does not check the value, so a higher value reads past the end of its list of counters.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Arrows and Throwing Axes (upgrades 4 to 7).}}
    {{formatbitlbl |label=0x01 |value=Swords and Axes (upgrades 0 to 3).}}
    {{formatbitlbl |label=0x02 |value=Shields (upgrades 8 to 11).}}
    {{formatbitlbl |label=0x03 |value=Ship Cannons (upgrades 12 to 15).}}
    {{formatbitlbl |label=0x04 |value=Ship Armor (upgrades 16 to 19).}}
    {{formatbitlbl |label=0x05 |value=Not used by any upgrade in the default data. The game reads this counter in one place only: the "Level" number in the panel of a selected ship. Each level of this counter adds 1 to the Level shown for Transports, and for Oil Tankers, Destroyers, Battleships, Juggernaughts, Submarines and Turtles if they have the Sea Unit flag (Unit Flags bit 0x03 in UDTA). Nothing else reads it, so it gives no bonus in play. The game's executable does have a bonus amount of 10 per level for this counter in its list of upgrade bonuses, but nothing uses that amount.}}
    {{formatbitlbl |label=0x06 |value=Catapults and Ballistas (upgrades 20 to 23).}}
    {{formatbitlbl |label=0x07 |value=Ranger and Berserker Training (upgrades 24 and 28). Longbow, Scouting and Marksmanship (and the Troll equivalents) can only be researched once this counter is not 0.}}
    {{formatbitlbl |label=0x08 |value=Longbow and Lighter Axes (upgrades 25 and 29).}}
    {{formatbitlbl |label=0x09 |value=Ranger and Berserker Scouting (upgrades 26 and 30).}}
    {{formatbitlbl |label=0x0A |value=Ranger Marksmanship and Berserker Regeneration (upgrades 27 and 31).}}
  {{end-bittable}} }}
{{end-formattable}}

## Flags
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x023C}}
  {{formatlbl |label=Length |value=208 bytes (4 bytes / Upgrade)}}
  {{formatlbl |label=Description |value=The bit (or bits) this upgrade uses in the player's upgrade or spell bits, which are the same bits as in the ALOW section of PUDs: upgrades 0 to 31 use the upgrade bits, entries 32 to 51 the spell bits. When research starts, the flags are marked as being researched for the player; when it finishes or is cancelled, the mark is removed. If the mark is already gone when the research finishes, nothing happens (no level and no refund). For upgrades 0 to 31 the flags give nothing by themselves (the bonus comes from Group). The research buttons are hidden while the bit they check is being researched, but each button checks a fixed bit, not this field; in the default data upgrade 5 (Arrows 2) has 0x01 instead of 0x02, so Arrows 2 can be started in a second Lumber Mill while the first is still researching it, and the second one to finish has no effect and its cost is lost. For entries 32 to 51 the flags are added to the spells the player knows when the research finishes; a spell's cast button is only shown when its bit is known. Two values do more when the research finishes, and only when the flags are exactly that value: 0x10000 turns all the player's Archers into Rangers and Axe Throwers into Berserkers (also those being trained), and 0x100000 turns Knights into Paladins and Ogres into Ogre Mages (also those being trained) and gives the player Holy Vision and Eye of Kilrogg if those spells are allowed.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Upgrades: Arrows and Throwing Axes level 1. Spells: Holy Vision.}}
    {{formatbitlbl |label=0x01 |value=Upgrades: Arrows and Throwing Axes level 2. Spells: Healing.}}
    {{formatbitlbl |label=0x02 |value=Upgrades: Swords and Axes level 1. Spells: not used by any entry in the default data.}}
    {{formatbitlbl |label=0x03 |value=Upgrades: Swords and Axes level 2. Spells: Exorcism.}}
    {{formatbitlbl |label=0x04 |value=Upgrades: Shields level 1. Spells: Flame Shield.}}
    {{formatbitlbl |label=0x05 |value=Upgrades: Shields level 2. Spells: Fireball.}}
    {{formatbitlbl |label=0x06 |value=Upgrades: Ship Cannons level 1. Spells: Slow.}}
    {{formatbitlbl |label=0x07 |value=Upgrades: Ship Cannons level 2. Spells: Invisibility.}}
    {{formatbitlbl |label=0x08 |value=Upgrades: Ship Armor level 1. Spells: Polymorph.}}
    {{formatbitlbl |label=0x09 |value=Upgrades: Ship Armor level 2. Spells: Blizzard.}}
    {{formatbitlbl |label=0x0A |value=Upgrades: not checked by any research button. Spells: Eye of Kilrogg.}}
    {{formatbitlbl |label=0x0B |value=Upgrades: not checked by any research button. Spells: Bloodlust.}}
    {{formatbitlbl |label=0x0C |value=Upgrades: Catapults and Ballistas level 1. Spells: not used by any entry in the default data.}}
    {{formatbitlbl |label=0x0D |value=Upgrades: Catapults and Ballistas level 2. Spells: Raise Dead.}}
    {{formatbitlbl |label=0x0E |value=Upgrades: not checked by any research button. Spells: Death Coil.}}
    {{formatbitlbl |label=0x0F |value=Upgrades: not checked by any research button. Spells: Whirlwind.}}
    {{formatbitlbl |label=0x10 |value=Upgrades: Ranger and Berserker Training (exactly 0x10000 also turns Archers and Axe Throwers into Rangers and Berserkers). Spells: Haste.}}
    {{formatbitlbl |label=0x11 |value=Upgrades: Longbow and Lighter Axes. Spells: Unholy Armor.}}
    {{formatbitlbl |label=0x12 |value=Upgrades: Ranger and Berserker Scouting. Spells: Runes.}}
    {{formatbitlbl |label=0x13 |value=Upgrades: Ranger Marksmanship and Berserker Regeneration. Spells: Death and Decay.}}
    {{formatbitlbl |label=0x14 |value=Upgrades: not checked by any research button. Spells: Knights to Paladins and Ogres to Ogre Mages (exactly 0x100000 also turns the units and gives Holy Vision and Eye of Kilrogg).}}
    {{formatbitlbl |label=0x15 |value=Unused 0x15. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x16 |value=Unused 0x16. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x17 |value=Unused 0x17. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x18 |value=Unused 0x18. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x19 |value=Unused 0x19. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x1A |value=Unused 0x1A. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x1B |value=Unused 0x1B. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x1C |value=Unused 0x1C. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x1D |value=Unused 0x1D. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x1E |value=Unused 0x1E. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
    {{formatbitlbl |label=0x1F |value=Unused 0x1F. The game never tests this bit. If it is set, it is copied into the player's upgrade or spell bits like the other bits, but nothing checks it there.}}
  {{end-bittable}} }}
{{end-formattable}}

---

## Appendix: Upgrade and Spell types
{{begin-formattable}}
  {{formatlbl |label=Description |value=The upgrade and spell list. Every field in this section has one entry per upgrade, in this order. The order is the same as the upgrade names in STRDAT.WAR (rez\stat_txt.tbl in the Battle.net Edition) and the numbers in the Research command buttons of the game's executable. Entries 0x00 to 0x1F are handled as upgrades and 0x20 to 0x33 as spells (see the description of this section).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Sword 1}}
    {{formatbitlbl |label=0x01 |value=Sword 2}}
    {{formatbitlbl |label=0x02 |value=Axe 1}}
    {{formatbitlbl |label=0x03 |value=Axe 2}}
    {{formatbitlbl |label=0x04 |value=Arrow 1}}
    {{formatbitlbl |label=0x05 |value=Arrow 2}}
    {{formatbitlbl |label=0x06 |value=Throwing Axes 1 (Spear 1)}}
    {{formatbitlbl |label=0x07 |value=Throwing Axes 2 (Spear 2)}}
    {{formatbitlbl |label=0x08 |value=Human Shield 1}}
    {{formatbitlbl |label=0x09 |value=Human Shield 2}}
    {{formatbitlbl |label=0x0A |value=Orc Shield 1}}
    {{formatbitlbl |label=0x0B |value=Orc Shield 2}}
    {{formatbitlbl |label=0x0C |value=Human Ship Cannon 1}}
    {{formatbitlbl |label=0x0D |value=Human Ship Cannon 2}}
    {{formatbitlbl |label=0x0E |value=Orc Ship Cannon 1}}
    {{formatbitlbl |label=0x0F |value=Orc Ship Cannon 2}}
    {{formatbitlbl |label=0x10 |value=Human Ship Armor 1}}
    {{formatbitlbl |label=0x11 |value=Human Ship Armor 2}}
    {{formatbitlbl |label=0x12 |value=Orc Ship Armor 1}}
    {{formatbitlbl |label=0x13 |value=Orc Ship Armor 2}}
    {{formatbitlbl |label=0x14 |value=Catapult 1}}
    {{formatbitlbl |label=0x15 |value=Catapult 2}}
    {{formatbitlbl |label=0x16 |value=Ballista 1}}
    {{formatbitlbl |label=0x17 |value=Ballista 2}}
    {{formatbitlbl |label=0x18 |value=Elven Ranger Training}}
    {{formatbitlbl |label=0x19 |value=Longbow}}
    {{formatbitlbl |label=0x1A |value=Ranger Scouting}}
    {{formatbitlbl |label=0x1B |value=Ranger Marksmanship}}
    {{formatbitlbl |label=0x1C |value=Troll Berserker Training}}
    {{formatbitlbl |label=0x1D |value=Lighter Axes}}
    {{formatbitlbl |label=0x1E |value=Berserker Scouting}}
    {{formatbitlbl |label=0x1F |value=Berserker Regeneration}}
    {{formatbitlbl |label=0x20 |value=Upgrade Ogres to Ogre-Mages}}
    {{formatbitlbl |label=0x21 |value=Upgrade Knights to Paladins}}
    {{formatbitlbl |label=0x22 |value=Holy Vision}}
    {{formatbitlbl |label=0x23 |value=Healing}}
    {{formatbitlbl |label=0x24 |value=Exorcism}}
    {{formatbitlbl |label=0x25 |value=Flame Shield}}
    {{formatbitlbl |label=0x26 |value=Fireball}}
    {{formatbitlbl |label=0x27 |value=Slow}}
    {{formatbitlbl |label=0x28 |value=Invisibility}}
    {{formatbitlbl |label=0x29 |value=Polymorph}}
    {{formatbitlbl |label=0x2A |value=Blizzard}}
    {{formatbitlbl |label=0x2B |value=Eye of Kilrogg}}
    {{formatbitlbl |label=0x2C |value=Bloodlust}}
    {{formatbitlbl |label=0x2D |value=Raise Dead}}
    {{formatbitlbl |label=0x2E |value=Death Coil}}
    {{formatbitlbl |label=0x2F |value=Whirlwind}}
    {{formatbitlbl |label=0x30 |value=Haste}}
    {{formatbitlbl |label=0x31 |value=Unholy Armor}}
    {{formatbitlbl |label=0x32 |value=Runes}}
    {{formatbitlbl |label=0x33 |value=Death and Decay}}
  {{end-bittable}} }}
{{end-formattable}}

