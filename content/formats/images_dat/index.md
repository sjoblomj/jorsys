# images.dat Format

images.dat holds the data of every image. An image is one GRP graphic together with its animation script, and it is drawn as part of a sprite. A unit is usually made of several images: its body, its shadow, and overlays such as engine glows and turrets (see Appendix: Images list). Each entry gives the GRP file, how the image turns and is clicked, whether it plays its full animation script, how it is drawn, which animation script it uses, and six overlay files: lists of points where other graphics attach.

The file is arr\images.dat in the game's MPQ archives. It has 999 entries, one for each image, and is 37962 bytes long. It is stored field by field, not entry by entry: first the GRP File of all 999 images, then the Graphic Turns of all 999, and so on, with nothing in between. The offsets below count from the start of the file.

The layout is the same in every version from 1.04 to 1.17, in both StarCraft and Brood War. StarCraft 1.00 to 1.03 used an older layout with 755 images (28690 bytes). That older file is still in StarDat.mpq in later versions, but it is never loaded, because the game finds the copy in BrooDat.mpq (or patch_rt.mpq) first. Without Brood War, the game and StarEdit only load the graphics files of images 0 to 754, so the higher images have no graphics.

The game loads the file once, when the program starts, together with scripts\iscript.bin and arr\images.tbl. StarEdit reads it as well. If the file is longer than the layout, the game stops with a file error. A shorter file loads without an error if it ends exactly where a field ends; the missing fields then keep whatever they held before. Out-of-range values are not rejected: the game then reads whatever follows the table that the value points into.

## GRP File
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=3996 bytes (4 bytes / Image)}}
  {{formatlbl |label=Description |value=A file number in arr\images.tbl, counting from 1; 0 means none. The game loads unit\<string> when the program starts, and stops with a fatal error if the file cannot be opened. An image with the same value as an earlier image in the same field shares its file. Nothing checks that an image has a GRP before drawing it.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\images.tbl.}}
{{end-formattable}}

## Graphic Turns
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0F9C}}
  {{formatlbl |label=Length |value=999 bytes (1 byte / Image)}}
  {{formatlbl |label=Description |value=Whether the image turns with its unit. If set, the GRP must have 17 frames for each animation frame: 17 directions over the right half of a turn, with the left half drawn mirrored. If clear, the frame is only what the animation script chooses. Only the lowest bit counts.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Does not turn}}
    {{formatbitlbl |label=0x01 |value=Turns (17 directions, mirrored)}}
  {{end-bittable}} }}
{{end-formattable}}

## Clickable
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1383}}
  {{formatlbl |label=Length |value=999 bytes (1 byte / Image)}}
  {{formatlbl |label=Description |value=Whether the image counts for clicking on its unit. The area that can be clicked is the box around the current frames of all clickable images of the sprite; if none is clickable, clicking the unit does not work reliably. Within that box, units with units.dat flag 0x100 can be clicked on a visible pixel of any clickable image, others only on a visible pixel of their main image. Only the lowest bit counts.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Not clickable}}
    {{formatbitlbl |label=0x01 |value=Clickable}}
  {{end-bittable}} }}
{{end-formattable}}

## Use Full Animation Script
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x176A}}
  {{formatlbl |label=Length |value=999 bytes (1 byte / Image)}}
  {{formatlbl |label=Description |value=If clear, the image only plays the Init and Death entries of its animation script and ignores requests for the others (walking, attacking and so on). Only the lowest bit counts.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Init and Death only}}
    {{formatbitlbl |label=0x01 |value=All animations}}
  {{end-bittable}} }}
{{end-formattable}}

## Draw If Cloaked
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1B51}}
  {{formatlbl |label=Length |value=999 bytes (1 byte / Image)}}
  {{formatlbl |label=Description |value=0 hides the image while its unit is cloaked (shadows, engine glows). It also stops animation script commands that create a sprite (sprul, spruluselo) from creating one with this image while the unit is cloaked. Only images with Draw Function 0 get the cloaked look; visible images with another draw function keep drawing normally. StarEdit uses it when showing cloaked preplaced units.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Hidden while cloaked}}
    {{formatbitlbl |label=0x01 and up |value=Shown while cloaked}}
  {{end-bittable}} }}
{{end-formattable}}

## Draw Function
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x1F38}}
  {{formatlbl |label=Length |value=999 bytes (1 byte / Image)}}
  {{formatlbl |label=Description |value=How the image is drawn. Values 2 to 7, 12 and 16 are set by the game while it runs and are not used in the shipped file.}}
  {{formatlbl |label=Values |value=Values above 17 are not rejected: the game takes the image's update and drawing routines from the memory after its two tables of 18. In 1.05, 1.15.0 and 1.17 none of the values 18 to 255 finds a drawing routine there, and most find something that is not code at all, so that calling it crashes the game (in 1.15.0, the value 18 gets the number 8 as the address of its drawing routine).}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=Normal. The only value that cloaking and hallucination change}}
    {{formatbitlbl |label=0x01 |value=Normal, but stays normal on a cloaked or hallucinated unit (blood splats, Shield Battery charge, Installation doodads)}}
    {{formatbitlbl |label=0x02 |value=Cloaking (used by the game while a unit cloaks)}}
    {{formatbitlbl |label=0x03 |value=Cloaked (used by the game)}}
    {{formatbitlbl |label=0x04 |value=Decloaking (used by the game)}}
    {{formatbitlbl |label=0x05 |value=Cloaking, seen through (used by the game)}}
    {{formatbitlbl |label=0x06 |value=Cloaked, seen through (used by the game)}}
    {{formatbitlbl |label=0x07 |value=Decloaking, seen through (used by the game)}}
    {{formatbitlbl |label=0x08 |value=EMP shockwave distortion}}
    {{formatbitlbl |label=0x09 |value=Colour remapping through the table chosen by Remapping (glows, fire, explosions)}}
    {{formatbitlbl |label=0x0A |value=Shadow: darkens what is underneath}}
    {{formatbitlbl |label=0x0B |value=Health bar: draws the hit point, shield and energy bar instead of the GRP}}
    {{formatbitlbl |label=0x0C |value=Protoss warp-in texture (used by the game)}}
    {{formatbitlbl |label=0x0D |value=Selection circle}}
    {{formatbitlbl |label=0x0E |value=Normal, in the colour of the player who owns the sprite (the Flag)}}
    {{formatbitlbl |label=0x0F |value=Draws only a green outline of the frame (building placement box)}}
    {{formatbitlbl |label=0x10 |value=Hallucination (used by the game)}}
    {{formatbitlbl |label=0x11 |value=Protoss warp-in fade}}
  {{end-bittable}} }}
{{end-formattable}}

## Remapping
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x231F}}
  {{formatlbl |label=Length |value=999 bytes (1 byte / Image)}}
  {{formatlbl |label=Description |value=For Draw Function 9 only: which colour table the image is drawn through. Each table is loaded with the map from Tileset\<tileset>\<name>.pcx; every drawn pixel becomes table[GRP pixel, screen pixel]. Ignored for other draw functions.}}
  {{formatlbl |label=Values |value=Values above 7 are not rejected: the game takes the table's address from the memory after its list of seven, which is unrelated data. 0 with Draw Function 9 has no table: the image gets a null table address, and the game crashes with an access violation when it draws the first pixel of the image.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=None}}
    {{formatbitlbl |label=0x01 |value=ofire (orange fire and glows)}}
    {{formatbitlbl |label=0x02 |value=gfire (green fire)}}
    {{formatbitlbl |label=0x03 |value=bfire (blue fire, Protoss glows, shield hit)}}
    {{formatbitlbl |label=0x04 |value=bexpl (blue explosions)}}
    {{formatbitlbl |label=0x05 |value=trans50 (50% translucency, also used for cloaking)}}
    {{formatbitlbl |label=0x06 |value=red (one row only, so most GRP colours read past it)}}
    {{formatbitlbl |label=0x07 |value=green (one row only, like red)}}
  {{end-bittable}} }}
{{end-formattable}}

## Animation Script
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x2706}}
  {{formatlbl |label=Length |value=3996 bytes (4 bytes / Image)}}
  {{formatlbl |label=Description |value=The animation script (in scripts\iscript.bin) that runs the image. It is an ID that the game looks up in the script file's header, not a position; an ID that is not there stops the game with the fatal error "script %d does not exist". Several images can share a script.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535; must be an ID in iscript.bin.}}
{{end-formattable}}

## Shield Overlay
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x36A2}}
  {{formatlbl |label=Length |value=3996 bytes (4 bytes / Image)}}
  {{formatlbl |label=Description |value=A file number in arr\images.tbl, counting from 1; 0 means none. The game loads unit\<string> when the program starts, and stops with a fatal error if the file cannot be opened. An image with the same value as an earlier image in the same field shares its file. Where the shield flash (image 424) appears when the unit's shields are hit: the file has one list per direction the unit faces (17), with 32 points for the directions the hit comes from (not mirrored). The game does not test for 0 before using it, but it only uses it for units with shields; if such a unit's image had 0, the game would read through a null address and crash with an access violation. Most unit images have protoss\mshield.los.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\images.tbl.}}
{{end-formattable}}

## Attack Overlay
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x463E}}
  {{formatlbl |label=Length |value=3996 bytes (4 bytes / Image)}}
  {{formatlbl |label=Description |value=A file number in arr\images.tbl, counting from 1; 0 means none. The game loads unit\<string> when the program starts, and stops with a fatal error if the file cannot be opened. An image with the same value as an earlier image in the same field shares its file. The file is a list of points: for each frame of the image's GRP, a number of (x, y) offsets in pixels from the image, as signed bytes; x is mirrored with the image, and (127, 127) means no point. Used for the muzzle flashes of units firing from inside a Bunker (the bunker's own file, terran\pillbox.loa, one point for each of 8 directions) and by animation script commands that place graphics at an overlay point (imgoluselo and the like) with overlay 0. Neither use tests for 0: with 0 the game reads through a null address and crashes with an access violation.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\images.tbl.}}
{{end-formattable}}

## Damage Overlay
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x55DA}}
  {{formatlbl |label=Length |value=3996 bytes (4 bytes / Image)}}
  {{formatlbl |label=Description |value=A file number in arr\images.tbl, counting from 1; 0 means none. The game loads unit\<string> when the program starts, and stops with a fatal error if the file cannot be opened. An image with the same value as an earlier image in the same field shares its file. The file is a list of points: for each frame of the image's GRP, a number of (x, y) offsets in pixels from the image, as signed bytes; x is mirrored with the image, and (127, 127) means no point. Where the fires appear on a damaged building: none above 2/3 of its hit points, then more and larger fires as the hit points drop, at random points of the list. Up to 22 points of the first frame count. 0 means the unit never shows damage fires.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\images.tbl.}}
{{end-formattable}}

## Special Overlay
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x6576}}
  {{formatlbl |label=Length |value=3996 bytes (4 bytes / Image)}}
  {{formatlbl |label=Description |value=A file number in arr\images.tbl, counting from 1; 0 means none. The game loads unit\<string> when the program starts, and stops with a fatal error if the file cannot be opened. An image with the same value as an earlier image in the same field shares its file. The file is a list of points: for each frame of the image's GRP, a number of (x, y) offsets in pixels from the image, as signed bytes; x is mirrored with the image, and (127, 127) means no point. Point 0 is where things attached to the image sit: the turret of a unit with a subunit (Siege Tank, Goliath), and overlays created by the animation script commands imgolorig and switchul. creategasoverlays n puts geyser smoke at point n. Also used by the *uselo script commands with overlay 2. None of these uses tests for 0: with 0 the game reads through a null address and crashes with an access violation.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\images.tbl.}}
{{end-formattable}}

## Landing Dust Overlay
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x7512}}
  {{formatlbl |label=Length |value=3996 bytes (4 bytes / Image)}}
  {{formatlbl |label=Description |value=A file number in arr\images.tbl, counting from 1; 0 means none. The game loads unit\<string> when the program starts, and stops with a fatal error if the file cannot be opened. An image with the same value as an earlier image in the same field shares its file. The file is a list of points: for each frame of the image's GRP, a number of (x, y) offsets in pixels from the image, as signed bytes; x is mirrored with the image, and (127, 127) means no point. Where dust appears when a building lands: dust sprites at points 0 to 8 and mirrored ones at points 16 to 24. 0 means no dust. Points 0 and 1 are also where the two units hatch from a Zergling or Scourge egg (zerg\zzebirth.lob, zerg\zavbirth.lob); that use does not test for 0, and with 0 the game reads through a null address and crashes with an access violation.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\images.tbl.}}
{{end-formattable}}

## Lift-off Dust Overlay
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x84AE}}
  {{formatlbl |label=Length |value=3996 bytes (4 bytes / Image)}}
  {{formatlbl |label=Description |value=A file number in arr\images.tbl, counting from 1; 0 means none. The game loads unit\<string> when the program starts, and stops with a fatal error if the file cannot be opened. An image with the same value as an earlier image in the same field shares its file. The file is a list of points: for each frame of the image's GRP, a number of (x, y) offsets in pixels from the image, as signed bytes; x is mirrored with the image, and (127, 127) means no point. Where dust appears when a building lifts off, used like Landing Dust Overlay. 0 means no dust. StarEdit shows it for buildings placed lifted.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\images.tbl.}}
{{end-formattable}}

---

## Appendix: Images list
{{begin-formattable}}
  {{formatlbl |label=Description |value=Every image, with its GRP file from arr\images.tbl in the shipped data (all under unit\). Images 755 to 998 only exist in Brood War.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x000 |value=zerg\avenger.grp}}
    {{formatbitlbl |label=0x001 |value=zerg\avenger.grp}}
    {{formatbitlbl |label=0x002 |value=zerg\zavBirth.grp}}
    {{formatbitlbl |label=0x003 |value=zerg\zavDeath.grp}}
    {{formatbitlbl |label=0x004 |value=zerg\zavExplo.grp}}
    {{formatbitlbl |label=0x005 |value=zerg\brood.grp}}
    {{formatbitlbl |label=0x006 |value=zerg\zbrShad.grp}}
    {{formatbitlbl |label=0x007 |value=zerg\zbrDeath.grp}}
    {{formatbitlbl |label=0x008 |value=zerg\bugguy.grp}}
    {{formatbitlbl |label=0x009 |value=zerg\zbgShad.grp}}
    {{formatbitlbl |label=0x00A |value=thingy\zbgExplo.grp}}
    {{formatbitlbl |label=0x00B |value=zerg\cocoon.grp}}
    {{formatbitlbl |label=0x00C |value=zerg\cocoon.grp}}
    {{formatbitlbl |label=0x00D |value=zerg\defiler.grp}}
    {{formatbitlbl |label=0x00E |value=zerg\defiler.grp}}
    {{formatbitlbl |label=0x00F |value=zerg\zdebirth.grp}}
    {{formatbitlbl |label=0x010 |value=zerg\zdeDeath.grp}}
    {{formatbitlbl |label=0x011 |value=zerg\drone.grp}}
    {{formatbitlbl |label=0x012 |value=zerg\drone.grp}}
    {{formatbitlbl |label=0x013 |value=zerg\zdrbirth.grp}}
    {{formatbitlbl |label=0x014 |value=zerg\zdrDeath.grp}}
    {{formatbitlbl |label=0x015 |value=zerg\egg.grp}}
    {{formatbitlbl |label=0x016 |value=zerg\zegShad.grp}}
    {{formatbitlbl |label=0x017 |value=zerg\zegspawn.grp}}
    {{formatbitlbl |label=0x018 |value=zerg\zegDeath.grp}}
    {{formatbitlbl |label=0x019 |value=zerg\guardian.grp}}
    {{formatbitlbl |label=0x01A |value=zerg\guardian.grp}}
    {{formatbitlbl |label=0x01B |value=zerg\cocoon.grp}}
    {{formatbitlbl |label=0x01C |value=zerg\zguDeath.grp}}
    {{formatbitlbl |label=0x01D |value=zerg\hydra.grp}}
    {{formatbitlbl |label=0x01E |value=zerg\zhyShad.grp}}
    {{formatbitlbl |label=0x01F |value=zerg\zhybirth.grp}}
    {{formatbitlbl |label=0x020 |value=zerg\zhyDeath.grp}}
    {{formatbitlbl |label=0x021 |value=zerg\uikerr.grp}}
    {{formatbitlbl |label=0x022 |value=zerg\uikShad.grp}}
    {{formatbitlbl |label=0x023 |value=thingy\spooge.grp}}
    {{formatbitlbl |label=0x024 |value=zerg\larva.grp}}
    {{formatbitlbl |label=0x025 |value=zerg\zlaDeath.grp}}
    {{formatbitlbl |label=0x026 |value=zerg\mutalid.grp}}
    {{formatbitlbl |label=0x027 |value=zerg\mutalid.grp}}
    {{formatbitlbl |label=0x028 |value=zerg\zmubirth.grp}}
    {{formatbitlbl |label=0x029 |value=zerg\zmuDeath.grp}}
    {{formatbitlbl |label=0x02A |value=zerg\overlord.grp}}
    {{formatbitlbl |label=0x02B |value=zerg\overlord.grp}}
    {{formatbitlbl |label=0x02C |value=zerg\zovBirth.grp}}
    {{formatbitlbl |label=0x02D |value=zerg\zovDeath.grp}}
    {{formatbitlbl |label=0x02E |value=zerg\queen.grp}}
    {{formatbitlbl |label=0x02F |value=zerg\queen.grp}}
    {{formatbitlbl |label=0x030 |value=zerg\zquDeath.grp}}
    {{formatbitlbl |label=0x031 |value=zerg\zquBirth.grp}}
    {{formatbitlbl |label=0x032 |value=zerg\ultra.grp}}
    {{formatbitlbl |label=0x033 |value=zerg\zulShad.grp}}
    {{formatbitlbl |label=0x034 |value=zerg\zulbirth.grp}}
    {{formatbitlbl |label=0x035 |value=zerg\zulDeath.grp}}
    {{formatbitlbl |label=0x036 |value=zerg\zergling.grp}}
    {{formatbitlbl |label=0x037 |value=zerg\zzeShad.grp}}
    {{formatbitlbl |label=0x038 |value=zerg\zzebirth.grp}}
    {{formatbitlbl |label=0x039 |value=zerg\zzeDeath.grp}}
    {{formatbitlbl |label=0x03A |value=thingy\zAirDthL.grp}}
    {{formatbitlbl |label=0x03B |value=thingy\zAirDthS.grp}}
    {{formatbitlbl |label=0x03C |value=thingy\zBldDthS.grp}}
    {{formatbitlbl |label=0x03D |value=zerg\UCereb.grp}}
    {{formatbitlbl |label=0x03E |value=zerg\zucShad.grp}}
    {{formatbitlbl |label=0x03F |value=terran\control.grp}}
    {{formatbitlbl |label=0x040 |value=zerg\chrysal.grp}}
    {{formatbitlbl |label=0x041 |value=zerg\zchShad.grp}}
    {{formatbitlbl |label=0x042 |value=zerg\cerebrat.grp}}
    {{formatbitlbl |label=0x043 |value=zerg\zceShad.grp}}
    {{formatbitlbl |label=0x044 |value=zerg\fcolony.grp}}
    {{formatbitlbl |label=0x045 |value=zerg\zfcShad.grp}}
    {{formatbitlbl |label=0x046 |value=zerg\hatchery.grp}}
    {{formatbitlbl |label=0x047 |value=zerg\zhaShad.grp}}
    {{formatbitlbl |label=0x048 |value=Zerg\Hive.grp}}
    {{formatbitlbl |label=0x049 |value=zerg\zhiShad.grp}}
    {{formatbitlbl |label=0x04A |value=zerg\Lair.grp}}
    {{formatbitlbl |label=0x04B |value=zerg\zlrShad.grp}}
    {{formatbitlbl |label=0x04C |value=zerg\Lurker.grp}}
    {{formatbitlbl |label=0x04D |value=zerg\zluShad.grp}}
    {{formatbitlbl |label=0x04E |value=neutral\kerrChry.grp}}
    {{formatbitlbl |label=0x04F |value=neutral\nkoShad.grp}}
    {{formatbitlbl |label=0x050 |value=zerg\MutaCham.grp}}
    {{formatbitlbl |label=0x051 |value=zerg\zmcShad.grp}}
    {{formatbitlbl |label=0x052 |value=zerg\Mutapit.grp}}
    {{formatbitlbl |label=0x053 |value=zerg\zmhShad.grp}}
    {{formatbitlbl |label=0x054 |value=zerg\nest.grp}}
    {{formatbitlbl |label=0x055 |value=zerg\zneShad.grp}}
    {{formatbitlbl |label=0x056 |value=zerg\NydusPit.grp}}
    {{formatbitlbl |label=0x057 |value=zerg\znyShad.grp}}
    {{formatbitlbl |label=0x058 |value=zerg\Over1.grp}}
    {{formatbitlbl |label=0x059 |value=zerg\Over2.grp}}
    {{formatbitlbl |label=0x05A |value=zerg\Over2.grp}}
    {{formatbitlbl |label=0x05B |value=zerg\RCluster.grp}}
    {{formatbitlbl |label=0x05C |value=zerg\zrcShad.grp}}
    {{formatbitlbl |label=0x05D |value=zerg\Extract.grp}}
    {{formatbitlbl |label=0x05E |value=zerg\zreShad.grp}}
    {{formatbitlbl |label=0x05F |value=zerg\Snakey.grp}}
    {{formatbitlbl |label=0x060 |value=zerg\zsbShad.grp}}
    {{formatbitlbl |label=0x061 |value=zerg\spire.grp}}
    {{formatbitlbl |label=0x062 |value=zerg\zspShad.grp}}
    {{formatbitlbl |label=0x063 |value=zerg\SColony.grp}}
    {{formatbitlbl |label=0x064 |value=zerg\zscShad.grp}}
    {{formatbitlbl |label=0x065 |value=zerg\Infest03.grp}}
    {{formatbitlbl |label=0x066 |value=zerg\ZBuild.grp}}
    {{formatbitlbl |label=0x067 |value=zerg\ZBuild.grp}}
    {{formatbitlbl |label=0x068 |value=zerg\ZBuild.grp}}
    {{formatbitlbl |label=0x069 |value=zerg\ZBuild.grp}}
    {{formatbitlbl |label=0x06A |value=zerg\ZBShad.grp}}
    {{formatbitlbl |label=0x06B |value=zerg\zSpawn01.grp}}
    {{formatbitlbl |label=0x06C |value=zerg\zSpawn02.grp}}
    {{formatbitlbl |label=0x06D |value=zerg\zSpawn03.grp}}
    {{formatbitlbl |label=0x06E |value=thingy\ZRubbleS.grp}}
    {{formatbitlbl |label=0x06F |value=thingy\ZRubbleL.grp}}
    {{formatbitlbl |label=0x070 |value=protoss\carrier.grp}}
    {{formatbitlbl |label=0x071 |value=protoss\carrier.grp}}
    {{formatbitlbl |label=0x072 |value=thingy\pcaGlow.grp}}
    {{formatbitlbl |label=0x073 |value=protoss\carrier.grp}}
    {{formatbitlbl |label=0x074 |value=protoss\Intercep.grp}}
    {{formatbitlbl |label=0x075 |value=protoss\Intercep.grp}}
    {{formatbitlbl |label=0x076 |value=protoss\shuttle.grp}}
    {{formatbitlbl |label=0x077 |value=protoss\shuttle.grp}}
    {{formatbitlbl |label=0x078 |value=thingy\pshGlow.grp}}
    {{formatbitlbl |label=0x079 |value=protoss\shuttle.grp}}
    {{formatbitlbl |label=0x07A |value=protoss\dragoon.grp}}
    {{formatbitlbl |label=0x07B |value=protoss\pdrShad.grp}}
    {{formatbitlbl |label=0x07C |value=protoss\pdrDeath.grp}}
    {{formatbitlbl |label=0x07D |value=protoss\dragoon.grp}}
    {{formatbitlbl |label=0x07E |value=protoss\templar.grp}}
    {{formatbitlbl |label=0x07F |value=protoss\pteShad.grp}}
    {{formatbitlbl |label=0x080 |value=protoss\templar.grp}}
    {{formatbitlbl |label=0x081 |value=protoss\dtemplar.grp}}
    {{formatbitlbl |label=0x082 |value=protoss\arbiter.grp}}
    {{formatbitlbl |label=0x083 |value=protoss\arbiter.grp}}
    {{formatbitlbl |label=0x084 |value=thingy\pabGlow.grp}}
    {{formatbitlbl |label=0x085 |value=protoss\arbiter.grp}}
    {{formatbitlbl |label=0x086 |value=protoss\archon.grp}}
    {{formatbitlbl |label=0x087 |value=protoss\archonT.grp}}
    {{formatbitlbl |label=0x088 |value=protoss\archonT2.grp}}
    {{formatbitlbl |label=0x089 |value=protoss\probe.grp}}
    {{formatbitlbl |label=0x08A |value=protoss\probe.grp}}
    {{formatbitlbl |label=0x08B |value=protoss\probe.grp}}
    {{formatbitlbl |label=0x08C |value=protoss\scout.grp}}
    {{formatbitlbl |label=0x08D |value=protoss\scout.grp}}
    {{formatbitlbl |label=0x08E |value=thingy\pscGlow.grp}}
    {{formatbitlbl |label=0x08F |value=protoss\scout.grp}}
    {{formatbitlbl |label=0x090 |value=protoss\trilob.grp}}
    {{formatbitlbl |label=0x091 |value=protoss\ptrShad.grp}}
    {{formatbitlbl |label=0x092 |value=protoss\trilob.grp}}
    {{formatbitlbl |label=0x093 |value=protoss\sapper.grp}}
    {{formatbitlbl |label=0x094 |value=protoss\witness.grp}}
    {{formatbitlbl |label=0x095 |value=protoss\witness.grp}}
    {{formatbitlbl |label=0x096 |value=protoss\witness.grp}}
    {{formatbitlbl |label=0x097 |value=protoss\zealot.grp}}
    {{formatbitlbl |label=0x098 |value=protoss\pzeShad.grp}}
    {{formatbitlbl |label=0x099 |value=protoss\zealot.grp}}
    {{formatbitlbl |label=0x09A |value=protoss\zealot.grp}}
    {{formatbitlbl |label=0x09B |value=protoss\archives.grp}}
    {{formatbitlbl |label=0x09C |value=protoss\archives.grp}}
    {{formatbitlbl |label=0x09D |value=protoss\pacShad.grp}}
    {{formatbitlbl |label=0x09E |value=protoss\assim.grp}}
    {{formatbitlbl |label=0x09F |value=protoss\assim.grp}}
    {{formatbitlbl |label=0x0A0 |value=protoss\pasShad.grp}}
    {{formatbitlbl |label=0x0A1 |value=protoss\beacon.grp}}
    {{formatbitlbl |label=0x0A2 |value=protoss\beacon.grp}}
    {{formatbitlbl |label=0x0A3 |value=protoss\pbeShad.grp}}
    {{formatbitlbl |label=0x0A4 |value=protoss\citadel.grp}}
    {{formatbitlbl |label=0x0A5 |value=protoss\citadel.grp}}
    {{formatbitlbl |label=0x0A6 |value=protoss\pciShad.grp}}
    {{formatbitlbl |label=0x0A7 |value=protoss\forge.grp}}
    {{formatbitlbl |label=0x0A8 |value=protoss\forgeT.grp}}
    {{formatbitlbl |label=0x0A9 |value=protoss\forge.grp}}
    {{formatbitlbl |label=0x0AA |value=protoss\pfoShad.grp}}
    {{formatbitlbl |label=0x0AB |value=protoss\gateway.grp}}
    {{formatbitlbl |label=0x0AC |value=protoss\gateway.grp}}
    {{formatbitlbl |label=0x0AD |value=protoss\pgaShad.grp}}
    {{formatbitlbl |label=0x0AE |value=protoss\gencore.grp}}
    {{formatbitlbl |label=0x0AF |value=protoss\gencore.grp}}
    {{formatbitlbl |label=0x0B0 |value=protoss\gencoreT.grp}}
    {{formatbitlbl |label=0x0B1 |value=protoss\pgcShad.grp}}
    {{formatbitlbl |label=0x0B2 |value=neutral\Khyad01.grp}}
    {{formatbitlbl |label=0x0B3 |value=protoss\nexus.grp}}
    {{formatbitlbl |label=0x0B4 |value=protoss\nexus.grp}}
    {{formatbitlbl |label=0x0B5 |value=protoss\pneGlow.grp}}
    {{formatbitlbl |label=0x0B6 |value=protoss\pneShad.grp}}
    {{formatbitlbl |label=0x0B7 |value=protoss\photon.grp}}
    {{formatbitlbl |label=0x0B8 |value=protoss\ppbShad.grp}}
    {{formatbitlbl |label=0x0B9 |value=protoss\photon.grp}}
    {{formatbitlbl |label=0x0BA |value=protoss\prism.grp}}
    {{formatbitlbl |label=0x0BB |value=protoss\prism.grp}}
    {{formatbitlbl |label=0x0BC |value=protoss\pauShad.grp}}
    {{formatbitlbl |label=0x0BD |value=protoss\pylon.grp}}
    {{formatbitlbl |label=0x0BE |value=protoss\pylon.grp}}
    {{formatbitlbl |label=0x0BF |value=protoss\ppyShad.grp}}
    {{formatbitlbl |label=0x0C0 |value=protoss\robotic.grp}}
    {{formatbitlbl |label=0x0C1 |value=protoss\robotic.grp}}
    {{formatbitlbl |label=0x0C2 |value=protoss\proShad.grp}}
    {{formatbitlbl |label=0x0C3 |value=protoss\sbattery.grp}}
    {{formatbitlbl |label=0x0C4 |value=protoss\pbaGlow.grp}}
    {{formatbitlbl |label=0x0C5 |value=protoss\sbattery.grp}}
    {{formatbitlbl |label=0x0C6 |value=protoss\pbaShad.grp}}
    {{formatbitlbl |label=0x0C7 |value=protoss\stargate.grp}}
    {{formatbitlbl |label=0x0C8 |value=protoss\psgGlow.grp}}
    {{formatbitlbl |label=0x0C9 |value=protoss\stargate.grp}}
    {{formatbitlbl |label=0x0CA |value=protoss\psgShad.grp}}
    {{formatbitlbl |label=0x0CB |value=neutral\stasis.grp}}
    {{formatbitlbl |label=0x0CC |value=protoss\stasis.grp}}
    {{formatbitlbl |label=0x0CD |value=protoss\stasis.grp}}
    {{formatbitlbl |label=0x0CE |value=protoss\pstShad.grp}}
    {{formatbitlbl |label=0x0CF |value=neutral\temple.grp}}
    {{formatbitlbl |label=0x0D0 |value=protoss\warp.grp}}
    {{formatbitlbl |label=0x0D1 |value=protoss\warp.grp}}
    {{formatbitlbl |label=0x0D2 |value=protoss\texture.grp}}
    {{formatbitlbl |label=0x0D3 |value=protoss\pb1Glow.grp}}
    {{formatbitlbl |label=0x0D4 |value=protoss\pwaShad.grp}}
    {{formatbitlbl |label=0x0D5 |value=thingy\tBangS.grp}}
    {{formatbitlbl |label=0x0D6 |value=thingy\tBangL.grp}}
    {{formatbitlbl |label=0x0D7 |value=thingy\tBangX.grp}}
    {{formatbitlbl |label=0x0D8 |value=thingy\PRubbleS.grp}}
    {{formatbitlbl |label=0x0D9 |value=thingy\PRubbleL.grp}}
    {{formatbitlbl |label=0x0DA |value=terran\BattleCr.grp}}
    {{formatbitlbl |label=0x0DB |value=terran\BattleCr.grp}}
    {{formatbitlbl |label=0x0DC |value=thingy\tbaGlow.grp}}
    {{formatbitlbl |label=0x0DD |value=neutral\civilian.grp}}
    {{formatbitlbl |label=0x0DE |value=neutral\nciShad.grp}}
    {{formatbitlbl |label=0x0DF |value=terran\dropship.grp}}
    {{formatbitlbl |label=0x0E0 |value=terran\dropship.grp}}
    {{formatbitlbl |label=0x0E1 |value=thingy\tdrGlow.grp}}
    {{formatbitlbl |label=0x0E2 |value=terran\firebat.grp}}
    {{formatbitlbl |label=0x0E3 |value=terran\tfbShad.grp}}
    {{formatbitlbl |label=0x0E4 |value=terran\ghost.grp}}
    {{formatbitlbl |label=0x0E5 |value=terran\tghShad.grp}}
    {{formatbitlbl |label=0x0E6 |value=terran\tghDeath.grp}}
    {{formatbitlbl |label=0x0E7 |value=terran\ghost.grp}}
    {{formatbitlbl |label=0x0E8 |value=thingy\NukeBeam.grp}}
    {{formatbitlbl |label=0x0E9 |value=thingy\NukeTarg.grp}}
    {{formatbitlbl |label=0x0EA |value=terran\goliath.grp}}
    {{formatbitlbl |label=0x0EB |value=terran\goliathT.grp}}
    {{formatbitlbl |label=0x0EC |value=terran\tgoShad.grp}}
    {{formatbitlbl |label=0x0ED |value=terran\ughost.grp}}
    {{formatbitlbl |label=0x0EE |value=terran\ughShad.grp}}
    {{formatbitlbl |label=0x0EF |value=terran\marine.grp}}
    {{formatbitlbl |label=0x0F0 |value=terran\tmaShad.grp}}
    {{formatbitlbl |label=0x0F1 |value=terran\tmaDeath.grp}}
    {{formatbitlbl |label=0x0F2 |value=terran\marine.grp}}
    {{formatbitlbl |label=0x0F3 |value=terran\phoenix.grp}}
    {{formatbitlbl |label=0x0F4 |value=terran\phoenix.grp}}
    {{formatbitlbl |label=0x0F5 |value=thingy\tphGlow.grp}}
    {{formatbitlbl |label=0x0F6 |value=terran\marine.grp}}
    {{formatbitlbl |label=0x0F7 |value=terran\SCV.grp}}
    {{formatbitlbl |label=0x0F8 |value=terran\SCV.grp}}
    {{formatbitlbl |label=0x0F9 |value=thingy\tscGlow.grp}}
    {{formatbitlbl |label=0x0FA |value=terran\tank.grp}}
    {{formatbitlbl |label=0x0FB |value=terran\tankt.grp}}
    {{formatbitlbl |label=0x0FC |value=terran\ttaShad.grp}}
    {{formatbitlbl |label=0x0FD |value=terran\stank.grp}}
    {{formatbitlbl |label=0x0FE |value=terran\stankt.grp}}
    {{formatbitlbl |label=0x0FF |value=terran\tstShad.grp}}
    {{formatbitlbl |label=0x100 |value=terran\Vulture.grp}}
    {{formatbitlbl |label=0x101 |value=terran\Vulture.grp}}
    {{formatbitlbl |label=0x102 |value=terran\Spider.grp}}
    {{formatbitlbl |label=0x103 |value=terran\tsmShad.grp}}
    {{formatbitlbl |label=0x104 |value=terran\wessel.grp}}
    {{formatbitlbl |label=0x105 |value=terran\wesselt.grp}}
    {{formatbitlbl |label=0x106 |value=terran\tveShad.grp}}
    {{formatbitlbl |label=0x107 |value=terran\Academy.grp}}
    {{formatbitlbl |label=0x108 |value=terran\AcademyT.grp}}
    {{formatbitlbl |label=0x109 |value=terran\tacShad.grp}}
    {{formatbitlbl |label=0x10A |value=terran\TBarrack.grp}}
    {{formatbitlbl |label=0x10B |value=terran\tbrShad.grp}}
    {{formatbitlbl |label=0x10C |value=terran\chemlab.grp}}
    {{formatbitlbl |label=0x10D |value=terran\chemlabT.grp}}
    {{formatbitlbl |label=0x10E |value=terran\tclShad.grp}}
    {{formatbitlbl |label=0x10F |value=terran\ComSat.grp}}
    {{formatbitlbl |label=0x110 |value=terran\ComSatC.grp}}
    {{formatbitlbl |label=0x111 |value=terran\ComSatT.grp}}
    {{formatbitlbl |label=0x112 |value=terran\tcsShad.grp}}
    {{formatbitlbl |label=0x113 |value=terran\control.grp}}
    {{formatbitlbl |label=0x114 |value=terran\controlT.grp}}
    {{formatbitlbl |label=0x115 |value=terran\tccShad.grp}}
    {{formatbitlbl |label=0x116 |value=terran\Depot.grp}}
    {{formatbitlbl |label=0x117 |value=terran\DepotT.grp}}
    {{formatbitlbl |label=0x118 |value=terran\tdeShad.grp}}
    {{formatbitlbl |label=0x119 |value=terran\DryDocks.grp}}
    {{formatbitlbl |label=0x11A |value=terran\DryDockC.grp}}
    {{formatbitlbl |label=0x11B |value=terran\DryDockT.grp}}
    {{formatbitlbl |label=0x11C |value=terran\tddShad.grp}}
    {{formatbitlbl |label=0x11D |value=terran\factory.grp}}
    {{formatbitlbl |label=0x11E |value=terran\factoryT.grp}}
    {{formatbitlbl |label=0x11F |value=terran\tfaShad.grp}}
    {{formatbitlbl |label=0x120 |value=terran\GeneLab.grp}}
    {{formatbitlbl |label=0x121 |value=terran\GeneLabC.grp}}
    {{formatbitlbl |label=0x122 |value=terran\GeneLabT.grp}}
    {{formatbitlbl |label=0x123 |value=terran\tglShad.grp}}
    {{formatbitlbl |label=0x124 |value=neutral\ion.grp}}
    {{formatbitlbl |label=0x125 |value=terran\machines.grp}}
    {{formatbitlbl |label=0x126 |value=terran\machineC.grp}}
    {{formatbitlbl |label=0x127 |value=terran\tmsShad.grp}}
    {{formatbitlbl |label=0x128 |value=terran\missile.grp}}
    {{formatbitlbl |label=0x129 |value=terran\missileT.grp}}
    {{formatbitlbl |label=0x12A |value=terran\tmiShad.grp}}
    {{formatbitlbl |label=0x12B |value=neutral\Cbattle.grp}}
    {{formatbitlbl |label=0x12C |value=neutral\cbaShad.grp}}
    {{formatbitlbl |label=0x12D |value=terran\physics.grp}}
    {{formatbitlbl |label=0x12E |value=terran\physicsC.grp}}
    {{formatbitlbl |label=0x12F |value=terran\tplShad.grp}}
    {{formatbitlbl |label=0x130 |value=terran\PillBox.grp}}
    {{formatbitlbl |label=0x131 |value=terran\tpbShad.grp}}
    {{formatbitlbl |label=0x132 |value=terran\PillBoxT.grp}}
    {{formatbitlbl |label=0x133 |value=terran\refinery.grp}}
    {{formatbitlbl |label=0x134 |value=terran\treShad.grp}}
    {{formatbitlbl |label=0x135 |value=terran\research.grp}}
    {{formatbitlbl |label=0x136 |value=terran\ResearcT.grp}}
    {{formatbitlbl |label=0x137 |value=terran\trlShad.grp}}
    {{formatbitlbl |label=0x138 |value=terran\nukesilo.grp}}
    {{formatbitlbl |label=0x139 |value=terran\NukeSilC.grp}}
    {{formatbitlbl |label=0x13A |value=terran\NukeSilT.grp}}
    {{formatbitlbl |label=0x13B |value=terran\tnsShad.grp}}
    {{formatbitlbl |label=0x13C |value=terran\nukemiss.grp}}
    {{formatbitlbl |label=0x13D |value=terran\nukemiss.grp}}
    {{formatbitlbl |label=0x13E |value=thingy\NukeHit.grp}}
    {{formatbitlbl |label=0x13F |value=terran\starport.grp}}
    {{formatbitlbl |label=0x140 |value=terran\StarpoT.grp}}
    {{formatbitlbl |label=0x141 |value=terran\tspShad.grp}}
    {{formatbitlbl |label=0x142 |value=terran\weaponpl.grp}}
    {{formatbitlbl |label=0x143 |value=terran\weaponpT.grp}}
    {{formatbitlbl |label=0x144 |value=terran\twpShad.grp}}
    {{formatbitlbl |label=0x145 |value=terran\TBldLrg.grp}}
    {{formatbitlbl |label=0x146 |value=terran\tb2Shad.grp}}
    {{formatbitlbl |label=0x147 |value=terran\tBldMed.grp}}
    {{formatbitlbl |label=0x148 |value=terran\tb3Shad.grp}}
    {{formatbitlbl |label=0x149 |value=terran\TBldSml.grp}}
    {{formatbitlbl |label=0x14A |value=terran\TBldSml.grp}}
    {{formatbitlbl |label=0x14B |value=terran\tb1Shad.grp}}
    {{formatbitlbl |label=0x14C |value=thingy\tBangS.grp}}
    {{formatbitlbl |label=0x14D |value=thingy\tBangL.grp}}
    {{formatbitlbl |label=0x14E |value=thingy\tBangX.grp}}
    {{formatbitlbl |label=0x14F |value=thingy\RubbleS.grp}}
    {{formatbitlbl |label=0x150 |value=thingy\RubbleL.grp}}
    {{formatbitlbl |label=0x151 |value=thingy\Dswarm.grp}}
    {{formatbitlbl |label=0x152 |value=neutral\Acritter.grp}}
    {{formatbitlbl |label=0x153 |value=neutral\nacShad.grp}}
    {{formatbitlbl |label=0x154 |value=neutral\Bcritter.grp}}
    {{formatbitlbl |label=0x155 |value=neutral\nbcShad.grp}}
    {{formatbitlbl |label=0x156 |value=neutral\Jcritter.grp}}
    {{formatbitlbl |label=0x157 |value=neutral\njcShad.grp}}
    {{formatbitlbl |label=0x158 |value=neutral\geyser.grp}}
    {{formatbitlbl |label=0x159 |value=neutral\geyser.grp}}
    {{formatbitlbl |label=0x15A |value=neutral\geyShad.grp}}
    {{formatbitlbl |label=0x15B |value=neutral\min01.grp}}
    {{formatbitlbl |label=0x15C |value=neutral\min01Sha.grp}}
    {{formatbitlbl |label=0x15D |value=neutral\min02.grp}}
    {{formatbitlbl |label=0x15E |value=neutral\min02Sha.grp}}
    {{formatbitlbl |label=0x15F |value=neutral\min03.grp}}
    {{formatbitlbl |label=0x160 |value=neutral\min03Sha.grp}}
    {{formatbitlbl |label=0x161 |value=protoss\scout.grp}}
    {{formatbitlbl |label=0x162 |value=zerg\zmarker.grp}}
    {{formatbitlbl |label=0x163 |value=zerg\zCirGlow.grp}}
    {{formatbitlbl |label=0x164 |value=terran\tMarker.grp}}
    {{formatbitlbl |label=0x165 |value=terran\tCirGlow.grp}}
    {{formatbitlbl |label=0x166 |value=protoss\pMarker.grp}}
    {{formatbitlbl |label=0x167 |value=protoss\pCirGlow.grp}}
    {{formatbitlbl |label=0x168 |value=thingy\eldFire.grp}}
    {{formatbitlbl |label=0x169 |value=thingy\eldSmall.grp}}
    {{formatbitlbl |label=0x16A |value=thingy\eldMed.grp}}
    {{formatbitlbl |label=0x16B |value=thingy\eldLarge.grp}}
    {{formatbitlbl |label=0x16C |value=thingy\esfHit.grp}}
    {{formatbitlbl |label=0x16D |value=thingy\esfSmall.grp}}
    {{formatbitlbl |label=0x16E |value=thingy\esfSmall.grp}}
    {{formatbitlbl |label=0x16F |value=thingy\esfLarge.grp}}
    {{formatbitlbl |label=0x170 |value=thingy\sbaSmall.grp}}
    {{formatbitlbl |label=0x171 |value=thingy\sbaSmall.grp}}
    {{formatbitlbl |label=0x172 |value=thingy\sbaLarge.grp}}
    {{formatbitlbl |label=0x173 |value=thingy\edmFronS.grp}}
    {{formatbitlbl |label=0x174 |value=thingy\edmFronM.grp}}
    {{formatbitlbl |label=0x175 |value=thingy\edmFronL.grp}}
    {{formatbitlbl |label=0x176 |value=thingy\edmBackS.grp}}
    {{formatbitlbl |label=0x177 |value=thingy\edmBackM.grp}}
    {{formatbitlbl |label=0x178 |value=thingy\edmBackL.grp}}
    {{formatbitlbl |label=0x179 |value=thingy\edmHitS.grp}}
    {{formatbitlbl |label=0x17A |value=thingy\edmHitM.grp}}
    {{formatbitlbl |label=0x17B |value=thingy\edmHitL.grp}}
    {{formatbitlbl |label=0x17C |value=thingy\eradLrg.grp}}
    {{formatbitlbl |label=0x17D |value=thingy\eradLrg.grp}}
    {{formatbitlbl |label=0x17E |value=thingy\eradLrg.grp}}
    {{formatbitlbl |label=0x17F |value=thingy\Ensnare.grp}}
    {{formatbitlbl |label=0x180 |value=thingy\ensGooS.grp}}
    {{formatbitlbl |label=0x181 |value=thingy\ensGooM.grp}}
    {{formatbitlbl |label=0x182 |value=thingy\ensGooL.grp}}
    {{formatbitlbl |label=0x183 |value=thingy\ebbCloud.grp}}
    {{formatbitlbl |label=0x184 |value=thingy\ebbHitS.grp}}
    {{formatbitlbl |label=0x185 |value=thingy\ebbHitM.grp}}
    {{formatbitlbl |label=0x186 |value=thingy\ebbHitL.grp}}
    {{formatbitlbl |label=0x187 |value=thingy\recall.grp}}
    {{formatbitlbl |label=0x188 |value=neutral\Flag.grp}}
    {{formatbitlbl |label=0x189 |value=neutral\KerrEgg.grp}}
    {{formatbitlbl |label=0x18A |value=neutral\PsiEmit.grp}}
    {{formatbitlbl |label=0x18B |value=neutral\DataDisk.grp}}
    {{formatbitlbl |label=0x18C |value=neutral\KhChunk.grp}}
    {{formatbitlbl |label=0x18D |value=neutral\OreChunk.grp}}
    {{formatbitlbl |label=0x18E |value=neutral\OreChunk.grp}}
    {{formatbitlbl |label=0x18F |value=neutral\GasOrb.grp}}
    {{formatbitlbl |label=0x190 |value=neutral\GasOrb.grp}}
    {{formatbitlbl |label=0x191 |value=neutral\GasSac.grp}}
    {{formatbitlbl |label=0x192 |value=neutral\GasSac.grp}}
    {{formatbitlbl |label=0x193 |value=neutral\GasTank.grp}}
    {{formatbitlbl |label=0x194 |value=neutral\GasTank.grp}}
    {{formatbitlbl |label=0x195 |value=neutral\norShad.grp}}
    {{formatbitlbl |label=0x196 |value=neutral\ngoShad.grp}}
    {{formatbitlbl |label=0x197 |value=neutral\ngsShad.grp}}
    {{formatbitlbl |label=0x198 |value=neutral\ngcShad.grp}}
    {{formatbitlbl |label=0x199 |value=neutral\nddShad.grp}}
    {{formatbitlbl |label=0x19A |value=neutral\nddSha2.grp}}
    {{formatbitlbl |label=0x19B |value=neutral\nflShad.grp}}
    {{formatbitlbl |label=0x19C |value=neutral\nflSha2.grp}}
    {{formatbitlbl |label=0x19D |value=neutral\nkhShad.grp}}
    {{formatbitlbl |label=0x19E |value=neutral\nkhSha2.grp}}
    {{formatbitlbl |label=0x19F |value=neutral\nkeShad.grp}}
    {{formatbitlbl |label=0x1A0 |value=neutral\nkeSha2.grp}}
    {{formatbitlbl |label=0x1A1 |value=neutral\npsShad.grp}}
    {{formatbitlbl |label=0x1A2 |value=neutral\npsSha2.grp}}
    {{formatbitlbl |label=0x1A3 |value=thingy\plasma.grp}}
    {{formatbitlbl |label=0x1A4 |value=thingy\PlasDrip.grp}}
    {{formatbitlbl |label=0x1A5 |value=thingy\flamer.grp}}
    {{formatbitlbl |label=0x1A6 |value=thingy\smoke.grp}}
    {{formatbitlbl |label=0x1A7 |value=thingy\bDust.grp}}
    {{formatbitlbl |label=0x1A8 |value=thingy\pshield.grp}}
    {{formatbitlbl |label=0x1A9 |value=thingy\explo2.grp}}
    {{formatbitlbl |label=0x1AA |value=thingy\dbl_exp.grp}}
    {{formatbitlbl |label=0x1AB |value=thingy\HKexplod.grp}}
    {{formatbitlbl |label=0x1AC |value=thingy\small.grp}}
    {{formatbitlbl |label=0x1AD |value=thingy\tmnExplo.grp}}
    {{formatbitlbl |label=0x1AE |value=thingy\GeySmok1.grp}}
    {{formatbitlbl |label=0x1AF |value=thingy\GeySmok2.grp}}
    {{formatbitlbl |label=0x1B0 |value=thingy\GeySmok3.grp}}
    {{formatbitlbl |label=0x1B1 |value=thingy\GeySmok4.grp}}
    {{formatbitlbl |label=0x1B2 |value=thingy\GeySmok5.grp}}
    {{formatbitlbl |label=0x1B3 |value=thingy\GeySmoS1.grp}}
    {{formatbitlbl |label=0x1B4 |value=thingy\GeySmoS1.grp}}
    {{formatbitlbl |label=0x1B5 |value=thingy\GeySmoS1.grp}}
    {{formatbitlbl |label=0x1B6 |value=thingy\GeySmoS1.grp}}
    {{formatbitlbl |label=0x1B7 |value=thingy\GeySmoS1.grp}}
    {{formatbitlbl |label=0x1B8 |value=thingy\efgHit.grp}}
    {{formatbitlbl |label=0x1B9 |value=thingy\GreSmoke.grp}}
    {{formatbitlbl |label=0x1BA |value=thingy\HKexplod.grp}}
    {{formatbitlbl |label=0x1BB |value=thingy\HKTrail.grp}}
    {{formatbitlbl |label=0x1BC |value=thingy\psaExplo.grp}}
    {{formatbitlbl |label=0x1BD |value=thingy\blackx.grp}}
    {{formatbitlbl |label=0x1BE |value=thingy\elbBat.grp}}
    {{formatbitlbl |label=0x1BF |value=thingy\elbHit.grp}}
    {{formatbitlbl |label=0x1C0 |value=thingy\elbMuzz.grp}}
    {{formatbitlbl |label=0x1C1 |value=thingy\pteglow.grp}}
    {{formatbitlbl |label=0x1C2 |value=thingy\oFireC.grp}}
    {{formatbitlbl |label=0x1C3 |value=thingy\oFireF.grp}}
    {{formatbitlbl |label=0x1C4 |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1C5 |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1C6 |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1C7 |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1C8 |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1C9 |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1CA |value=thingy\bblood01.grp}}
    {{formatbitlbl |label=0x1CB |value=thingy\bblood02.grp}}
    {{formatbitlbl |label=0x1CC |value=thingy\bblood03.grp}}
    {{formatbitlbl |label=0x1CD |value=thingy\bblood04.grp}}
    {{formatbitlbl |label=0x1CE |value=thingy\bblood01.grp}}
    {{formatbitlbl |label=0x1CF |value=thingy\bblood02.grp}}
    {{formatbitlbl |label=0x1D0 |value=thingy\bblood03.grp}}
    {{formatbitlbl |label=0x1D1 |value=thingy\bblood04.grp}}
    {{formatbitlbl |label=0x1D2 |value=thingy\oFireC.grp}}
    {{formatbitlbl |label=0x1D3 |value=thingy\oFireF.grp}}
    {{formatbitlbl |label=0x1D4 |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1D5 |value=thingy\oFireC.grp}}
    {{formatbitlbl |label=0x1D6 |value=thingy\oFireF.grp}}
    {{formatbitlbl |label=0x1D7 |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1D8 |value=thingy\oFireC.grp}}
    {{formatbitlbl |label=0x1D9 |value=thingy\oFireF.grp}}
    {{formatbitlbl |label=0x1DA |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1DB |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1DC |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1DD |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1DE |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1DF |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1E0 |value=thingy\bblood01.grp}}
    {{formatbitlbl |label=0x1E1 |value=thingy\bblood02.grp}}
    {{formatbitlbl |label=0x1E2 |value=thingy\bblood03.grp}}
    {{formatbitlbl |label=0x1E3 |value=thingy\bblood04.grp}}
    {{formatbitlbl |label=0x1E4 |value=thingy\bblood01.grp}}
    {{formatbitlbl |label=0x1E5 |value=thingy\bblood02.grp}}
    {{formatbitlbl |label=0x1E6 |value=thingy\bblood03.grp}}
    {{formatbitlbl |label=0x1E7 |value=thingy\bblood04.grp}}
    {{formatbitlbl |label=0x1E8 |value=thingy\oFireC.grp}}
    {{formatbitlbl |label=0x1E9 |value=thingy\oFireF.grp}}
    {{formatbitlbl |label=0x1EA |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1EB |value=thingy\oFireC.grp}}
    {{formatbitlbl |label=0x1EC |value=thingy\oFireF.grp}}
    {{formatbitlbl |label=0x1ED |value=thingy\oFireV.grp}}
    {{formatbitlbl |label=0x1EE |value=thingy\dust01.grp}}
    {{formatbitlbl |label=0x1EF |value=thingy\dust02.grp}}
    {{formatbitlbl |label=0x1F0 |value=thingy\dust03.grp}}
    {{formatbitlbl |label=0x1F1 |value=thingy\dust04.grp}}
    {{formatbitlbl |label=0x1F2 |value=thingy\dust05.grp}}
    {{formatbitlbl |label=0x1F3 |value=thingy\dust06.grp}}
    {{formatbitlbl |label=0x1F4 |value=thingy\dust07.grp}}
    {{formatbitlbl |label=0x1F5 |value=thingy\dust08.grp}}
    {{formatbitlbl |label=0x1F6 |value=thingy\dust09.grp}}
    {{formatbitlbl |label=0x1F7 |value=bullet\circle14.grp}}
    {{formatbitlbl |label=0x1F8 |value=bullet\zspark.grp}}
    {{formatbitlbl |label=0x1F9 |value=bullet\PDripHit.grp}}
    {{formatbitlbl |label=0x1FA |value=bullet\Tentacle.grp}}
    {{formatbitlbl |label=0x1FB |value=thingy\ep2Fire.grp}}
    {{formatbitlbl |label=0x1FC |value=thingy\etgHit.grp}}
    {{formatbitlbl |label=0x1FD |value=thingy\ep3Shot.grp}}
    {{formatbitlbl |label=0x1FE |value=thingy\ep3Burst.grp}}
    {{formatbitlbl |label=0x1FF |value=bullet\spores.grp}}
    {{formatbitlbl |label=0x200 |value=thingy\SporeHit.grp}}
    {{formatbitlbl |label=0x201 |value=thingy\SpoTrail.grp}}
    {{formatbitlbl |label=0x202 |value=thingy\gSmoke.grp}}
    {{formatbitlbl |label=0x203 |value=bullet\Spore2.grp}}
    {{formatbitlbl |label=0x204 |value=bullet\parasite.grp}}
    {{formatbitlbl |label=0x205 |value=thingy\consume.grp}}
    {{formatbitlbl |label=0x206 |value=thingy\eplMuzz.grp}}
    {{formatbitlbl |label=0x207 |value=bullet\pspark.grp}}
    {{formatbitlbl |label=0x208 |value=bullet\ephFire.grp}}
    {{formatbitlbl |label=0x209 |value=bullet\hks.grp}}
    {{formatbitlbl |label=0x20A |value=bullet\blastcan.grp}}
    {{formatbitlbl |label=0x20B |value=bullet\dragbull.grp}}
    {{formatbitlbl |label=0x20C |value=bullet\epbBul.grp}}
    {{formatbitlbl |label=0x20D |value=thingy\psiStorm.grp}}
    {{formatbitlbl |label=0x20E |value=bullet\scvspark.grp}}
    {{formatbitlbl |label=0x20F |value=bullet\tspark.grp}}
    {{formatbitlbl |label=0x210 |value=bullet\gemini.grp}}
    {{formatbitlbl |label=0x211 |value=bullet\missile.grp}}
    {{formatbitlbl |label=0x212 |value=thingy\ecaHit.grp}}
    {{formatbitlbl |label=0x213 |value=thingy\ecaHit.grp}}
    {{formatbitlbl |label=0x214 |value=bullet\grenade.grp}}
    {{formatbitlbl |label=0x215 |value=thingy\mushroom.grp}}
    {{formatbitlbl |label=0x216 |value=thingy\elbfire.grp}}
    {{formatbitlbl |label=0x217 |value=thingy\elbfireW.grp}}
    {{formatbitlbl |label=0x218 |value=thingy\ettFlash.grp}}
    {{formatbitlbl |label=0x219 |value=thingy\esiFire.grp}}
    {{formatbitlbl |label=0x21A |value=thingy\tveGlowB.grp}}
    {{formatbitlbl |label=0x21B |value=thingy\tveGlowO.grp}}
    {{formatbitlbl |label=0x21C |value=thingy\tveGlowW.grp}}
    {{formatbitlbl |label=0x21D |value=bullet\eycBull.grp}}
    {{formatbitlbl |label=0x21E |value=bullet\eycBull.grp}}
    {{formatbitlbl |label=0x21F |value=thingy\eycBlast.grp}}
    {{formatbitlbl |label=0x220 |value=thingy\eycHit.grp}}
    {{formatbitlbl |label=0x221 |value=thingy\halmind.grp}}
    {{formatbitlbl |label=0x222 |value=thingy\eveCast.grp}}
    {{formatbitlbl |label=0x223 |value=thingy\emsHit.grp}}
    {{formatbitlbl |label=0x224 |value=thingy\emsHit.grp}}
    {{formatbitlbl |label=0x225 |value=thingy\emsBeam.grp}}
    {{formatbitlbl |label=0x226 |value=thingy\elect02a.grp}}
    {{formatbitlbl |label=0x227 |value=thingy\elect02.grp}}
    {{formatbitlbl |label=0x228 |value=thingy\elect02a.grp}}
    {{formatbitlbl |label=0x229 |value=thingy\elect02.grp}}
    {{formatbitlbl |label=0x22A |value=bullet\missile.grp}}
    {{formatbitlbl |label=0x22B |value=thingy\emp.grp}}
    {{formatbitlbl |label=0x22C |value=thingy\empl.grp}}
    {{formatbitlbl |label=0x22D |value=thingy\ehaMed.grp}}
    {{formatbitlbl |label=0x22E |value=thingy\ehaMed.grp}}
    {{formatbitlbl |label=0x22F |value=thingy\ehaMed.grp}}
    {{formatbitlbl |label=0x230 |value=thingy\blackx.grp}}
    {{formatbitlbl |label=0x231 |value=thingy\o022.grp}}
    {{formatbitlbl |label=0x232 |value=thingy\o032.grp}}
    {{formatbitlbl |label=0x233 |value=thingy\o048.grp}}
    {{formatbitlbl |label=0x234 |value=thingy\o062.grp}}
    {{formatbitlbl |label=0x235 |value=thingy\o072.grp}}
    {{formatbitlbl |label=0x236 |value=thingy\o094.grp}}
    {{formatbitlbl |label=0x237 |value=thingy\o110.grp}}
    {{formatbitlbl |label=0x238 |value=thingy\o122.grp}}
    {{formatbitlbl |label=0x239 |value=thingy\o146.grp}}
    {{formatbitlbl |label=0x23A |value=thingy\o224.grp}}
    {{formatbitlbl |label=0x23B |value=thingy\od022.grp}}
    {{formatbitlbl |label=0x23C |value=thingy\od032.grp}}
    {{formatbitlbl |label=0x23D |value=thingy\od048.grp}}
    {{formatbitlbl |label=0x23E |value=thingy\od062.grp}}
    {{formatbitlbl |label=0x23F |value=thingy\od072.grp}}
    {{formatbitlbl |label=0x240 |value=thingy\od094.grp}}
    {{formatbitlbl |label=0x241 |value=thingy\od110.grp}}
    {{formatbitlbl |label=0x242 |value=thingy\od122.grp}}
    {{formatbitlbl |label=0x243 |value=thingy\od146.grp}}
    {{formatbitlbl |label=0x244 |value=thingy\od224.grp}}
    {{formatbitlbl |label=0x245 |value=thingy\blackx.grp}}
    {{formatbitlbl |label=0x246 |value=neutral\maprev.grp}}
    {{formatbitlbl |label=0x247 |value=thingy\blackx.grp}}
    {{formatbitlbl |label=0x248 |value=thingy\Juice01.grp}}
    {{formatbitlbl |label=0x249 |value=thingy\Juice02.grp}}
    {{formatbitlbl |label=0x24A |value=thingy\Juice01.grp}}
    {{formatbitlbl |label=0x24B |value=thingy\Juice02.grp}}
    {{formatbitlbl |label=0x24C |value=thingy\StartLoc.grp}}
    {{formatbitlbl |label=0x24D |value=thingy\tileset\AshWorld\rock01.grp}}
    {{formatbitlbl |label=0x24E |value=thingy\tileset\AshWorld\Rock1Sha.grp}}
    {{formatbitlbl |label=0x24F |value=thingy\tileset\AshWorld\rock02.grp}}
    {{formatbitlbl |label=0x250 |value=thingy\tileset\AshWorld\Rock2Sha.grp}}
    {{formatbitlbl |label=0x251 |value=thingy\tileset\AshWorld\rock03.grp}}
    {{formatbitlbl |label=0x252 |value=thingy\tileset\AshWorld\Rock3Sha.grp}}
    {{formatbitlbl |label=0x253 |value=thingy\tileset\AshWorld\rock04.grp}}
    {{formatbitlbl |label=0x254 |value=thingy\tileset\AshWorld\Rock4Sha.grp}}
    {{formatbitlbl |label=0x255 |value=thingy\tileset\AshWorld\rock05.grp}}
    {{formatbitlbl |label=0x256 |value=thingy\tileset\AshWorld\Rock5Sha.grp}}
    {{formatbitlbl |label=0x257 |value=thingy\tileset\AshWorld\LALRoc01.grp}}
    {{formatbitlbl |label=0x258 |value=thingy\tileset\AshWorld\LALRoc02.grp}}
    {{formatbitlbl |label=0x259 |value=thingy\tileset\AshWorld\HASRoc01.grp}}
    {{formatbitlbl |label=0x25A |value=thingy\tileset\AshWorld\HASRoc02.grp}}
    {{formatbitlbl |label=0x25B |value=thingy\tileset\AshWorld\HASRoc03.grp}}
    {{formatbitlbl |label=0x25C |value=thingy\tileset\AshWorld\HASRoc04.grp}}
    {{formatbitlbl |label=0x25D |value=thingy\tileset\AshWorld\HASRoc05.grp}}
    {{formatbitlbl |label=0x25E |value=thingy\tileset\AshWorld\HASRoc06.grp}}
    {{formatbitlbl |label=0x25F |value=thingy\tileset\AshWorld\RORock01.grp}}
    {{formatbitlbl |label=0x260 |value=thingy\tileset\AshWorld\RORock02.grp}}
    {{formatbitlbl |label=0x261 |value=thingy\tileset\AshWorld\RORock03.grp}}
    {{formatbitlbl |label=0x262 |value=thingy\tileset\Jungle\HDRock01.grp}}
    {{formatbitlbl |label=0x263 |value=thingy\tileset\Jungle\HDRock1s.grp}}
    {{formatbitlbl |label=0x264 |value=thingy\tileset\Jungle\HDRock02.grp}}
    {{formatbitlbl |label=0x265 |value=thingy\tileset\Jungle\HDRock2s.grp}}
    {{formatbitlbl |label=0x266 |value=thingy\tileset\Jungle\HDRock03.grp}}
    {{formatbitlbl |label=0x267 |value=thingy\tileset\Jungle\HDRock3s.grp}}
    {{formatbitlbl |label=0x268 |value=thingy\tileset\Jungle\HDRock04.grp}}
    {{formatbitlbl |label=0x269 |value=thingy\tileset\Jungle\HDRock4s.grp}}
    {{formatbitlbl |label=0x26A |value=thingy\tileset\Jungle\JUbush01.grp}}
    {{formatbitlbl |label=0x26B |value=thingy\tileset\Jungle\JUbush1S.grp}}
    {{formatbitlbl |label=0x26C |value=thingy\tileset\Jungle\JUbush03.grp}}
    {{formatbitlbl |label=0x26D |value=thingy\tileset\Jungle\JUbush3s.grp}}
    {{formatbitlbl |label=0x26E |value=thingy\tileset\Jungle\JUbush05.grp}}
    {{formatbitlbl |label=0x26F |value=thingy\tileset\Jungle\JUbush5s.grp}}
    {{formatbitlbl |label=0x270 |value=thingy\tileset\Jungle\LDtree01.grp}}
    {{formatbitlbl |label=0x271 |value=thingy\tileset\Jungle\LDtree1s.grp}}
    {{formatbitlbl |label=0x272 |value=thingy\tileset\Jungle\LDtree02.grp}}
    {{formatbitlbl |label=0x273 |value=thingy\tileset\Jungle\LDtree2s.grp}}
    {{formatbitlbl |label=0x274 |value=thingy\tileset\Jungle\LDtree03.grp}}
    {{formatbitlbl |label=0x275 |value=thingy\tileset\Jungle\LDtree3s.grp}}
    {{formatbitlbl |label=0x276 |value=thingy\tileset\Jungle\LDtree04.grp}}
    {{formatbitlbl |label=0x277 |value=thingy\tileset\Jungle\LDtree4s.grp}}
    {{formatbitlbl |label=0x278 |value=thingy\tileset\Jungle\tree01.grp}}
    {{formatbitlbl |label=0x279 |value=thingy\tileset\Jungle\tree1sha.grp}}
    {{formatbitlbl |label=0x27A |value=thingy\tileset\Jungle\tree02.grp}}
    {{formatbitlbl |label=0x27B |value=thingy\tileset\Jungle\tree2sha.grp}}
    {{formatbitlbl |label=0x27C |value=thingy\tileset\Jungle\tree03.grp}}
    {{formatbitlbl |label=0x27D |value=thingy\tileset\Jungle\tree3sha.grp}}
    {{formatbitlbl |label=0x27E |value=thingy\tileset\Jungle\tree04.grp}}
    {{formatbitlbl |label=0x27F |value=thingy\tileset\Jungle\tree4sha.grp}}
    {{formatbitlbl |label=0x280 |value=thingy\tileset\Jungle\dd025.grp}}
    {{formatbitlbl |label=0x281 |value=thingy\tileset\Jungle\dd026.grp}}
    {{formatbitlbl |label=0x282 |value=thingy\tileset\Jungle\dd027.grp}}
    {{formatbitlbl |label=0x283 |value=thingy\tileset\Jungle\dd028.grp}}
    {{formatbitlbl |label=0x284 |value=thingy\tileset\Jungle\dd029.grp}}
    {{formatbitlbl |label=0x285 |value=thingy\tileset\Jungle\dd030.grp}}
    {{formatbitlbl |label=0x286 |value=thingy\tileset\Jungle\dd031.grp}}
    {{formatbitlbl |label=0x287 |value=thingy\tileset\Jungle\dd055.grp}}
    {{formatbitlbl |label=0x288 |value=thingy\tileset\Jungle\dd056.grp}}
    {{formatbitlbl |label=0x289 |value=thingy\tileset\Jungle\dd075.grp}}
    {{formatbitlbl |label=0x28A |value=thingy\tileset\Jungle\dd076.grp}}
    {{formatbitlbl |label=0x28B |value=thingy\tileset\Jungle\dd077.grp}}
    {{formatbitlbl |label=0x28C |value=thingy\tileset\Jungle\dd078.grp}}
    {{formatbitlbl |label=0x28D |value=thingy\tileset\Jungle\dd079.grp}}
    {{formatbitlbl |label=0x28E |value=thingy\tileset\Jungle\dd080.grp}}
    {{formatbitlbl |label=0x28F |value=thingy\tileset\Jungle\dd081.grp}}
    {{formatbitlbl |label=0x290 |value=thingy\tileset\Jungle\dd091.grp}}
    {{formatbitlbl |label=0x291 |value=thingy\tileset\Jungle\dd203.grp}}
    {{formatbitlbl |label=0x292 |value=thingy\tileset\Jungle\dd204.grp}}
    {{formatbitlbl |label=0x293 |value=thingy\tileset\Jungle\dd205.grp}}
    {{formatbitlbl |label=0x294 |value=thingy\tileset\Jungle\dd206.grp}}
    {{formatbitlbl |label=0x295 |value=thingy\tileset\Jungle\dd207.grp}}
    {{formatbitlbl |label=0x296 |value=thingy\tileset\Jungle\dd209.grp}}
    {{formatbitlbl |label=0x297 |value=thingy\tileset\Jungle\dd210.grp}}
    {{formatbitlbl |label=0x298 |value=thingy\tileset\Jungle\dd211.grp}}
    {{formatbitlbl |label=0x299 |value=thingy\tileset\Platform\Dish01.grp}}
    {{formatbitlbl |label=0x29A |value=thingy\tileset\Platform\Dish1Sha.grp}}
    {{formatbitlbl |label=0x29B |value=thingy\tileset\Platform\Dish02.grp}}
    {{formatbitlbl |label=0x29C |value=thingy\tileset\Platform\Dish2Sha.grp}}
    {{formatbitlbl |label=0x29D |value=thingy\tileset\Platform\Dish03.grp}}
    {{formatbitlbl |label=0x29E |value=thingy\tileset\Platform\Dish3Sha.grp}}
    {{formatbitlbl |label=0x29F |value=thingy\tileset\Platform\Glob01.grp}}
    {{formatbitlbl |label=0x2A0 |value=thingy\tileset\Platform\Glob1Sha.grp}}
    {{formatbitlbl |label=0x2A1 |value=thingy\tileset\Platform\Glob02.grp}}
    {{formatbitlbl |label=0x2A2 |value=thingy\tileset\Platform\Glob2Sha.grp}}
    {{formatbitlbl |label=0x2A3 |value=thingy\tileset\Platform\Glob03.grp}}
    {{formatbitlbl |label=0x2A4 |value=thingy\tileset\Platform\Glob3Sha.grp}}
    {{formatbitlbl |label=0x2A5 |value=thingy\tileset\Platform\Towr01.grp}}
    {{formatbitlbl |label=0x2A6 |value=thingy\tileset\Platform\Towr02.grp}}
    {{formatbitlbl |label=0x2A7 |value=thingy\tileset\Platform\tree01.grp}}
    {{formatbitlbl |label=0x2A8 |value=thingy\tileset\Platform\tree02.grp}}
    {{formatbitlbl |label=0x2A9 |value=thingy\tileset\Platform\LBSign01.grp}}
    {{formatbitlbl |label=0x2AA |value=thingy\tileset\Platform\LBSign02.grp}}
    {{formatbitlbl |label=0x2AB |value=thingy\tileset\Platform\LBSign03.grp}}
    {{formatbitlbl |label=0x2AC |value=thingy\tileset\Platform\LBSign04.grp}}
    {{formatbitlbl |label=0x2AD |value=thingy\tileset\Platform\LBSign05.grp}}
    {{formatbitlbl |label=0x2AE |value=thingy\tileset\Platform\LBSign06.grp}}
    {{formatbitlbl |label=0x2AF |value=thingy\tileset\Platform\LBSign07.grp}}
    {{formatbitlbl |label=0x2B0 |value=thingy\tileset\Platform\LBSign08.grp}}
    {{formatbitlbl |label=0x2B1 |value=thingy\tileset\Platform\SPThin01.grp}}
    {{formatbitlbl |label=0x2B2 |value=thingy\tileset\Platform\refinery.grp}}
    {{formatbitlbl |label=0x2B3 |value=thingy\tileset\Badlands\HDRock01.grp}}
    {{formatbitlbl |label=0x2B4 |value=thingy\tileset\Badlands\HDRock1S.grp}}
    {{formatbitlbl |label=0x2B5 |value=thingy\tileset\Badlands\HDRock02.grp}}
    {{formatbitlbl |label=0x2B6 |value=thingy\tileset\Badlands\HDRock2S.grp}}
    {{formatbitlbl |label=0x2B7 |value=thingy\tileset\Badlands\HDRock03.grp}}
    {{formatbitlbl |label=0x2B8 |value=thingy\tileset\Badlands\HDRock3S.grp}}
    {{formatbitlbl |label=0x2B9 |value=thingy\tileset\Badlands\HDRock04.grp}}
    {{formatbitlbl |label=0x2BA |value=thingy\tileset\Badlands\HDRock4S.grp}}
    {{formatbitlbl |label=0x2BB |value=thingy\tileset\Badlands\HDRock05.grp}}
    {{formatbitlbl |label=0x2BC |value=thingy\tileset\Badlands\HDRock06.grp}}
    {{formatbitlbl |label=0x2BD |value=thingy\tileset\Badlands\HDRock07.grp}}
    {{formatbitlbl |label=0x2BE |value=thingy\tileset\Badlands\HDRock08.grp}}
    {{formatbitlbl |label=0x2BF |value=thingy\tileset\Badlands\HDVent01.grp}}
    {{formatbitlbl |label=0x2C0 |value=thingy\tileset\Badlands\HDTree01.grp}}
    {{formatbitlbl |label=0x2C1 |value=thingy\tileset\Badlands\LDTree1S.grp}}
    {{formatbitlbl |label=0x2C2 |value=thingy\tileset\Badlands\HDTree02.grp}}
    {{formatbitlbl |label=0x2C3 |value=thingy\tileset\Badlands\LDTree2S.grp}}
    {{formatbitlbl |label=0x2C4 |value=thingy\tileset\Badlands\HDTree03.grp}}
    {{formatbitlbl |label=0x2C5 |value=thingy\tileset\Badlands\LDTree3S.grp}}
    {{formatbitlbl |label=0x2C6 |value=thingy\tileset\Badlands\HDTree04.grp}}
    {{formatbitlbl |label=0x2C7 |value=thingy\tileset\Badlands\LDTree4S.grp}}
    {{formatbitlbl |label=0x2C8 |value=thingy\tileset\Badlands\HGTree01.grp}}
    {{formatbitlbl |label=0x2C9 |value=thingy\tileset\Badlands\LCShop01.grp}}
    {{formatbitlbl |label=0x2CA |value=thingy\tileset\Badlands\LCShop02.grp}}
    {{formatbitlbl |label=0x2CB |value=thingy\tileset\Badlands\LCShop03.grp}}
    {{formatbitlbl |label=0x2CC |value=thingy\tileset\Badlands\LCShop04.grp}}
    {{formatbitlbl |label=0x2CD |value=thingy\tileset\Badlands\LCShop05.grp}}
    {{formatbitlbl |label=0x2CE |value=thingy\tileset\Badlands\LCShop06.grp}}
    {{formatbitlbl |label=0x2CF |value=thingy\tileset\Badlands\LCShop07.grp}}
    {{formatbitlbl |label=0x2D0 |value=thingy\tileset\Badlands\LCShop08.grp}}
    {{formatbitlbl |label=0x2D1 |value=thingy\tileset\Badlands\LCShop09.grp}}
    {{formatbitlbl |label=0x2D2 |value=thingy\tileset\Badlands\LCShopAA.grp}}
    {{formatbitlbl |label=0x2D3 |value=thingy\tileset\Badlands\LCSign01.grp}}
    {{formatbitlbl |label=0x2D4 |value=thingy\tileset\Badlands\LCSign02.grp}}
    {{formatbitlbl |label=0x2D5 |value=thingy\tileset\Badlands\LCSign03.grp}}
    {{formatbitlbl |label=0x2D6 |value=thingy\tileset\Badlands\LCSign04.grp}}
    {{formatbitlbl |label=0x2D7 |value=thingy\tileset\Badlands\LCSign05.grp}}
    {{formatbitlbl |label=0x2D8 |value=thingy\tileset\Badlands\LCSign06.grp}}
    {{formatbitlbl |label=0x2D9 |value=thingy\tileset\Badlands\LCSign07.grp}}
    {{formatbitlbl |label=0x2DA |value=thingy\tileset\Badlands\LCSign08.grp}}
    {{formatbitlbl |label=0x2DB |value=thingy\tileset\Badlands\LCSign09.grp}}
    {{formatbitlbl |label=0x2DC |value=thingy\tileset\Badlands\LCSignAA.grp}}
    {{formatbitlbl |label=0x2DD |value=thingy\tileset\Badlands\LCSignBB.grp}}
    {{formatbitlbl |label=0x2DE |value=thingy\tileset\Badlands\LCSignCC.grp}}
    {{formatbitlbl |label=0x2DF |value=thingy\tileset\install\CLPlate2.grp}}
    {{formatbitlbl |label=0x2E0 |value=thingy\tileset\install\CLPlate1.grp}}
    {{formatbitlbl |label=0x2E1 |value=thingy\tileset\install\CLPlat1T.grp}}
    {{formatbitlbl |label=0x2E2 |value=thingy\tileset\install\DCGun1.grp}}
    {{formatbitlbl |label=0x2E3 |value=thingy\tileset\install\DCGun1.grp}}
    {{formatbitlbl |label=0x2E4 |value=thingy\tileset\install\DCGun2.grp}}
    {{formatbitlbl |label=0x2E5 |value=thingy\tileset\install\DCGun2.grp}}
    {{formatbitlbl |label=0x2E6 |value=thingy\tileset\install\CRDoor1.grp}}
    {{formatbitlbl |label=0x2E7 |value=thingy\tileset\install\CRDoor1.grp}}
    {{formatbitlbl |label=0x2E8 |value=thingy\tileset\install\DCFan1.grp}}
    {{formatbitlbl |label=0x2E9 |value=thingy\tileset\install\DCFan1.grp}}
    {{formatbitlbl |label=0x2EA |value=thingy\tileset\install\DICran1.grp}}
    {{formatbitlbl |label=0x2EB |value=thingy\tileset\install\DICran2.grp}}
    {{formatbitlbl |label=0x2EC |value=thingy\tileset\install\DICran3.grp}}
    {{formatbitlbl |label=0x2ED |value=thingy\tileset\install\DICran4.grp}}
    {{formatbitlbl |label=0x2EE |value=thingy\tileset\install\DIDoor1.grp}}
    {{formatbitlbl |label=0x2EF |value=thingy\tileset\install\DIDoor1.grp}}
    {{formatbitlbl |label=0x2F0 |value=thingy\tileset\install\DIGear1.grp}}
    {{formatbitlbl |label=0x2F1 |value=thingy\tileset\install\DIGear2.grp}}
    {{formatbitlbl |label=0x2F2 |value=thingy\tileset\install\DIHatc1.grp}}
    {{formatbitlbl |label=0x2F3 |value=thingy\tileset\twilight\Ldarch.grp}}
    {{formatbitlbl |label=0x2F4 |value=thingy\tileset\twilight\Lddrill.grp}}
    {{formatbitlbl |label=0x2F5 |value=thingy\tileset\twilight\Ldxel01.grp}}
    {{formatbitlbl |label=0x2F6 |value=thingy\tileset\twilight\Ldxel02.grp}}
    {{formatbitlbl |label=0x2F7 |value=thingy\tileset\twilight\Ldxel03.grp}}
    {{formatbitlbl |label=0x2F8 |value=thingy\tileset\twilight\Ldxel04.grp}}
    {{formatbitlbl |label=0x2F9 |value=thingy\tileset\twilight\Ldxel05.grp}}
    {{formatbitlbl |label=0x2FA |value=thingy\tileset\twilight\Ldxel06.grp}}
    {{formatbitlbl |label=0x2FB |value=thingy\tileset\twilight\Ldxeltur.grp}}
    {{formatbitlbl |label=0x2FC |value=thingy\tileset\twilight\JTree01.grp}}
    {{formatbitlbl |label=0x2FD |value=thingy\tileset\twilight\JTree02.grp}}
    {{formatbitlbl |label=0x2FE |value=thingy\tileset\twilight\JTree03.grp}}
    {{formatbitlbl |label=0x2FF |value=thingy\tileset\twilight\JTree04.grp}}
    {{formatbitlbl |label=0x300 |value=thingy\tileset\twilight\JTree05.grp}}
    {{formatbitlbl |label=0x301 |value=thingy\tileset\twilight\rstatue.grp}}
    {{formatbitlbl |label=0x302 |value=thingy\tileset\twilight\rstatue.grp}}
    {{formatbitlbl |label=0x303 |value=thingy\tileset\ice\HDbld01.grp}}
    {{formatbitlbl |label=0x304 |value=thingy\tileset\ice\SHDbld01.grp}}
    {{formatbitlbl |label=0x305 |value=thingy\tileset\ice\HDbld02.grp}}
    {{formatbitlbl |label=0x306 |value=thingy\tileset\ice\SHDbld02.grp}}
    {{formatbitlbl |label=0x307 |value=thingy\tileset\ice\HDbld03.grp}}
    {{formatbitlbl |label=0x308 |value=thingy\tileset\ice\SHDbld03.grp}}
    {{formatbitlbl |label=0x309 |value=thingy\tileset\ice\HDbld04.grp}}
    {{formatbitlbl |label=0x30A |value=thingy\tileset\ice\SHDbld04.grp}}
    {{formatbitlbl |label=0x30B |value=thingy\tileset\ice\HDradarl.grp}}
    {{formatbitlbl |label=0x30C |value=thingy\tileset\ice\SHDradrl.grp}}
    {{formatbitlbl |label=0x30D |value=thingy\tileset\ice\HDradarR.grp}}
    {{formatbitlbl |label=0x30E |value=thingy\tileset\ice\SHDradrR.grp}}
    {{formatbitlbl |label=0x30F |value=thingy\tileset\ice\HDRock01.grp}}
    {{formatbitlbl |label=0x310 |value=thingy\tileset\ice\SHDRck01.grp}}
    {{formatbitlbl |label=0x311 |value=thingy\tileset\ice\HDRock02.grp}}
    {{formatbitlbl |label=0x312 |value=thingy\tileset\ice\SHDRck02.grp}}
    {{formatbitlbl |label=0x313 |value=thingy\tileset\ice\HDSTre01.grp}}
    {{formatbitlbl |label=0x314 |value=thingy\tileset\ice\HDSTre02.grp}}
    {{formatbitlbl |label=0x315 |value=thingy\tileset\ice\HDSTre03.grp}}
    {{formatbitlbl |label=0x316 |value=thingy\tileset\ice\HDSTre04.grp}}
    {{formatbitlbl |label=0x317 |value=thingy\tileset\ice\HDSpire.grp}}
    {{formatbitlbl |label=0x318 |value=thingy\tileset\ice\SHDSpire.grp}}
    {{formatbitlbl |label=0x319 |value=thingy\tileset\ice\HDTwr01.grp}}
    {{formatbitlbl |label=0x31A |value=thingy\tileset\ice\SHDTwr01.grp}}
    {{formatbitlbl |label=0x31B |value=thingy\tileset\ice\HDTwr02.grp}}
    {{formatbitlbl |label=0x31C |value=thingy\tileset\ice\SHDTwr02.grp}}
    {{formatbitlbl |label=0x31D |value=thingy\tileset\ice\LDBTre01.grp}}
    {{formatbitlbl |label=0x31E |value=thingy\tileset\ice\SLDBTre1.grp}}
    {{formatbitlbl |label=0x31F |value=thingy\tileset\ice\LDBTre02.grp}}
    {{formatbitlbl |label=0x320 |value=thingy\tileset\ice\SLDBTre2.grp}}
    {{formatbitlbl |label=0x321 |value=thingy\tileset\ice\LDBTre03.grp}}
    {{formatbitlbl |label=0x322 |value=thingy\tileset\ice\SLDBTre3.grp}}
    {{formatbitlbl |label=0x323 |value=thingy\tileset\ice\LDBTre04.grp}}
    {{formatbitlbl |label=0x324 |value=thingy\tileset\ice\SLDBTre4.grp}}
    {{formatbitlbl |label=0x325 |value=thingy\tileset\ice\LDbld01.grp}}
    {{formatbitlbl |label=0x326 |value=thingy\tileset\ice\SLDbld01.grp}}
    {{formatbitlbl |label=0x327 |value=thingy\tileset\ice\LDbld02.grp}}
    {{formatbitlbl |label=0x328 |value=thingy\tileset\ice\SLDbld02.grp}}
    {{formatbitlbl |label=0x329 |value=thingy\tileset\ice\LDComm.grp}}
    {{formatbitlbl |label=0x32A |value=thingy\tileset\ice\SLDComm.grp}}
    {{formatbitlbl |label=0x32B |value=thingy\tileset\ice\LDDtre01.grp}}
    {{formatbitlbl |label=0x32C |value=thingy\tileset\ice\SLDDtre1.grp}}
    {{formatbitlbl |label=0x32D |value=thingy\tileset\ice\LDDtre02.grp}}
    {{formatbitlbl |label=0x32E |value=thingy\tileset\ice\SLDDtre2.grp}}
    {{formatbitlbl |label=0x32F |value=thingy\tileset\ice\LDDish.grp}}
    {{formatbitlbl |label=0x330 |value=thingy\tileset\ice\SLDDish.grp}}
    {{formatbitlbl |label=0x331 |value=thingy\tileset\ice\LDRdr01.grp}}
    {{formatbitlbl |label=0x332 |value=thingy\tileset\ice\SLDRdr01.grp}}
    {{formatbitlbl |label=0x333 |value=thingy\tileset\ice\LDRdr02.grp}}
    {{formatbitlbl |label=0x334 |value=thingy\tileset\ice\SLDRdr02.grp}}
    {{formatbitlbl |label=0x335 |value=thingy\tileset\ice\LDRdr03.grp}}
    {{formatbitlbl |label=0x336 |value=thingy\tileset\ice\SLDRdr03.grp}}
    {{formatbitlbl |label=0x337 |value=thingy\tileset\ice\LDRck01.grp}}
    {{formatbitlbl |label=0x338 |value=thingy\tileset\ice\SLDRck01.grp}}
    {{formatbitlbl |label=0x339 |value=thingy\tileset\ice\LDRck02.grp}}
    {{formatbitlbl |label=0x33A |value=thingy\tileset\ice\SLDRck02.grp}}
    {{formatbitlbl |label=0x33B |value=thingy\tileset\ice\HDPipes.grp}}
    {{formatbitlbl |label=0x33C |value=thingy\tileset\ice\SHDPipes.grp}}
    {{formatbitlbl |label=0x33D |value=thingy\tileset\ice\LDthing.grp}}
    {{formatbitlbl |label=0x33E |value=thingy\tileset\ice\SLDthing.grp}}
    {{formatbitlbl |label=0x33F |value=thingy\tileset\ice\LDsmrock.grp}}
    {{formatbitlbl |label=0x340 |value=thingy\tileset\ice\HDPipes.grp}}
    {{formatbitlbl |label=0x341 |value=thingy\tileset\ice\SHDPipes.grp}}
    {{formatbitlbl |label=0x342 |value=thingy\tileset\ice\HDRadr02.grp}}
    {{formatbitlbl |label=0x343 |value=thingy\tileset\ice\SHDRadr2.grp}}
    {{formatbitlbl |label=0x344 |value=thingy\tileset\ice\LDRck01.grp}}
    {{formatbitlbl |label=0x345 |value=thingy\tileset\ice\SLDRck01.grp}}
    {{formatbitlbl |label=0x346 |value=thingy\tileset\ice\LDRck02.grp}}
    {{formatbitlbl |label=0x347 |value=thingy\tileset\ice\SLDRck02.grp}}
    {{formatbitlbl |label=0x348 |value=thingy\tileset\ice\HDRadr02.grp}}
    {{formatbitlbl |label=0x349 |value=thingy\tileset\ice\JGant1.grp}}
    {{formatbitlbl |label=0x34A |value=thingy\tileset\ice\JGant1.grp}}
    {{formatbitlbl |label=0x34B |value=thingy\tileset\ice\RJBTree1.grp}}
    {{formatbitlbl |label=0x34C |value=thingy\tileset\ice\sRJBTre1.grp}}
    {{formatbitlbl |label=0x34D |value=thingy\tileset\ice\RJBTree2.grp}}
    {{formatbitlbl |label=0x34E |value=thingy\tileset\ice\sRJBTre2.grp}}
    {{formatbitlbl |label=0x34F |value=thingy\tileset\ice\RJBTree3.grp}}
    {{formatbitlbl |label=0x350 |value=thingy\tileset\ice\sRJBTre3.grp}}
    {{formatbitlbl |label=0x351 |value=thingy\tileset\ice\RJBTree4.grp}}
    {{formatbitlbl |label=0x352 |value=thingy\tileset\ice\sRJBTre4.grp}}
    {{formatbitlbl |label=0x353 |value=thingy\tileset\desert\HDBANT.grp}}
    {{formatbitlbl |label=0x354 |value=thingy\tileset\desert\HDBBROKE.grp}}
    {{formatbitlbl |label=0x355 |value=thingy\tileset\desert\SHDBBRKE.grp}}
    {{formatbitlbl |label=0x356 |value=thingy\tileset\desert\HDBGAS.grp}}
    {{formatbitlbl |label=0x357 |value=thingy\tileset\desert\SHDBGAS.grp}}
    {{formatbitlbl |label=0x358 |value=thingy\tileset\desert\HDBMED.grp}}
    {{formatbitlbl |label=0x359 |value=thingy\tileset\desert\SHDBMED.grp}}
    {{formatbitlbl |label=0x35A |value=thingy\tileset\desert\HDBMOSS.grp}}
    {{formatbitlbl |label=0x35B |value=thingy\tileset\desert\SHDBMOSS.grp}}
    {{formatbitlbl |label=0x35C |value=thingy\tileset\desert\HDBTENT.grp}}
    {{formatbitlbl |label=0x35D |value=thingy\tileset\desert\SHDBTENT.grp}}
    {{formatbitlbl |label=0x35E |value=thingy\tileset\desert\HDPLNT03.grp}}
    {{formatbitlbl |label=0x35F |value=thingy\tileset\desert\SHDPLNT3.grp}}
    {{formatbitlbl |label=0x360 |value=thingy\tileset\desert\JGBROKE.grp}}
    {{formatbitlbl |label=0x361 |value=thingy\tileset\desert\SJGBROKE.grp}}
    {{formatbitlbl |label=0x362 |value=thingy\tileset\desert\JGBGAS.grp}}
    {{formatbitlbl |label=0x363 |value=thingy\tileset\desert\SJGBGAS.grp}}
    {{formatbitlbl |label=0x364 |value=thingy\tileset\desert\JGBGEN.grp}}
    {{formatbitlbl |label=0x365 |value=thingy\tileset\desert\SJGBGEN.grp}}
    {{formatbitlbl |label=0x366 |value=thingy\tileset\desert\JGBSGN.grp}}
    {{formatbitlbl |label=0x367 |value=thingy\tileset\desert\SJGBSGN.grp}}
    {{formatbitlbl |label=0x368 |value=thingy\tileset\desert\JGBTENT.grp}}
    {{formatbitlbl |label=0x369 |value=thingy\tileset\desert\SJGBTENT.grp}}
    {{formatbitlbl |label=0x36A |value=thingy\tileset\desert\JGBCOMM.grp}}
    {{formatbitlbl |label=0x36B |value=thingy\tileset\desert\SJGBCOMM.grp}}
    {{formatbitlbl |label=0x36C |value=thingy\tileset\desert\JGBFACT.grp}}
    {{formatbitlbl |label=0x36D |value=thingy\tileset\desert\SJGBFACT.grp}}
    {{formatbitlbl |label=0x36E |value=thingy\tileset\desert\JGBRED.grp}}
    {{formatbitlbl |label=0x36F |value=thingy\tileset\desert\SJGBRED.grp}}
    {{formatbitlbl |label=0x370 |value=thingy\tileset\desert\JGPLNT01.grp}}
    {{formatbitlbl |label=0x371 |value=thingy\tileset\desert\JGPLNT02.grp}}
    {{formatbitlbl |label=0x372 |value=thingy\tileset\desert\SJGPLNT2.grp}}
    {{formatbitlbl |label=0x373 |value=thingy\tileset\desert\LDBAZ.grp}}
    {{formatbitlbl |label=0x374 |value=thingy\tileset\desert\SLDBAZ.grp}}
    {{formatbitlbl |label=0x375 |value=thingy\tileset\desert\LDBGAS.grp}}
    {{formatbitlbl |label=0x376 |value=thingy\tileset\desert\SLDBGAS.grp}}
    {{formatbitlbl |label=0x377 |value=thingy\tileset\desert\LDBGREN.grp}}
    {{formatbitlbl |label=0x378 |value=thingy\tileset\desert\SLDBGREN.grp}}
    {{formatbitlbl |label=0x379 |value=thingy\tileset\desert\LDBNEON.grp}}
    {{formatbitlbl |label=0x37A |value=thingy\tileset\desert\LDBSUKY.grp}}
    {{formatbitlbl |label=0x37B |value=thingy\tileset\desert\SLDBSUKY.grp}}
    {{formatbitlbl |label=0x37C |value=thingy\tileset\desert\LDBTENT.grp}}
    {{formatbitlbl |label=0x37D |value=thingy\tileset\desert\SLDBTENT.grp}}
    {{formatbitlbl |label=0x37E |value=thingy\tileset\desert\Ldneon.grp}}
    {{formatbitlbl |label=0x37F |value=thingy\tileset\desert\HDLbox01.grp}}
    {{formatbitlbl |label=0x380 |value=thingy\tileset\desert\SHDLbox1.grp}}
    {{formatbitlbl |label=0x381 |value=thingy\tileset\desert\HDMachn2.grp}}
    {{formatbitlbl |label=0x382 |value=thingy\tileset\desert\LDLbox01.grp}}
    {{formatbitlbl |label=0x383 |value=thingy\tileset\desert\SLDLbox1.grp}}
    {{formatbitlbl |label=0x384 |value=thingy\tileset\desert\LDMachn1.grp}}
    {{formatbitlbl |label=0x385 |value=thingy\tileset\desert\SLDMchn1.grp}}
    {{formatbitlbl |label=0x386 |value=thingy\tileset\desert\LDPlnt04.grp}}
    {{formatbitlbl |label=0x387 |value=thingy\tileset\desert\SLDPlnt4.grp}}
    {{formatbitlbl |label=0x388 |value=thingy\tileset\desert\HDLbox01.grp}}
    {{formatbitlbl |label=0x389 |value=thingy\tileset\desert\SHDLbox1.grp}}
    {{formatbitlbl |label=0x38A |value=thingy\tileset\desert\HDMachn2.grp}}
    {{formatbitlbl |label=0x38B |value=thingy\tileset\desert\LDLbox01.grp}}
    {{formatbitlbl |label=0x38C |value=thingy\tileset\desert\SLDLbox1.grp}}
    {{formatbitlbl |label=0x38D |value=thingy\tileset\desert\LDMachn1.grp}}
    {{formatbitlbl |label=0x38E |value=thingy\tileset\desert\SLDMchn1.grp}}
    {{formatbitlbl |label=0x38F |value=thingy\tileset\desert\Tgas.grp}}
    {{formatbitlbl |label=0x390 |value=thingy\tileset\desert\sarlacc.grp}}
    {{formatbitlbl |label=0x391 |value=protoss\scout.grp}}
    {{formatbitlbl |label=0x392 |value=zerg\Lurkegg.grp}}
    {{formatbitlbl |label=0x393 |value=zerg\devour.grp}}
    {{formatbitlbl |label=0x394 |value=zerg\devour.grp}}
    {{formatbitlbl |label=0x395 |value=thingy\zDvbirth.grp}}
    {{formatbitlbl |label=0x396 |value=zerg\zdvDeath.grp}}
    {{formatbitlbl |label=0x397 |value=zerg\zLubirth.grp}}
    {{formatbitlbl |label=0x398 |value=zerg\zLurker.grp}}
    {{formatbitlbl |label=0x399 |value=zerg\Zlurker.grp}}
    {{formatbitlbl |label=0x39A |value=zerg\zZluShad.grp}}
    {{formatbitlbl |label=0x39B |value=zerg\XOvermnd.grp}}
    {{formatbitlbl |label=0x39C |value=zerg\ZovShad.grp}}
    {{formatbitlbl |label=0x39D |value=protoss\darchn.grp}}
    {{formatbitlbl |label=0x39E |value=protoss\darchnT.grp}}
    {{formatbitlbl |label=0x39F |value=protoss\darchnT2.grp}}
    {{formatbitlbl |label=0x3A0 |value=protoss\PdaDeath.grp}}
    {{formatbitlbl |label=0x3A1 |value=protoss\corsair.grp}}
    {{formatbitlbl |label=0x3A2 |value=protoss\corsair.grp}}
    {{formatbitlbl |label=0x3A3 |value=thingy\pcsGlow.grp}}
    {{formatbitlbl |label=0x3A4 |value=thingy\elbFireC.grp}}
    {{formatbitlbl |label=0x3A5 |value=protoss\dtemplar.grp}}
    {{formatbitlbl |label=0x3A6 |value=protoss\XwarpGat.grp}}
    {{formatbitlbl |label=0x3A7 |value=protoss\pwgShad.grp}}
    {{formatbitlbl |label=0x3A8 |value=protoss\XwarpFir.grp}}
    {{formatbitlbl |label=0x3A9 |value=protoss\XelTempl.grp}}
    {{formatbitlbl |label=0x3AA |value=protoss\pxtShad.grp}}
    {{formatbitlbl |label=0x3AB |value=terran\bomber.grp}}
    {{formatbitlbl |label=0x3AC |value=terran\bomber.grp}}
    {{formatbitlbl |label=0x3AD |value=thingy\tbmGlow.grp}}
    {{formatbitlbl |label=0x3AE |value=thingy\tbmGlow.grp}}
    {{formatbitlbl |label=0x3AF |value=thingy\tbmAfter.grp}}
    {{formatbitlbl |label=0x3B0 |value=terran\medic.grp}}
    {{formatbitlbl |label=0x3B1 |value=terran\tmeShad.grp}}
    {{formatbitlbl |label=0x3B2 |value=terran\tmeDeath.grp}}
    {{formatbitlbl |label=0x3B3 |value=neutral\PsiDisr.grp}}
    {{formatbitlbl |label=0x3B4 |value=neutral\tpdShad.grp}}
    {{formatbitlbl |label=0x3B5 |value=neutral\Generate.grp}}
    {{formatbitlbl |label=0x3B6 |value=neutral\tgnShad.grp}}
    {{formatbitlbl |label=0x3B7 |value=thingy\Disrupt.grp}}
    {{formatbitlbl |label=0x3B8 |value=neutral\Kcritter.grp}}
    {{formatbitlbl |label=0x3B9 |value=neutral\nckShad.grp}}
    {{formatbitlbl |label=0x3BA |value=neutral\Scritter.grp}}
    {{formatbitlbl |label=0x3BB |value=neutral\Scritter.grp}}
    {{formatbitlbl |label=0x3BC |value=neutral\Icritter.grp}}
    {{formatbitlbl |label=0x3BD |value=neutral\ncicShad.grp}}
    {{formatbitlbl |label=0x3BE |value=neutral\Uraj.grp}}
    {{formatbitlbl |label=0x3BF |value=neutral\Khalis.grp}}
    {{formatbitlbl |label=0x3C0 |value=thingy\bsmoke.grp}}
    {{formatbitlbl |label=0x3C1 |value=bullet\Spike.grp}}
    {{formatbitlbl |label=0x3C2 |value=thingy\ZDvPuke.grp}}
    {{formatbitlbl |label=0x3C3 |value=thingy\ZDvHit.grp}}
    {{formatbitlbl |label=0x3C4 |value=thingy\PcsSplsh.grp}}
    {{formatbitlbl |label=0x3C5 |value=bullet\SMmissle.grp}}
    {{formatbitlbl |label=0x3C6 |value=bullet\grenade.grp}}
    {{formatbitlbl |label=0x3C7 |value=thingy\tCureSml.grp}}
    {{formatbitlbl |label=0x3C8 |value=thingy\tCureMed.grp}}
    {{formatbitlbl |label=0x3C9 |value=thingy\tCureLrg.grp}}
    {{formatbitlbl |label=0x3CA |value=thingy\tmeHealM.grp}}
    {{formatbitlbl |label=0x3CB |value=thingy\tmeHealM.grp}}
    {{formatbitlbl |label=0x3CC |value=thingy\tmeHealL.grp}}
    {{formatbitlbl |label=0x3CD |value=thingy\PDaMyoSm.grp}}
    {{formatbitlbl |label=0x3CE |value=thingy\PDaMyoMd.grp}}
    {{formatbitlbl |label=0x3CF |value=thingy\PDaMyoLg.grp}}
    {{formatbitlbl |label=0x3D0 |value=thingy\TmeFlshS.grp}}
    {{formatbitlbl |label=0x3D1 |value=thingy\TmeFlshM.grp}}
    {{formatbitlbl |label=0x3D2 |value=thingy\TmeFlshL.grp}}
    {{formatbitlbl |label=0x3D3 |value=thingy\PDaPsySm.grp}}
    {{formatbitlbl |label=0x3D4 |value=thingy\PDaPsyMd.grp}}
    {{formatbitlbl |label=0x3D5 |value=thingy\PDaPsyLg.grp}}
    {{formatbitlbl |label=0x3D6 |value=thingy\PDaParSm.grp}}
    {{formatbitlbl |label=0x3D7 |value=thingy\PDaParMd.grp}}
    {{formatbitlbl |label=0x3D8 |value=thingy\PDaParLg.grp}}
    {{formatbitlbl |label=0x3D9 |value=zerg\zmarker.grp}}
    {{formatbitlbl |label=0x3DA |value=thingy\ZdvGooS.grp}}
    {{formatbitlbl |label=0x3DB |value=thingy\ZdvGooS.grp}}
    {{formatbitlbl |label=0x3DC |value=thingy\ZdvGooS.grp}}
    {{formatbitlbl |label=0x3DD |value=thingy\ZdvGooS.grp}}
    {{formatbitlbl |label=0x3DE |value=thingy\ZdvGooM.grp}}
    {{formatbitlbl |label=0x3DF |value=thingy\ZdvGooM.grp}}
    {{formatbitlbl |label=0x3E0 |value=thingy\ZdvGooM.grp}}
    {{formatbitlbl |label=0x3E1 |value=thingy\ZdvGooM.grp}}
    {{formatbitlbl |label=0x3E2 |value=thingy\ZdvGooL.grp}}
    {{formatbitlbl |label=0x3E3 |value=thingy\ZdvGooL.grp}}
    {{formatbitlbl |label=0x3E4 |value=thingy\ZdvGooL.grp}}
    {{formatbitlbl |label=0x3E5 |value=thingy\ZdvGooL.grp}}
    {{formatbitlbl |label=0x3E6 |value=thingy\MaelHit.grp}}
  {{end-bittable}} }}
{{end-formattable}}

