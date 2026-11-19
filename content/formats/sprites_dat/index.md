# sprites.dat Format

sprites.dat holds the data of every sprite: the object on the map that carries a unit's, bullet's or doodad's images. Each entry gives the sprite's first image, whether it starts visible, and, for units, the size of its health bar and its selection circle. It is the file arr\sprites.dat in the game's MPQ archives and is 3229 bytes long. Each field below is a list, and the lists are stored one after another with nothing in between, so the offsets are from the start of the file. Sprites 0 to 129 are doodads that are part of the tileset, which never have a health bar or a selection circle, so three of the fields only have entries for sprites 130 to 516 (387 entries). The game reads those three fields at the sprite number minus 130; a doodad sprite given to a unit would read the end of the field before. StarEdit also reads the file (all fields except Health Bar). The layout is the same in every version from 1.04 to 1.17, of both StarCraft and Brood War. StarCraft 1.00 to 1.03 used an older layout with 386 entries (2081 bytes); the older file is still in StarDat.mpq in later versions but is never loaded, because the copy in BrooDat.mpq (or patch_rt.mpq) is found first. The game loads the file again each time a game starts. Fields are read in order, and the game stops with a file error if the file is longer than the layout. A shorter file that ends exactly where a field ends loads without an error; the fields after the end then keep whatever they held before. No field is checked when the game uses it, so an out-of-range value reads whatever follows the table it points into.

## Image
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=1034 bytes (2 bytes / Sprite)}}
  {{formatlbl |label=Description |value=The images.dat entry of the sprite's main image, created with the sprite. Its animation script may add further images.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 998.}}
{{end-formattable}}

## Health Bar
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x040A}}
  {{formatlbl |label=Length |value=387 bytes (1 byte / Sprites 130 to 516)}}
  {{formatlbl |label=Description |value=Width of the health bar in pixels. The bar is drawn in 3-pixel boxes, so the width is rounded down to 3n + 1, and it is at least 19. Its height comes from the unit (taller with shields and energy). 0 is used for sprites without a bar.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255.}}
{{end-formattable}}

## Unused
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x058D}}
  {{formatlbl |label=Length |value=517 bytes (1 byte / Sprite)}}
  {{formatlbl |label=Description |value=Not used: no code in StarCraft or StarEdit reads this field, in any version from 1.04 to 1.17. In the shipped file it is 1 for the sprites of units, their remains and buildings, and 0 for the rest.}}
  {{formatlbl |label=Values |value=Any value; ignored.}}
{{end-formattable}}

## Visible
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0792}}
  {{formatlbl |label=Length |value=517 bytes (1 byte / Sprite)}}
  {{formatlbl |label=Description |value=0 makes the sprite start hidden and seen by no player, until other code shows it. Only the Scanner Sweep's sprite, circle14 and the Subterranean Spines hit sprite have 0.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Starts hidden}}
    {{formatbitlbl |label=0x01 and up |value=Starts visible}}
  {{end-bittable}} }}
{{end-formattable}}

## Selection Circle
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0997}}
  {{formatlbl |label=Length |value=387 bytes (1 byte / Sprites 130 to 516)}}
  {{formatlbl |label=Description |value=Size of the selection circle: images.dat entry 561 + the value is the circle around your own units (22, 32, 48, 62, 72, 94, 110, 122, 146 and 224 pixels wide for 0 to 9), and 571 + the value the dashed circle around other players' units. The health bar is placed using the height of the circle image.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 9 (higher values pick whatever images follow).}}
{{end-formattable}}

## Selection Circle Offset
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0B1A}}
  {{formatlbl |label=Length |value=387 bytes (1 byte / Sprites 130 to 516)}}
  {{formatlbl |label=Description |value=How far below the sprite's position the selection circle is drawn, in pixels. It is a signed byte, so 128 to 255 move the circle up (255 is one pixel up). The health bar goes 8 pixels below the circle.}}
  {{formatlbl |label=Values |value=Integer value between −128 and 127, stored as a byte.}}
{{end-formattable}}

---

## Appendix: Sprites list
{{begin-formattable}}
  {{formatlbl |label=Description |value=Every sprite, with the units that use it (through flingy.dat), its image and that image's GRP file (from arr\images.tbl). Sprites 0 to 129 are tileset doodads. All taken from the shipped data files.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x000 |value=image 589, thingy\tileset\AshWorld\rock01.grp}}
    {{formatbitlbl |label=0x001 |value=image 591, thingy\tileset\AshWorld\rock02.grp}}
    {{formatbitlbl |label=0x002 |value=image 593, thingy\tileset\AshWorld\rock03.grp}}
    {{formatbitlbl |label=0x003 |value=image 595, thingy\tileset\AshWorld\rock04.grp}}
    {{formatbitlbl |label=0x004 |value=image 597, thingy\tileset\AshWorld\rock05.grp}}
    {{formatbitlbl |label=0x005 |value=image 599, thingy\tileset\AshWorld\LALRoc01.grp}}
    {{formatbitlbl |label=0x006 |value=image 600, thingy\tileset\AshWorld\LALRoc02.grp}}
    {{formatbitlbl |label=0x007 |value=image 601, thingy\tileset\AshWorld\HASRoc01.grp}}
    {{formatbitlbl |label=0x008 |value=image 602, thingy\tileset\AshWorld\HASRoc02.grp}}
    {{formatbitlbl |label=0x009 |value=image 603, thingy\tileset\AshWorld\HASRoc03.grp}}
    {{formatbitlbl |label=0x00A |value=image 604, thingy\tileset\AshWorld\HASRoc04.grp}}
    {{formatbitlbl |label=0x00B |value=image 605, thingy\tileset\AshWorld\HASRoc05.grp}}
    {{formatbitlbl |label=0x00C |value=image 606, thingy\tileset\AshWorld\HASRoc06.grp}}
    {{formatbitlbl |label=0x00D |value=image 607, thingy\tileset\AshWorld\RORock01.grp}}
    {{formatbitlbl |label=0x00E |value=image 608, thingy\tileset\AshWorld\RORock02.grp}}
    {{formatbitlbl |label=0x00F |value=image 609, thingy\tileset\AshWorld\RORock03.grp}}
    {{formatbitlbl |label=0x010 |value=image 610, thingy\tileset\Jungle\HDRock01.grp}}
    {{formatbitlbl |label=0x011 |value=image 612, thingy\tileset\Jungle\HDRock02.grp}}
    {{formatbitlbl |label=0x012 |value=image 614, thingy\tileset\Jungle\HDRock03.grp}}
    {{formatbitlbl |label=0x013 |value=image 616, thingy\tileset\Jungle\HDRock04.grp}}
    {{formatbitlbl |label=0x014 |value=image 618, thingy\tileset\Jungle\JUbush01.grp}}
    {{formatbitlbl |label=0x015 |value=image 620, thingy\tileset\Jungle\JUbush03.grp}}
    {{formatbitlbl |label=0x016 |value=image 622, thingy\tileset\Jungle\JUbush05.grp}}
    {{formatbitlbl |label=0x017 |value=image 624, thingy\tileset\Jungle\LDtree01.grp}}
    {{formatbitlbl |label=0x018 |value=image 626, thingy\tileset\Jungle\LDtree02.grp}}
    {{formatbitlbl |label=0x019 |value=image 628, thingy\tileset\Jungle\LDtree03.grp}}
    {{formatbitlbl |label=0x01A |value=image 630, thingy\tileset\Jungle\LDtree04.grp}}
    {{formatbitlbl |label=0x01B |value=image 632, thingy\tileset\Jungle\tree01.grp}}
    {{formatbitlbl |label=0x01C |value=image 634, thingy\tileset\Jungle\tree02.grp}}
    {{formatbitlbl |label=0x01D |value=image 636, thingy\tileset\Jungle\tree03.grp}}
    {{formatbitlbl |label=0x01E |value=image 638, thingy\tileset\Jungle\tree04.grp}}
    {{formatbitlbl |label=0x01F |value=image 640, thingy\tileset\Jungle\dd025.grp}}
    {{formatbitlbl |label=0x020 |value=image 641, thingy\tileset\Jungle\dd026.grp}}
    {{formatbitlbl |label=0x021 |value=image 642, thingy\tileset\Jungle\dd027.grp}}
    {{formatbitlbl |label=0x022 |value=image 643, thingy\tileset\Jungle\dd028.grp}}
    {{formatbitlbl |label=0x023 |value=image 644, thingy\tileset\Jungle\dd029.grp}}
    {{formatbitlbl |label=0x024 |value=image 645, thingy\tileset\Jungle\dd030.grp}}
    {{formatbitlbl |label=0x025 |value=image 646, thingy\tileset\Jungle\dd031.grp}}
    {{formatbitlbl |label=0x026 |value=image 647, thingy\tileset\Jungle\dd055.grp}}
    {{formatbitlbl |label=0x027 |value=image 648, thingy\tileset\Jungle\dd056.grp}}
    {{formatbitlbl |label=0x028 |value=image 649, thingy\tileset\Jungle\dd075.grp}}
    {{formatbitlbl |label=0x029 |value=image 650, thingy\tileset\Jungle\dd076.grp}}
    {{formatbitlbl |label=0x02A |value=image 651, thingy\tileset\Jungle\dd077.grp}}
    {{formatbitlbl |label=0x02B |value=image 652, thingy\tileset\Jungle\dd078.grp}}
    {{formatbitlbl |label=0x02C |value=image 653, thingy\tileset\Jungle\dd079.grp}}
    {{formatbitlbl |label=0x02D |value=image 654, thingy\tileset\Jungle\dd080.grp}}
    {{formatbitlbl |label=0x02E |value=image 655, thingy\tileset\Jungle\dd081.grp}}
    {{formatbitlbl |label=0x02F |value=image 656, thingy\tileset\Jungle\dd091.grp}}
    {{formatbitlbl |label=0x030 |value=image 657, thingy\tileset\Jungle\dd203.grp}}
    {{formatbitlbl |label=0x031 |value=image 658, thingy\tileset\Jungle\dd204.grp}}
    {{formatbitlbl |label=0x032 |value=image 659, thingy\tileset\Jungle\dd205.grp}}
    {{formatbitlbl |label=0x033 |value=image 660, thingy\tileset\Jungle\dd206.grp}}
    {{formatbitlbl |label=0x034 |value=image 661, thingy\tileset\Jungle\dd207.grp}}
    {{formatbitlbl |label=0x035 |value=image 662, thingy\tileset\Jungle\dd209.grp}}
    {{formatbitlbl |label=0x036 |value=image 663, thingy\tileset\Jungle\dd210.grp}}
    {{formatbitlbl |label=0x037 |value=image 664, thingy\tileset\Jungle\dd211.grp}}
    {{formatbitlbl |label=0x038 |value=image 665, thingy\tileset\Platform\Dish01.grp}}
    {{formatbitlbl |label=0x039 |value=image 667, thingy\tileset\Platform\Dish02.grp}}
    {{formatbitlbl |label=0x03A |value=image 669, thingy\tileset\Platform\Dish03.grp}}
    {{formatbitlbl |label=0x03B |value=image 671, thingy\tileset\Platform\Glob01.grp}}
    {{formatbitlbl |label=0x03C |value=image 673, thingy\tileset\Platform\Glob02.grp}}
    {{formatbitlbl |label=0x03D |value=image 675, thingy\tileset\Platform\Glob03.grp}}
    {{formatbitlbl |label=0x03E |value=image 677, thingy\tileset\Platform\Towr01.grp}}
    {{formatbitlbl |label=0x03F |value=image 678, thingy\tileset\Platform\Towr02.grp}}
    {{formatbitlbl |label=0x040 |value=image 679, thingy\tileset\Platform\tree01.grp}}
    {{formatbitlbl |label=0x041 |value=image 680, thingy\tileset\Platform\tree02.grp}}
    {{formatbitlbl |label=0x042 |value=image 681, thingy\tileset\Platform\LBSign01.grp}}
    {{formatbitlbl |label=0x043 |value=image 682, thingy\tileset\Platform\LBSign02.grp}}
    {{formatbitlbl |label=0x044 |value=image 683, thingy\tileset\Platform\LBSign03.grp}}
    {{formatbitlbl |label=0x045 |value=image 684, thingy\tileset\Platform\LBSign04.grp}}
    {{formatbitlbl |label=0x046 |value=image 685, thingy\tileset\Platform\LBSign05.grp}}
    {{formatbitlbl |label=0x047 |value=image 686, thingy\tileset\Platform\LBSign06.grp}}
    {{formatbitlbl |label=0x048 |value=image 687, thingy\tileset\Platform\LBSign07.grp}}
    {{formatbitlbl |label=0x049 |value=image 688, thingy\tileset\Platform\LBSign08.grp}}
    {{formatbitlbl |label=0x04A |value=image 689, thingy\tileset\Platform\SPThin01.grp}}
    {{formatbitlbl |label=0x04B |value=image 690, thingy\tileset\Platform\refinery.grp}}
    {{formatbitlbl |label=0x04C |value=image 691, thingy\tileset\Badlands\HDRock01.grp}}
    {{formatbitlbl |label=0x04D |value=image 693, thingy\tileset\Badlands\HDRock02.grp}}
    {{formatbitlbl |label=0x04E |value=image 695, thingy\tileset\Badlands\HDRock03.grp}}
    {{formatbitlbl |label=0x04F |value=image 697, thingy\tileset\Badlands\HDRock04.grp}}
    {{formatbitlbl |label=0x050 |value=image 699, thingy\tileset\Badlands\HDRock05.grp}}
    {{formatbitlbl |label=0x051 |value=image 700, thingy\tileset\Badlands\HDRock06.grp}}
    {{formatbitlbl |label=0x052 |value=image 701, thingy\tileset\Badlands\HDRock07.grp}}
    {{formatbitlbl |label=0x053 |value=image 702, thingy\tileset\Badlands\HDRock08.grp}}
    {{formatbitlbl |label=0x054 |value=image 703, thingy\tileset\Badlands\HDVent01.grp}}
    {{formatbitlbl |label=0x055 |value=image 704, thingy\tileset\Badlands\HDTree01.grp}}
    {{formatbitlbl |label=0x056 |value=image 706, thingy\tileset\Badlands\HDTree02.grp}}
    {{formatbitlbl |label=0x057 |value=image 708, thingy\tileset\Badlands\HDTree03.grp}}
    {{formatbitlbl |label=0x058 |value=image 710, thingy\tileset\Badlands\HDTree04.grp}}
    {{formatbitlbl |label=0x059 |value=image 712, thingy\tileset\Badlands\HGTree01.grp}}
    {{formatbitlbl |label=0x05A |value=image 713, thingy\tileset\Badlands\LCShop01.grp}}
    {{formatbitlbl |label=0x05B |value=image 714, thingy\tileset\Badlands\LCShop02.grp}}
    {{formatbitlbl |label=0x05C |value=image 715, thingy\tileset\Badlands\LCShop03.grp}}
    {{formatbitlbl |label=0x05D |value=image 716, thingy\tileset\Badlands\LCShop04.grp}}
    {{formatbitlbl |label=0x05E |value=image 717, thingy\tileset\Badlands\LCShop05.grp}}
    {{formatbitlbl |label=0x05F |value=image 718, thingy\tileset\Badlands\LCShop06.grp}}
    {{formatbitlbl |label=0x060 |value=image 719, thingy\tileset\Badlands\LCShop07.grp}}
    {{formatbitlbl |label=0x061 |value=image 720, thingy\tileset\Badlands\LCShop08.grp}}
    {{formatbitlbl |label=0x062 |value=image 721, thingy\tileset\Badlands\LCShop09.grp}}
    {{formatbitlbl |label=0x063 |value=image 722, thingy\tileset\Badlands\LCShopAA.grp}}
    {{formatbitlbl |label=0x064 |value=image 723, thingy\tileset\Badlands\LCSign01.grp}}
    {{formatbitlbl |label=0x065 |value=image 724, thingy\tileset\Badlands\LCSign02.grp}}
    {{formatbitlbl |label=0x066 |value=image 725, thingy\tileset\Badlands\LCSign03.grp}}
    {{formatbitlbl |label=0x067 |value=image 726, thingy\tileset\Badlands\LCSign04.grp}}
    {{formatbitlbl |label=0x068 |value=image 727, thingy\tileset\Badlands\LCSign05.grp}}
    {{formatbitlbl |label=0x069 |value=image 728, thingy\tileset\Badlands\LCSign06.grp}}
    {{formatbitlbl |label=0x06A |value=image 729, thingy\tileset\Badlands\LCSign07.grp}}
    {{formatbitlbl |label=0x06B |value=image 730, thingy\tileset\Badlands\LCSign08.grp}}
    {{formatbitlbl |label=0x06C |value=image 731, thingy\tileset\Badlands\LCSign09.grp}}
    {{formatbitlbl |label=0x06D |value=image 732, thingy\tileset\Badlands\LCSignAA.grp}}
    {{formatbitlbl |label=0x06E |value=image 733, thingy\tileset\Badlands\LCSignBB.grp}}
    {{formatbitlbl |label=0x06F |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x070 |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x071 |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x072 |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x073 |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x074 |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x075 |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x076 |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x077 |value=image 744, thingy\tileset\install\DCFan1.grp}}
    {{formatbitlbl |label=0x078 |value=image 745, thingy\tileset\install\DCFan1.grp}}
    {{formatbitlbl |label=0x079 |value=image 746, thingy\tileset\install\DICran1.grp}}
    {{formatbitlbl |label=0x07A |value=image 747, thingy\tileset\install\DICran2.grp}}
    {{formatbitlbl |label=0x07B |value=image 748, thingy\tileset\install\DICran3.grp}}
    {{formatbitlbl |label=0x07C |value=image 749, thingy\tileset\install\DICran4.grp}}
    {{formatbitlbl |label=0x07D |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x07E |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x07F |value=image 752, thingy\tileset\install\DIGear1.grp}}
    {{formatbitlbl |label=0x080 |value=image 753, thingy\tileset\install\DIGear2.grp}}
    {{formatbitlbl |label=0x081 |value=image 734, thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x082 |value=Zerg Scourge; image 0, zerg\avenger.grp}}
    {{formatbitlbl |label=0x083 |value=image 3, zerg\zavDeath.grp}}
    {{formatbitlbl |label=0x084 |value=image 4, zerg\zavExplo.grp}}
    {{formatbitlbl |label=0x085 |value=Zerg Broodling; image 5, zerg\brood.grp}}
    {{formatbitlbl |label=0x086 |value=image 7, zerg\zbrDeath.grp}}
    {{formatbitlbl |label=0x087 |value=Infested Terran; image 8, zerg\bugguy.grp}}
    {{formatbitlbl |label=0x088 |value=image 10, thingy\zbgExplo.grp}}
    {{formatbitlbl |label=0x089 |value=Mutalisk Cocoon; image 11, zerg\cocoon.grp}}
    {{formatbitlbl |label=0x08A |value=Zerg Defiler, Unclean One (Defiler); image 13, zerg\defiler.grp}}
    {{formatbitlbl |label=0x08B |value=image 16, zerg\zdeDeath.grp}}
    {{formatbitlbl |label=0x08C |value=Zerg Drone; image 17, zerg\drone.grp}}
    {{formatbitlbl |label=0x08D |value=image 20, zerg\zdrDeath.grp}}
    {{formatbitlbl |label=0x08E |value=Zerg Egg; image 21, zerg\egg.grp}}
    {{formatbitlbl |label=0x08F |value=image 24, zerg\zegDeath.grp}}
    {{formatbitlbl |label=0x090 |value=Zerg Guardian, Kukulza (Guardian); image 25, zerg\guardian.grp}}
    {{formatbitlbl |label=0x091 |value=image 28, zerg\zguDeath.grp}}
    {{formatbitlbl |label=0x092 |value=Zerg Hydralisk, Hunter Killer (Hydralisk); image 29, zerg\hydra.grp}}
    {{formatbitlbl |label=0x093 |value=image 32, zerg\zhyDeath.grp}}
    {{formatbitlbl |label=0x094 |value=Infested Kerrigan (Infested Terran); image 33, zerg\uikerr.grp}}
    {{formatbitlbl |label=0x095 |value=Zerg Larva; image 36, zerg\larva.grp}}
    {{formatbitlbl |label=0x096 |value=image 37, zerg\zlaDeath.grp}}
    {{formatbitlbl |label=0x097 |value=Zerg Mutalisk, Kukulza (Mutalisk); image 38, zerg\mutalid.grp}}
    {{formatbitlbl |label=0x098 |value=image 41, zerg\zmuDeath.grp}}
    {{formatbitlbl |label=0x099 |value=Zerg Overlord, Yggdrasill (Overlord); image 42, zerg\overlord.grp}}
    {{formatbitlbl |label=0x09A |value=image 45, zerg\zovDeath.grp}}
    {{formatbitlbl |label=0x09B |value=Zerg Queen, Matriarch (Queen); image 46, zerg\queen.grp}}
    {{formatbitlbl |label=0x09C |value=image 48, zerg\zquDeath.grp}}
    {{formatbitlbl |label=0x09D |value=Zerg Ultralisk, Torrasque (Ultralisk); image 50, zerg\ultra.grp}}
    {{formatbitlbl |label=0x09E |value=image 53, zerg\zulDeath.grp}}
    {{formatbitlbl |label=0x09F |value=Zerg Zergling, Devouring One (Zergling); image 54, zerg\zergling.grp}}
    {{formatbitlbl |label=0x0A0 |value=image 57, zerg\zzeDeath.grp}}
    {{formatbitlbl |label=0x0A1 |value=Zerg Cerebrate, Zerg Cerebrate Daggoth; image 61, zerg\UCereb.grp}}
    {{formatbitlbl |label=0x0A2 |value=Infested Command Center; image 63, terran\control.grp}}
    {{formatbitlbl |label=0x0A3 |value=Zerg Spawning Pool; image 64, zerg\chrysal.grp}}
    {{formatbitlbl |label=0x0A4 |value=Mature Chrysalis; image 78, neutral\kerrChry.grp}}
    {{formatbitlbl |label=0x0A5 |value=Zerg Evolution Chamber; image 66, zerg\cerebrat.grp}}
    {{formatbitlbl |label=0x0A6 |value=Zerg Creep Colony; image 68, zerg\fcolony.grp}}
    {{formatbitlbl |label=0x0A7 |value=Zerg Hatchery; image 70, zerg\hatchery.grp}}
    {{formatbitlbl |label=0x0A8 |value=Zerg Hive; image 72, Zerg\Hive.grp}}
    {{formatbitlbl |label=0x0A9 |value=Zerg Lair; image 74, zerg\Lair.grp}}
    {{formatbitlbl |label=0x0AA |value=Zerg Sunken Colony; image 76, zerg\Lurker.grp}}
    {{formatbitlbl |label=0x0AB |value=Zerg Greater Spire; image 80, zerg\MutaCham.grp}}
    {{formatbitlbl |label=0x0AC |value=Zerg Defiler Mound; image 82, zerg\Mutapit.grp}}
    {{formatbitlbl |label=0x0AD |value=Zerg Queen's Nest; image 84, zerg\nest.grp}}
    {{formatbitlbl |label=0x0AE |value=Zerg Nydus Canal; image 86, zerg\NydusPit.grp}}
    {{formatbitlbl |label=0x0AF |value=Zerg Overmind (With Shell); image 88, zerg\Over1.grp}}
    {{formatbitlbl |label=0x0B0 |value=Zerg Overmind; image 90, zerg\Over2.grp}}
    {{formatbitlbl |label=0x0B1 |value=Zerg Ultralisk Cavern; image 91, zerg\RCluster.grp}}
    {{formatbitlbl |label=0x0B2 |value=Zerg Extractor; image 93, zerg\Extract.grp}}
    {{formatbitlbl |label=0x0B3 |value=Zerg Hydralisk Den; image 95, zerg\Snakey.grp}}
    {{formatbitlbl |label=0x0B4 |value=Zerg Spire; image 97, zerg\spire.grp}}
    {{formatbitlbl |label=0x0B5 |value=Zerg Spore Colony; image 99, zerg\SColony.grp}}
    {{formatbitlbl |label=0x0B6 |value=image 107, zerg\zSpawn01.grp}}
    {{formatbitlbl |label=0x0B7 |value=image 108, zerg\zSpawn02.grp}}
    {{formatbitlbl |label=0x0B8 |value=image 109, zerg\zSpawn03.grp}}
    {{formatbitlbl |label=0x0B9 |value=image 60, thingy\zBldDthS.grp}}
    {{formatbitlbl |label=0x0BA |value=image 110, thingy\ZRubbleS.grp}}
    {{formatbitlbl |label=0x0BB |value=image 111, thingy\ZRubbleL.grp}}
    {{formatbitlbl |label=0x0BC |value=Protoss Arbiter, Danimoth (Arbiter); image 130, protoss\arbiter.grp}}
    {{formatbitlbl |label=0x0BD |value=Protoss Archon, Tassadar/Zeratul (Archon); image 134, protoss\archon.grp}}
    {{formatbitlbl |label=0x0BE |value=Protoss Carrier, Gantrithor (Carrier); image 112, protoss\carrier.grp}}
    {{formatbitlbl |label=0x0BF |value=Protoss Dragoon, Fenix (Dragoon); image 122, protoss\dragoon.grp}}
    {{formatbitlbl |label=0x0C0 |value=image 124, protoss\pdrDeath.grp}}
    {{formatbitlbl |label=0x0C1 |value=Protoss Interceptor; image 116, protoss\Intercep.grp}}
    {{formatbitlbl |label=0x0C2 |value=Protoss Probe; image 137, protoss\probe.grp}}
    {{formatbitlbl |label=0x0C3 |value=Protoss Scout, Mojo (Scout), Artanis (Scout), …; image 140, protoss\scout.grp}}
    {{formatbitlbl |label=0x0C4 |value=Protoss Shuttle; image 118, protoss\shuttle.grp}}
    {{formatbitlbl |label=0x0C5 |value=Protoss High Templar, Tassadar (Templar), Aldaris (Templar); image 126, protoss\templar.grp}}
    {{formatbitlbl |label=0x0C6 |value=Protoss Dark Templar (Hero), Zeratul (Dark Templar); image 129, protoss\dtemplar.grp}}
    {{formatbitlbl |label=0x0C7 |value=Warbringer (Reaver), Protoss Reaver; image 144, protoss\trilob.grp}}
    {{formatbitlbl |label=0x0C8 |value=Protoss Scarab; image 147, protoss\sapper.grp}}
    {{formatbitlbl |label=0x0C9 |value=Protoss Zealot, Fenix (Zealot); image 151, protoss\zealot.grp}}
    {{formatbitlbl |label=0x0CA |value=Protoss Observer; image 148, protoss\witness.grp}}
    {{formatbitlbl |label=0x0CB |value=Protoss Templar Archives; image 155, protoss\archives.grp}}
    {{formatbitlbl |label=0x0CC |value=Protoss Assimilator; image 158, protoss\assim.grp}}
    {{formatbitlbl |label=0x0CD |value=Protoss Observatory; image 161, protoss\beacon.grp}}
    {{formatbitlbl |label=0x0CE |value=Protoss Citadel of Adun; image 164, protoss\citadel.grp}}
    {{formatbitlbl |label=0x0CF |value=Protoss Forge; image 167, protoss\forge.grp}}
    {{formatbitlbl |label=0x0D0 |value=Protoss Gateway; image 171, protoss\gateway.grp}}
    {{formatbitlbl |label=0x0D1 |value=Protoss Cybernetics Core; image 174, protoss\gencore.grp}}
    {{formatbitlbl |label=0x0D2 |value=Khaydarin Crystal Formation; image 178, neutral\Khyad01.grp}}
    {{formatbitlbl |label=0x0D3 |value=Protoss Nexus; image 179, protoss\nexus.grp}}
    {{formatbitlbl |label=0x0D4 |value=Protoss Photon Cannon; image 183, protoss\photon.grp}}
    {{formatbitlbl |label=0x0D5 |value=Protoss Arbiter Tribunal; image 186, protoss\prism.grp}}
    {{formatbitlbl |label=0x0D6 |value=Protoss Pylon; image 189, protoss\pylon.grp}}
    {{formatbitlbl |label=0x0D7 |value=Protoss Robotics Facility; image 192, protoss\robotic.grp}}
    {{formatbitlbl |label=0x0D8 |value=Protoss Shield Battery; image 195, protoss\sbattery.grp}}
    {{formatbitlbl |label=0x0D9 |value=Protoss Stargate; image 199, protoss\stargate.grp}}
    {{formatbitlbl |label=0x0DA |value=Stasis Cell/Prison; image 203, neutral\stasis.grp}}
    {{formatbitlbl |label=0x0DB |value=Protoss Robotics Support Bay; image 204, protoss\stasis.grp}}
    {{formatbitlbl |label=0x0DC |value=Protoss Temple; image 207, neutral\temple.grp}}
    {{formatbitlbl |label=0x0DD |value=Protoss Fleet Beacon; image 208, protoss\warp.grp}}
    {{formatbitlbl |label=0x0DE |value=image 215, thingy\tBangX.grp}}
    {{formatbitlbl |label=0x0DF |value=image 216, thingy\PRubbleS.grp}}
    {{formatbitlbl |label=0x0E0 |value=image 217, thingy\PRubbleL.grp}}
    {{formatbitlbl |label=0x0E1 |value=Terran Battlecruiser, Arcturus Mengsk (Battlecruiser), Hyperion (Battlecruiser), …; image 218, terran\BattleCr.grp}}
    {{formatbitlbl |label=0x0E2 |value=Terran Civilian; image 221, neutral\civilian.grp}}
    {{formatbitlbl |label=0x0E3 |value=Terran Dropship; image 223, terran\dropship.grp}}
    {{formatbitlbl |label=0x0E4 |value=Gui Montag (Firebat), Terran Firebat; image 226, terran\firebat.grp}}
    {{formatbitlbl |label=0x0E5 |value=Terran Ghost, Samir Duran (Ghost), Alexei Stukov (Ghost), …; image 228, terran\ghost.grp}}
    {{formatbitlbl |label=0x0E6 |value=image 230, terran\tghDeath.grp}}
    {{formatbitlbl |label=0x0E7 |value=image 233, thingy\NukeTarg.grp}}
    {{formatbitlbl |label=0x0E8 |value=Terran Goliath, Alan Schezar (Goliath); image 234, terran\goliath.grp}}
    {{formatbitlbl |label=0x0E9 |value=Goliath Turret, Alan Schezar Turret; image 235, terran\goliathT.grp}}
    {{formatbitlbl |label=0x0EA |value=Sarah Kerrigan (Ghost); image 237, terran\ughost.grp}}
    {{formatbitlbl |label=0x0EB |value=Terran Marine, Jim Raynor (Marine); image 239, terran\marine.grp}}
    {{formatbitlbl |label=0x0EC |value=image 241, terran\tmaDeath.grp}}
    {{formatbitlbl |label=0x0ED |value=Scanner Sweep; image 246, terran\marine.grp}}
    {{formatbitlbl |label=0x0EE |value=Terran Wraith, Tom Kazansky (Wraith); image 243, terran\phoenix.grp}}
    {{formatbitlbl |label=0x0EF |value=Terran SCV; image 247, terran\SCV.grp}}
    {{formatbitlbl |label=0x0F0 |value=Terran Siege Tank (Tank Mode), Edmund Duke (Tank Mode); image 250, terran\tank.grp}}
    {{formatbitlbl |label=0x0F1 |value=Siege Tank Turret (Tank Mode), Edmund Duke Turret (Tank Mode); image 251, terran\tankt.grp}}
    {{formatbitlbl |label=0x0F2 |value=Edmund Duke (Siege Mode), Terran Siege Tank (Siege Mode); image 253, terran\stank.grp}}
    {{formatbitlbl |label=0x0F3 |value=Edmund Duke Turret (Siege Mode), Siege Tank Turret (Siege Mode); image 254, terran\stankt.grp}}
    {{formatbitlbl |label=0x0F4 |value=Terran Vulture, Jim Raynor (Vulture); image 256, terran\Vulture.grp}}
    {{formatbitlbl |label=0x0F5 |value=Spider Mine; image 258, terran\Spider.grp}}
    {{formatbitlbl |label=0x0F6 |value=Terran Science Vessel, Magellan (Science Vessel); image 260, terran\wessel.grp}}
    {{formatbitlbl |label=0x0F7 |value=image 261, terran\wesselt.grp}}
    {{formatbitlbl |label=0x0F8 |value=Terran Academy; image 263, terran\Academy.grp}}
    {{formatbitlbl |label=0x0F9 |value=Terran Barracks; image 266, terran\TBarrack.grp}}
    {{formatbitlbl |label=0x0FA |value=Terran Armory; image 268, terran\chemlab.grp}}
    {{formatbitlbl |label=0x0FB |value=Terran Comsat Station; image 271, terran\ComSat.grp}}
    {{formatbitlbl |label=0x0FC |value=Terran Command Center; image 275, terran\control.grp}}
    {{formatbitlbl |label=0x0FD |value=Terran Supply Depot; image 278, terran\Depot.grp}}
    {{formatbitlbl |label=0x0FE |value=Terran Control Tower; image 281, terran\DryDocks.grp}}
    {{formatbitlbl |label=0x0FF |value=Terran Factory; image 285, terran\factory.grp}}
    {{formatbitlbl |label=0x100 |value=Terran Covert Ops; image 288, terran\GeneLab.grp}}
    {{formatbitlbl |label=0x101 |value=Ion Cannon; image 292, neutral\ion.grp}}
    {{formatbitlbl |label=0x102 |value=Terran Machine Shop; image 293, terran\machines.grp}}
    {{formatbitlbl |label=0x103 |value=Terran Missile Turret; image 296, terran\missile.grp}}
    {{formatbitlbl |label=0x104 |value=Norad II (Crashed); image 299, neutral\Cbattle.grp}}
    {{formatbitlbl |label=0x105 |value=Terran Physics Lab; image 301, terran\physics.grp}}
    {{formatbitlbl |label=0x106 |value=Terran Bunker; image 304, terran\PillBox.grp}}
    {{formatbitlbl |label=0x107 |value=Terran Refinery; image 307, terran\refinery.grp}}
    {{formatbitlbl |label=0x108 |value=Terran Science Facility; image 309, terran\research.grp}}
    {{formatbitlbl |label=0x109 |value=Terran Nuclear Silo; image 312, terran\nukesilo.grp}}
    {{formatbitlbl |label=0x10A |value=Nuclear Missile; image 316, terran\nukemiss.grp}}
    {{formatbitlbl |label=0x10B |value=image 318, thingy\NukeHit.grp}}
    {{formatbitlbl |label=0x10C |value=Terran Starport; image 319, terran\starport.grp}}
    {{formatbitlbl |label=0x10D |value=Terran Engineering Bay; image 322, terran\weaponpl.grp}}
    {{formatbitlbl |label=0x10E |value=image 325, terran\TBldLrg.grp}}
    {{formatbitlbl |label=0x10F |value=image 330, terran\TBldSml.grp}}
    {{formatbitlbl |label=0x110 |value=image 334, thingy\tBangX.grp}}
    {{formatbitlbl |label=0x111 |value=image 335, thingy\RubbleS.grp}}
    {{formatbitlbl |label=0x112 |value=image 336, thingy\RubbleL.grp}}
    {{formatbitlbl |label=0x113 |value=Vespene Geyser; image 344, neutral\geyser.grp}}
    {{formatbitlbl |label=0x114 |value=Ragnasaur (Ashworld Critter); image 338, neutral\Acritter.grp}}
    {{formatbitlbl |label=0x115 |value=Rhynadon (Badlands Critter); image 340, neutral\Bcritter.grp}}
    {{formatbitlbl |label=0x116 |value=Bengalaas (Jungle Critter); image 342, neutral\Jcritter.grp}}
    {{formatbitlbl |label=0x117 |value=Mineral Field (Type 1); image 347, neutral\min01.grp}}
    {{formatbitlbl |label=0x118 |value=Mineral Field (Type 2); image 349, neutral\min02.grp}}
    {{formatbitlbl |label=0x119 |value=Mineral Field (Type 3); image 351, neutral\min03.grp}}
    {{formatbitlbl |label=0x11A |value=Independent Starport (Unused); image 353, protoss\scout.grp}}
    {{formatbitlbl |label=0x11B |value=Zerg Beacon, Zerg Flag Beacon; image 354, zerg\zmarker.grp}}
    {{formatbitlbl |label=0x11C |value=Terran Beacon, Terran Flag Beacon; image 356, terran\tMarker.grp}}
    {{formatbitlbl |label=0x11D |value=Protoss Beacon, Protoss Flag Beacon; image 358, protoss\pMarker.grp}}
    {{formatbitlbl |label=0x11E |value=Dark Swarm; image 337, thingy\Dswarm.grp}}
    {{formatbitlbl |label=0x11F |value=Flag; image 392, neutral\Flag.grp}}
    {{formatbitlbl |label=0x120 |value=Young Chrysalis; image 393, neutral\KerrEgg.grp}}
    {{formatbitlbl |label=0x121 |value=Psi Emitter; image 394, neutral\PsiEmit.grp}}
    {{formatbitlbl |label=0x122 |value=Data Disc; image 395, neutral\DataDisk.grp}}
    {{formatbitlbl |label=0x123 |value=Khaydarin Crystal; image 396, neutral\KhChunk.grp}}
    {{formatbitlbl |label=0x124 |value=Mineral Cluster Type 1; image 397, neutral\OreChunk.grp}}
    {{formatbitlbl |label=0x125 |value=Mineral Cluster Type 2; image 398, neutral\OreChunk.grp}}
    {{formatbitlbl |label=0x126 |value=Protoss Vespene Gas Orb Type 1; image 399, neutral\GasOrb.grp}}
    {{formatbitlbl |label=0x127 |value=Protoss Vespene Gas Orb Type 2; image 400, neutral\GasOrb.grp}}
    {{formatbitlbl |label=0x128 |value=Zerg Vespene Gas Sac Type 1; image 401, neutral\GasSac.grp}}
    {{formatbitlbl |label=0x129 |value=Zerg Vespene Gas Sac Type 2; image 402, neutral\GasSac.grp}}
    {{formatbitlbl |label=0x12A |value=Terran Vespene Gas Tank Type 1; image 403, neutral\GasTank.grp}}
    {{formatbitlbl |label=0x12B |value=Terran Vespene Gas Tank Type 2; image 404, neutral\GasTank.grp}}
    {{formatbitlbl |label=0x12C |value=image 503, bullet\circle14.grp}}
    {{formatbitlbl |label=0x12D |value=Start Location; image 588, thingy\StartLoc.grp}}
    {{formatbitlbl |label=0x12E |value=Map Revealer; image 582, neutral\maprev.grp}}
    {{formatbitlbl |label=0x12F |value=Floor Gun Trap; image 735, thingy\tileset\install\CLPlate2.grp}}
    {{formatbitlbl |label=0x130 |value=Left Wall Missile Trap; image 738, thingy\tileset\install\DCGun1.grp}}
    {{formatbitlbl |label=0x131 |value=Right Wall Missile Trap; image 739, thingy\tileset\install\DCGun1.grp}}
    {{formatbitlbl |label=0x132 |value=Left Wall Flame Trap; image 740, thingy\tileset\install\DCGun2.grp}}
    {{formatbitlbl |label=0x133 |value=Right Wall Flame Trap; image 741, thingy\tileset\install\DCGun2.grp}}
    {{formatbitlbl |label=0x134 |value=Floor Missile Trap; image 736, thingy\tileset\install\CLPlate1.grp}}
    {{formatbitlbl |label=0x135 |value=image 422, thingy\smoke.grp}}
    {{formatbitlbl |label=0x136 |value=image 441, thingy\GreSmoke.grp}}
    {{formatbitlbl |label=0x137 |value=image 430, thingy\GeySmok1.grp}}
    {{formatbitlbl |label=0x138 |value=image 431, thingy\GeySmok2.grp}}
    {{formatbitlbl |label=0x139 |value=image 432, thingy\GeySmok3.grp}}
    {{formatbitlbl |label=0x13A |value=image 433, thingy\GeySmok4.grp}}
    {{formatbitlbl |label=0x13B |value=image 434, thingy\GeySmok5.grp}}
    {{formatbitlbl |label=0x13C |value=image 425, thingy\explo2.grp}}
    {{formatbitlbl |label=0x13D |value=image 426, thingy\dbl_exp.grp}}
    {{formatbitlbl |label=0x13E |value=image 445, thingy\blackx.grp}}
    {{formatbitlbl |label=0x13F |value=image 23, zerg\zegspawn.grp}}
    {{formatbitlbl |label=0x140 |value=image 449, thingy\pteglow.grp}}
    {{formatbitlbl |label=0x141 |value=image 584, thingy\Juice01.grp}}
    {{formatbitlbl |label=0x142 |value=image 423, thingy\bDust.grp}}
    {{formatbitlbl |label=0x143 |value=image 494, thingy\dust01.grp}}
    {{formatbitlbl |label=0x144 |value=image 495, thingy\dust02.grp}}
    {{formatbitlbl |label=0x145 |value=image 496, thingy\dust03.grp}}
    {{formatbitlbl |label=0x146 |value=image 497, thingy\dust04.grp}}
    {{formatbitlbl |label=0x147 |value=image 498, thingy\dust05.grp}}
    {{formatbitlbl |label=0x148 |value=image 499, thingy\dust06.grp}}
    {{formatbitlbl |label=0x149 |value=image 500, thingy\dust07.grp}}
    {{formatbitlbl |label=0x14A |value=image 501, thingy\dust08.grp}}
    {{formatbitlbl |label=0x14B |value=image 502, thingy\dust09.grp}}
    {{formatbitlbl |label=0x14C |value=image 35, thingy\spooge.grp}}
    {{formatbitlbl |label=0x14D |value=image 519, bullet\pspark.grp}}
    {{formatbitlbl |label=0x14E |value=image 520, bullet\ephFire.grp}}
    {{formatbitlbl |label=0x14F |value=image 521, bullet\hks.grp}}
    {{formatbitlbl |label=0x150 |value=image 522, bullet\blastcan.grp}}
    {{formatbitlbl |label=0x151 |value=image 523, bullet\dragbull.grp}}
    {{formatbitlbl |label=0x152 |value=image 524, bullet\epbBul.grp}}
    {{formatbitlbl |label=0x153 |value=image 525, thingy\psiStorm.grp}}
    {{formatbitlbl |label=0x154 |value=image 526, bullet\scvspark.grp}}
    {{formatbitlbl |label=0x155 |value=image 527, bullet\tspark.grp}}
    {{formatbitlbl |label=0x156 |value=image 528, bullet\gemini.grp}}
    {{formatbitlbl |label=0x157 |value=image 532, bullet\grenade.grp}}
    {{formatbitlbl |label=0x158 |value=image 360, thingy\eldFire.grp}}
    {{formatbitlbl |label=0x159 |value=image 529, bullet\missile.grp}}
    {{formatbitlbl |label=0x15A |value=image 531, thingy\ecaHit.grp}}
    {{formatbitlbl |label=0x15B |value=image 534, thingy\elbfire.grp}}
    {{formatbitlbl |label=0x15C |value=image 535, thingy\elbfireW.grp}}
    {{formatbitlbl |label=0x15D |value=image 533, thingy\mushroom.grp}}
    {{formatbitlbl |label=0x15E |value=image 541, bullet\eycBull.grp}}
    {{formatbitlbl |label=0x15F |value=image 542, bullet\eycBull.grp}}
    {{formatbitlbl |label=0x160 |value=image 554, bullet\missile.grp}}
    {{formatbitlbl |label=0x161 |value=image 504, bullet\zspark.grp}}
    {{formatbitlbl |label=0x162 |value=image 505, bullet\PDripHit.grp}}
    {{formatbitlbl |label=0x163 |value=image 506, bullet\Tentacle.grp}}
    {{formatbitlbl |label=0x164 |value=image 507, thingy\ep2Fire.grp}}
    {{formatbitlbl |label=0x165 |value=image 509, thingy\ep3Shot.grp}}
    {{formatbitlbl |label=0x166 |value=image 511, bullet\spores.grp}}
    {{formatbitlbl |label=0x167 |value=image 515, bullet\Spore2.grp}}
    {{formatbitlbl |label=0x168 |value=image 516, bullet\parasite.grp}}
    {{formatbitlbl |label=0x169 |value=image 364, thingy\esfHit.grp}}
    {{formatbitlbl |label=0x16A |value=image 387, thingy\ebbCloud.grp}}
    {{formatbitlbl |label=0x16B |value=image 517, thingy\consume.grp}}
    {{formatbitlbl |label=0x16C |value=image 383, thingy\Ensnare.grp}}
    {{formatbitlbl |label=0x16D |value=image 512, thingy\SporeHit.grp}}
    {{formatbitlbl |label=0x16E |value=image 548, thingy\emsHit.grp}}
    {{formatbitlbl |label=0x16F |value=image 513, thingy\SpoTrail.grp}}
    {{formatbitlbl |label=0x170 |value=image 514, thingy\gSmoke.grp}}
    {{formatbitlbl |label=0x171 |value=image 523, bullet\dragbull.grp}}
    {{formatbitlbl |label=0x172 |value=image 503, bullet\circle14.grp}}
    {{formatbitlbl |label=0x173 |value=image 419, thingy\plasma.grp}}
    {{formatbitlbl |label=0x174 |value=image 420, thingy\PlasDrip.grp}}
    {{formatbitlbl |label=0x175 |value=image 443, thingy\HKTrail.grp}}
    {{formatbitlbl |label=0x176 |value=image 557, thingy\ehaMed.grp}}
    {{formatbitlbl |label=0x177 |value=image 558, thingy\ehaMed.grp}}
    {{formatbitlbl |label=0x178 |value=image 559, thingy\ehaMed.grp}}
    {{formatbitlbl |label=0x179 |value=image 306, terran\PillBoxT.grp}}
    {{formatbitlbl |label=0x17A |value=image 421, thingy\flamer.grp}}
    {{formatbitlbl |label=0x17B |value=image 391, thingy\recall.grp}}
    {{formatbitlbl |label=0x17C |value=image 546, thingy\eveCast.grp}}
    {{formatbitlbl |label=0x17D |value=Left Upper Level Door; image 742, thingy\tileset\install\CRDoor1.grp}}
    {{formatbitlbl |label=0x17E |value=Right Upper Level Door; image 743, thingy\tileset\install\CRDoor1.grp}}
    {{formatbitlbl |label=0x17F |value=Left Pit Door; image 750, thingy\tileset\install\DIDoor1.grp}}
    {{formatbitlbl |label=0x180 |value=Right Pit Door; image 751, thingy\tileset\install\DIDoor1.grp}}
    {{formatbitlbl |label=0x181 |value=Floor Hatch (Unused); image 754, thingy\tileset\install\DIHatc1.grp}}
    {{formatbitlbl |label=0x182 |value=image 757, thingy\tileset\twilight\Ldxel01.grp}}
    {{formatbitlbl |label=0x183 |value=image 758, thingy\tileset\twilight\Ldxel02.grp}}
    {{formatbitlbl |label=0x184 |value=image 759, thingy\tileset\twilight\Ldxel03.grp}}
    {{formatbitlbl |label=0x185 |value=image 760, thingy\tileset\twilight\Ldxel04.grp}}
    {{formatbitlbl |label=0x186 |value=image 761, thingy\tileset\twilight\Ldxel05.grp}}
    {{formatbitlbl |label=0x187 |value=image 762, thingy\tileset\twilight\Ldxel06.grp}}
    {{formatbitlbl |label=0x188 |value=image 755, thingy\tileset\twilight\Ldarch.grp}}
    {{formatbitlbl |label=0x189 |value=image 756, thingy\tileset\twilight\Lddrill.grp}}
    {{formatbitlbl |label=0x18A |value=image 763, thingy\tileset\twilight\Ldxeltur.grp}}
    {{formatbitlbl |label=0x18B |value=image 764, thingy\tileset\twilight\JTree01.grp}}
    {{formatbitlbl |label=0x18C |value=image 765, thingy\tileset\twilight\JTree02.grp}}
    {{formatbitlbl |label=0x18D |value=image 766, thingy\tileset\twilight\JTree03.grp}}
    {{formatbitlbl |label=0x18E |value=image 767, thingy\tileset\twilight\JTree04.grp}}
    {{formatbitlbl |label=0x18F |value=image 768, thingy\tileset\twilight\JTree05.grp}}
    {{formatbitlbl |label=0x190 |value=image 769, thingy\tileset\twilight\rstatue.grp}}
    {{formatbitlbl |label=0x191 |value=image 770, thingy\tileset\twilight\rstatue.grp}}
    {{formatbitlbl |label=0x192 |value=image 771, thingy\tileset\ice\HDbld01.grp}}
    {{formatbitlbl |label=0x193 |value=image 773, thingy\tileset\ice\HDbld02.grp}}
    {{formatbitlbl |label=0x194 |value=image 775, thingy\tileset\ice\HDbld03.grp}}
    {{formatbitlbl |label=0x195 |value=image 777, thingy\tileset\ice\HDbld04.grp}}
    {{formatbitlbl |label=0x196 |value=image 779, thingy\tileset\ice\HDradarl.grp}}
    {{formatbitlbl |label=0x197 |value=image 781, thingy\tileset\ice\HDradarR.grp}}
    {{formatbitlbl |label=0x198 |value=image 783, thingy\tileset\ice\HDRock01.grp}}
    {{formatbitlbl |label=0x199 |value=image 785, thingy\tileset\ice\HDRock02.grp}}
    {{formatbitlbl |label=0x19A |value=image 787, thingy\tileset\ice\HDSTre01.grp}}
    {{formatbitlbl |label=0x19B |value=image 788, thingy\tileset\ice\HDSTre02.grp}}
    {{formatbitlbl |label=0x19C |value=image 789, thingy\tileset\ice\HDSTre03.grp}}
    {{formatbitlbl |label=0x19D |value=image 790, thingy\tileset\ice\HDSTre04.grp}}
    {{formatbitlbl |label=0x19E |value=image 791, thingy\tileset\ice\HDSpire.grp}}
    {{formatbitlbl |label=0x19F |value=image 793, thingy\tileset\ice\HDTwr01.grp}}
    {{formatbitlbl |label=0x1A0 |value=image 795, thingy\tileset\ice\HDTwr02.grp}}
    {{formatbitlbl |label=0x1A1 |value=image 797, thingy\tileset\ice\LDBTre01.grp}}
    {{formatbitlbl |label=0x1A2 |value=image 799, thingy\tileset\ice\LDBTre02.grp}}
    {{formatbitlbl |label=0x1A3 |value=image 801, thingy\tileset\ice\LDBTre03.grp}}
    {{formatbitlbl |label=0x1A4 |value=image 803, thingy\tileset\ice\LDBTre04.grp}}
    {{formatbitlbl |label=0x1A5 |value=image 805, thingy\tileset\ice\LDbld01.grp}}
    {{formatbitlbl |label=0x1A6 |value=image 807, thingy\tileset\ice\LDbld02.grp}}
    {{formatbitlbl |label=0x1A7 |value=image 809, thingy\tileset\ice\LDComm.grp}}
    {{formatbitlbl |label=0x1A8 |value=image 811, thingy\tileset\ice\LDDtre01.grp}}
    {{formatbitlbl |label=0x1A9 |value=image 813, thingy\tileset\ice\LDDtre02.grp}}
    {{formatbitlbl |label=0x1AA |value=image 815, thingy\tileset\ice\LDDish.grp}}
    {{formatbitlbl |label=0x1AB |value=image 817, thingy\tileset\ice\LDRdr01.grp}}
    {{formatbitlbl |label=0x1AC |value=image 819, thingy\tileset\ice\LDRdr02.grp}}
    {{formatbitlbl |label=0x1AD |value=image 821, thingy\tileset\ice\LDRdr03.grp}}
    {{formatbitlbl |label=0x1AE |value=image 823, thingy\tileset\ice\LDRck01.grp}}
    {{formatbitlbl |label=0x1AF |value=image 825, thingy\tileset\ice\LDRck02.grp}}
    {{formatbitlbl |label=0x1B0 |value=image 834, thingy\tileset\ice\HDRadr02.grp}}
    {{formatbitlbl |label=0x1B1 |value=image 829, thingy\tileset\ice\LDthing.grp}}
    {{formatbitlbl |label=0x1B2 |value=image 831, thingy\tileset\ice\LDsmrock.grp}}
    {{formatbitlbl |label=0x1B3 |value=image 836, thingy\tileset\ice\LDRck01.grp}}
    {{formatbitlbl |label=0x1B4 |value=image 838, thingy\tileset\ice\LDRck02.grp}}
    {{formatbitlbl |label=0x1B5 |value=image 832, thingy\tileset\ice\HDPipes.grp}}
    {{formatbitlbl |label=0x1B6 |value=image 827, thingy\tileset\ice\HDPipes.grp}}
    {{formatbitlbl |label=0x1B7 |value=image 840, thingy\tileset\ice\HDRadr02.grp}}
    {{formatbitlbl |label=0x1B8 |value=image 841, thingy\tileset\ice\JGant1.grp}}
    {{formatbitlbl |label=0x1B9 |value=image 842, thingy\tileset\ice\JGant1.grp}}
    {{formatbitlbl |label=0x1BA |value=image 843, thingy\tileset\ice\RJBTree1.grp}}
    {{formatbitlbl |label=0x1BB |value=image 845, thingy\tileset\ice\RJBTree2.grp}}
    {{formatbitlbl |label=0x1BC |value=image 847, thingy\tileset\ice\RJBTree3.grp}}
    {{formatbitlbl |label=0x1BD |value=image 849, thingy\tileset\ice\RJBTree4.grp}}
    {{formatbitlbl |label=0x1BE |value=image 851, thingy\tileset\desert\HDBANT.grp}}
    {{formatbitlbl |label=0x1BF |value=image 852, thingy\tileset\desert\HDBBROKE.grp}}
    {{formatbitlbl |label=0x1C0 |value=image 854, thingy\tileset\desert\HDBGAS.grp}}
    {{formatbitlbl |label=0x1C1 |value=image 856, thingy\tileset\desert\HDBMED.grp}}
    {{formatbitlbl |label=0x1C2 |value=image 858, thingy\tileset\desert\HDBMOSS.grp}}
    {{formatbitlbl |label=0x1C3 |value=image 860, thingy\tileset\desert\HDBTENT.grp}}
    {{formatbitlbl |label=0x1C4 |value=image 862, thingy\tileset\desert\HDPLNT03.grp}}
    {{formatbitlbl |label=0x1C5 |value=image 864, thingy\tileset\desert\JGBROKE.grp}}
    {{formatbitlbl |label=0x1C6 |value=image 866, thingy\tileset\desert\JGBGAS.grp}}
    {{formatbitlbl |label=0x1C7 |value=image 868, thingy\tileset\desert\JGBGEN.grp}}
    {{formatbitlbl |label=0x1C8 |value=image 870, thingy\tileset\desert\JGBSGN.grp}}
    {{formatbitlbl |label=0x1C9 |value=image 872, thingy\tileset\desert\JGBTENT.grp}}
    {{formatbitlbl |label=0x1CA |value=image 874, thingy\tileset\desert\JGBCOMM.grp}}
    {{formatbitlbl |label=0x1CB |value=image 876, thingy\tileset\desert\JGBFACT.grp}}
    {{formatbitlbl |label=0x1CC |value=image 878, thingy\tileset\desert\JGBRED.grp}}
    {{formatbitlbl |label=0x1CD |value=image 880, thingy\tileset\desert\JGPLNT01.grp}}
    {{formatbitlbl |label=0x1CE |value=image 881, thingy\tileset\desert\JGPLNT02.grp}}
    {{formatbitlbl |label=0x1CF |value=image 883, thingy\tileset\desert\LDBAZ.grp}}
    {{formatbitlbl |label=0x1D0 |value=image 885, thingy\tileset\desert\LDBGAS.grp}}
    {{formatbitlbl |label=0x1D1 |value=image 887, thingy\tileset\desert\LDBGREN.grp}}
    {{formatbitlbl |label=0x1D2 |value=image 889, thingy\tileset\desert\LDBNEON.grp}}
    {{formatbitlbl |label=0x1D3 |value=image 890, thingy\tileset\desert\LDBSUKY.grp}}
    {{formatbitlbl |label=0x1D4 |value=image 892, thingy\tileset\desert\LDBTENT.grp}}
    {{formatbitlbl |label=0x1D5 |value=image 894, thingy\tileset\desert\Ldneon.grp}}
    {{formatbitlbl |label=0x1D6 |value=image 895, thingy\tileset\desert\HDLbox01.grp}}
    {{formatbitlbl |label=0x1D7 |value=image 904, thingy\tileset\desert\HDLbox01.grp}}
    {{formatbitlbl |label=0x1D8 |value=image 897, thingy\tileset\desert\HDMachn2.grp}}
    {{formatbitlbl |label=0x1D9 |value=image 906, thingy\tileset\desert\HDMachn2.grp}}
    {{formatbitlbl |label=0x1DA |value=image 898, thingy\tileset\desert\LDLbox01.grp}}
    {{formatbitlbl |label=0x1DB |value=image 907, thingy\tileset\desert\LDLbox01.grp}}
    {{formatbitlbl |label=0x1DC |value=image 900, thingy\tileset\desert\LDMachn1.grp}}
    {{formatbitlbl |label=0x1DD |value=image 909, thingy\tileset\desert\LDMachn1.grp}}
    {{formatbitlbl |label=0x1DE |value=image 902, thingy\tileset\desert\LDPlnt04.grp}}
    {{formatbitlbl |label=0x1DF |value=image 911, thingy\tileset\desert\Tgas.grp}}
    {{formatbitlbl |label=0x1E0 |value=image 912, thingy\tileset\desert\sarlacc.grp}}
    {{formatbitlbl |label=0x1E1 |value=Lurker Egg; image 914, zerg\Lurkegg.grp}}
    {{formatbitlbl |label=0x1E2 |value=Zerg Devourer; image 915, zerg\devour.grp}}
    {{formatbitlbl |label=0x1E3 |value=image 918, zerg\zdvDeath.grp}}
    {{formatbitlbl |label=0x1E4 |value=image 920, zerg\zLurker.grp}}
    {{formatbitlbl |label=0x1E5 |value=Zerg Lurker; image 921, zerg\Zlurker.grp}}
    {{formatbitlbl |label=0x1E6 |value=Protoss Dark Archon; image 925, protoss\darchn.grp}}
    {{formatbitlbl |label=0x1E7 |value=Protoss Corsair, Raszagal (Corsair); image 929, protoss\corsair.grp}}
    {{formatbitlbl |label=0x1E8 |value=Protoss Dark Templar (Unit); image 933, protoss\dtemplar.grp}}
    {{formatbitlbl |label=0x1E9 |value=Terran Medic; image 944, terran\medic.grp}}
    {{formatbitlbl |label=0x1EA |value=image 946, terran\tmeDeath.grp}}
    {{formatbitlbl |label=0x1EB |value=Terran Valkyrie; image 939, terran\bomber.grp}}
    {{formatbitlbl |label=0x1EC |value=Scantid (Desert Critter); image 952, neutral\Kcritter.grp}}
    {{formatbitlbl |label=0x1ED |value=Kakaru (Twilight Critter); image 954, neutral\Scritter.grp}}
    {{formatbitlbl |label=0x1EE |value=Ursadon (Ice World Critter); image 956, neutral\Icritter.grp}}
    {{formatbitlbl |label=0x1EF |value=Overmind Cocoon; image 923, zerg\XOvermnd.grp}}
    {{formatbitlbl |label=0x1F0 |value=Power Generator; image 949, neutral\Generate.grp}}
    {{formatbitlbl |label=0x1F1 |value=Xel'Naga Temple; image 937, protoss\XelTempl.grp}}
    {{formatbitlbl |label=0x1F2 |value=Psi Disrupter; image 947, neutral\PsiDisr.grp}}
    {{formatbitlbl |label=0x1F3 |value=Warp Gate; image 934, protoss\XwarpGat.grp}}
    {{formatbitlbl |label=0x1F4 |value=image 979, thingy\PDaPsySm.grp}}
    {{formatbitlbl |label=0x1F5 |value=image 980, thingy\PDaPsyMd.grp}}
    {{formatbitlbl |label=0x1F6 |value=image 981, thingy\PDaPsyLg.grp}}
    {{formatbitlbl |label=0x1F7 |value=Disruption Web; image 951, thingy\Disrupt.grp}}
    {{formatbitlbl |label=0x1F8 |value=image 503, bullet\circle14.grp}}
    {{formatbitlbl |label=0x1F9 |value=image 960, thingy\bsmoke.grp}}
    {{formatbitlbl |label=0x1FA |value=image 964, thingy\PcsSplsh.grp}}
    {{formatbitlbl |label=0x1FB |value=image 932, thingy\elbFireC.grp}}
    {{formatbitlbl |label=0x1FC |value=image 966, bullet\grenade.grp}}
    {{formatbitlbl |label=0x1FD |value=image 965, bullet\SMmissle.grp}}
    {{formatbitlbl |label=0x1FE |value=image 985, zerg\zmarker.grp}}
    {{formatbitlbl |label=0x1FF |value=image 961, bullet\Spike.grp}}
    {{formatbitlbl |label=0x200 |value=image 962, thingy\ZDvPuke.grp}}
    {{formatbitlbl |label=0x201 |value=image 963, thingy\ZDvHit.grp}}
    {{formatbitlbl |label=0x202 |value=image 998, thingy\MaelHit.grp}}
    {{formatbitlbl |label=0x203 |value=Uraj Crystal; image 958, neutral\Uraj.grp}}
    {{formatbitlbl |label=0x204 |value=Khalis Crystal; image 959, neutral\Khalis.grp}}
  {{end-bittable}} }}
{{end-formattable}}

