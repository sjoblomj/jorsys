# News

{{begin-newsitem |time=2025-06-19T20:41:01Z |title=IronGRP 0.5 |author=Ojan |email=ojan@jorsys.org}}

{{highlight |text=IronGRP}} version 0.5 was just released with the following features: 

* Added [ImHex](https://imhex.werwolv.net) pattern language definitions for Normal GRPs, Uncompressed GRPs and WarCraft I style GRPs.
* Added [yazi](https://yazi-rs.github.io/) integration.
* Included fallback greyscale palette.
* Added a Readme file.
* Added a logo.
* Moved the PNG handling to an external library, [palpngrs](https://github.com/sjoblomj/palpngrs).
* Better logging: Introduced logging library and the log level 'trace'.
* Removed some Optimisation schemes from CompressionType Optimised. This makes it slightly less optimised but identical to how Blizzard did it, and the code is less complex.

{{highlight |text=IronGRP}} is available on [GitHub](https://github.com/sjoblomj/irongrp).

{{end-newsitem}}


{{begin-newsitem |time=2025-06-11T21:40:59Z |title=IronImage |author=Ojan |email=ojan@jorsys.org}}

After creating {{highlight |text=palpngrs}} ([GitHub](https://github.com/sjoblomj/palpngrs)) out of code from {{highlight |text=IronGRP}}, I decided to create a little utility that can convert between Palettized images and PNGs. I called it {{highlight |text=IronImage}}.

It can convert between PNGs and Palettized images from WarCraft I and WarCraft II. It can also convert between PNGs and the cursor format of WarCraft I and WarCraft II (which has the identical format to Palettized images, but with two extra bytes in the header {{dash}} one for the x-hotspot and one for the y-hotspot).

The code is available at [GitHub](https://github.com/sjoblomj/ironimage).

I would like to add support for PCX images, which are used in StarCraft. Image support in {{highlight |text=palpngrs}} is provided by [image-rs](https://github.com/image-rs/image), and there seems to be an experimental image-rs module, [image-extras](https://github.com/image-rs/image-extras) where PCX support is being considered (see discussion [here](https://github.com/image-rs/image/issues/2363)). However, it does not yet seem to be in a stable state, and [GIMP](gimp.org) supports the PCX format anyway. I will probably revisit PCX support at a later time. For now, IMG and Cursor support will have to do.

{{end-newsitem}}


{{begin-newsitem |time=2025-05-30T19:26:18Z |title=Namebreaking |author=Ojan |email=ojan@jorsys.org}}

From Diablo I and onward, up until fairly recently, Blizzard has used MPQ files to store their game data. The MPQ format is a container format that can hold multiple files and directories, like ZIP files. While the MPQ files store files, they do not store file names. To know the names of the files, an external listfile must be used. Internally, the MPQ files instead store two hashes of the file names to identify the files.

Almost all file names of all MPQ files are known, but there are a few unknown file names.

Back in the days, some 20 years ago, I tried to figure out all the names of the MPQ files of Blizzard. At university, I wrote a distributed brute-force program that would try to find one of the remaining portrait files, but it never found it.

I just created a little CUDA program to make use of the GPU to continue to brute-force where I left off many years ago. Just a little something to run in the background, in the hopes that some of the last unknown properties of the games will be revealed.

{{end-newsitem}}


{{begin-newsitem |time=2025-05-20T18:55:19Z |title=Work begun on image converter |author=Ojan |email=ojan@jorsys.org}}

I have started to work on an image converter for WarCraft I and WarCraft II. I have made a library called [palpngrs](https://github.com/sjoblomj/palpngrs) out of the code I had for {{highlight |text=IronGRP}}, which can handle conversions to and from Palettized images and PNG files. Very few lines of code then allowed me to slap together a little utility that can convert raw IMG files (used for backgrounds and dialog elements in WarCraft I and WarCraft II) as well as Cursor files (used for the mouse cursor in WarCraft I and WarCraft II) to PNGs and back.

I have some finishing touches to do and I can't decide on a name I like for it. But with this utility, {{highlight |text=IronGRP}} and {{highlight |text=IronTBL}}, a fair amount of the game files of WarCraft I and WarCraft II can now be converted to and from more accessible formats.

{{end-newsitem}}


{{begin-newsitem |time=2025-05-10T06:13:47Z |title=IronGRP 0.4 released |author=Ojan |email=ojan@jorsys.org}}

{{highlight |text=IronGRP}} 0.4 has just been released and is avaliable at [GitHub](https://github.com/sjoblomj/irongrp). Some of the features have been mentioned before: It has support for Extended Uncompressed GRPs and WarCraft I GRPs, and it can now correctly differentiate between different GRP types. I have added some boundary checks for width, height, offsets and frame count, and added more unit tests. It can now also generate shell completions, to make the tool more ergonomic to work with.

When converting from GRP to PNGs, {{highlight |text=IronGRP}} will now name the output files "uncompressed_frame_xxx.png" or "war1_frame_xxx.png", respectively. This is to make it easier to identify the type of GRP that was used when converting back to GRP. When converting from PNGs to GRP, if no CompressionType is given (or if CompressionType Auto is given), {{highlight |text=IronGRP}} will create an Uncompressed GRP if any of the input filenames contains "uncompressed", and create a WarCraft I style GRP if any of the input filenames contains "war1".

A fair amount of refactoring has been done, so the code is now a bit better structured, and I've prepared to move a chunk of the code to handle the conversion between PNGs and Palettized images into its own library. This will allow me to use the same code in upcomming tools that I have in mind. The cursor formats of WarCraft I and WarCraft II uses the same principle of Palettized Images, as does the Parallax SPK files of StarCraft. I suspect the tilesets of all these games do too, but I haven't looked into that yet.

{{end-newsitem}}


{{begin-newsitem |time=2025-04-26T09:37:22Z |title=Support for WarCraft I GRPs in IronGRP |author=Ojan |email=ojan@jorsys.org}}

I extracted the GRPs from WarCraft I: Orcs and Humans from its data archive files. The format is nearly identical to Uncompressed GRPs, except that the header is four bytes instead of six (in WarCraft I there is first a two byte frame count, and then a byte with the maximum width followed by a byte of the maximum height - In StarCraft and WarCraft II the max width and max height are both two bytes each).

This caused a surprising amount of code changes in {{highlight |text=IronGRP}}, but nothing too difficult. There is still work to be done in automatically detecting whether the header is four or six bytes, though. I implemented a primitive check, but it fails to differentiate between WarCraft I GRPs and Extended Uncompressed GRPs. Some more work is needed to make it correct and more robust.

{{end-newsitem}}


{{begin-newsitem |time=2025-04-21T14:27:41Z |title=Support for Extended Uncompressed GRPs |author=Ojan |email=ojan@jorsys.org}}

After spending the Easter holidays being sick, I looked a bit more at the last three GRPs that I mentioned last time.

The `art/orc.grp` and `art/human.grp` turned out to be what I call Extended Uncompressed GRPs for lack of a better name. A frame in the GRP files only have room for sprites of up to 255x255 pixels. However, for these two files, Blizzard has done a little trick. Each frame contain an offset to where the image data starts. By setting the high bit of the offset, it indicates that the frame is wider than 255 pixels. The actual width then, is what the frame reports, plus 256, which for these two files becomes 300 pixels wide. {{highlight |text=IronGRP}} now supports this format hack, and converting from GRP to PNGs to GRP renders identical result as the input.

As for the `art/unit/orc/black.grp` {{dash}} the Orc Blacksmith from WarCraft II {{dash}} it turns out that Blizzard for some reason tweaked a parameter when encoding it. GRPs use RLE (Run-Length Encoding) compression, which on a high level works like this: a control byte is used to communicate one of three command types: one being that the next x pixels are transparent; one being that the next x pixels are identical; one being to copy the next x pixels, which can be different. So if there were eight identical pixels in a row, the command byte would signal identicality, and the next byte would be the pixel value. This thus saves 8 - 2 = 6 bytes of space.

Normally, four pixels must be identical for the identicality instruction to be used. However, for the Orc Blacksmith GRP {{dash}} and that GRP alone {{dash}} a different more efficient threshold of three pixels is used. As this saves more space than the normal threshold of four pixels, it is unclear why this is not the standard.

{{highlight |text=IronGRP}} supports three different compression types: the Normal RLE compression, Uncompressed, and a more Optimised compression type. The Optimised compression type would previously do three things: use this more efficient threshold of three identical pixels; attempt to reuse the encoded ending pixels of a row if that matched the first pixels of the next row; as well as continuing to read identical pixels rather than finishing because too many pixels had been read.

These latter two optimisations do result in smaller file sizes, but only by very little, and they add complexity to the code. I have thus decided to remove them, and instead just use the more efficient threshold of three pixels for the identicality instruction. Not only do these two optimisations not yield a significant size reduction, but by not doing them, the Optimised compression type now creates an identical output of the Blacksmith.

A user then has the option to use the Normal RLE compression type, or the Optimised compression type. The games should have no problem using either, so it is up to the user whether they want the Blizzard standard way, or a slightly more efficient way.

With this, all GRPs of StarCraft, StarCraft: Brood Wars and WarCraft II: Battle.net edition can now be perfectly converted (apart from the WarCraft II portrait files I mentioned previously, which can be handled but with a difference, which I regard as an error on Blizzard's part).

{{end-newsitem}}



{{begin-newsitem |time=2025-04-19T09:14:19Z |title=IronGRP 0.3 |author=Ojan |email=ojan@jorsys.org}}

With release 0.3 of {{highlight |text=IronGRP}}, it now supports converting to and from uncompressed GRPs. That means that every last GRP from StarCraft and StarCraft: Brood War can be converted to and from PNGs. The program is available on [GitHub](https://github.com/sjoblomj/irongrp).

I now turn my attention to WarCraft II: Battle.net Edition. The GRP format is the same as in StarCraft, but a few files have differences when going from GRP to PNGs to GRP again, and some files fail due to format errors. For WarCraft II: BNE, we have:

| Status             | Numbers |
| :----------------- | ------: |
| Identical          |     266 |
| GRPs differ        |       7 |
| Ratio of identical |     95% |

The seven outliers are:
1. War2Dat/Art/Unit/Orc/black.grp
2. War2Dat/Art/unit/Portrait/portrait.grp
3. War2Dat/Art/unit/Portrait/l_port.grp
4. War2Dat/Art/unit/Portrait/s_port.grp
5. War2Dat/Art/unit/Portrait/x_port.grp
6. War2Dat/art/orc.grp
7. War2Dat/art/human.grp

The first one, the Orc Blacksmith, is a normal GRP. There are significant differences in the input and output GRPs. I need to investigate further what is happening there.

The four portrait files all have the same underlying issue. Identical frames can be reused to save space, which is frequently utilized in the GRPs. The frames 182 and 183 are identical and the image data is reused. Ditto with frames 184 and 185. However, frame 158 and 159 are also identical, but their image data is not reused but instead duplicated. For all these three pairs of frames, {{highlight |text=IronGRP}} detects that they are identical and reuse the image data. I will write this off as an error on Blizzard's part, as there is no reason to reuse some frames and not others.

The last two files are probably Uncompressed GRPs or a variant thereof. Either my handling of Uncompressed GRPs is not solid enough, or they are a different variant compared to the Uncompressed GRPs of StarCraft.
{{end-newsitem}}



{{begin-newsitem |time=2025-04-15T16:36:58Z |title=Fixed offset bug in IronGRP |author=Ojan |email=ojan@jorsys.org}}

{{highlight |text=IronGRP}} now correctly handles the last eight normal GRPs that previously were encoded differently than their input! When frames had identical image contents, it would reuse the same frame data, including the vertical and horizontal offsets. It turned out that 
identical image data does not necessarily mean identical offsets. For instance, the red blinking "nuke dot" jumps around a little bit, which is accomplished by setting different offsets, although the image data is the same.

This means that all normal GRPs are now handled correctly! Remaining are ten uncompressed GRPs, that I will turn my attention to next.

| Status             | Numbers |
| :----------------- | ------: |
| Identical          |    1080 |
| GRPs differ        |      10 |
| Ratio of identical |     99% |

The ten uncompressed GRPs are:

 1. Patch_rt.mpq: dlgs/protoss.grp
 2. Patch_rt.mpq: dlgs/terran.grp
 3. Patch_rt.mpq: dlgs/zerg.grp
 4. Patch_rt.mpq: glue/PalNl/Dlg.grp
 5. BrooDat.mpq: glue/ScorePd/iScore.grp
 6. BrooDat.mpq: glue/ScorePv/iScore.grp
 7. BrooDat.mpq: glue/ScoreTd/iScore.grp
 8. BrooDat.mpq: glue/ScoreTv/iScore.grp
 9. BrooDat.mpq: glue/ScoreZd/iScore.grp
10. BrooDat.mpq: glue/ScoreZv/iScore.grp
{{end-newsitem}}



{{begin-newsitem |time=2025-04-14T21:52:08Z |title=Palettes ruining the party |author=Ojan |email=ojan@jorsys.org}}

So I've been playing around with {{highlight |text=IronGRP}} for a few hours now, and I just realized what the cause of (almost all) the remaining differences between the input GRPs and the output GRPs are.

The algorithm I use to encode PNG files into GRPs is based on reading the colour values of each pixel in the PNG, and finding the index of the corresponding colour in the palette. This is done by searching through the palette for the matching colour (or if the user has deviated from the palette, the closest colour match), and then using that index in the GRP encoding.

However, I just realized that the palette file that I have been using has several entries with duplicated colours. I have thus been trying to figure out why on earth the program would swap a single colour for another (I thought it was some integer overflow situation again), when what happened is that it looked for a colour matching the pixel value and correctly returned the first match it found, when the input GRP referred to a different index with an identical colour value.

When I switched to a palette file that has no duplicated colours, the results were better. When running on all GRP files in StarDat.mpq, BrooDat.mpq and patch_rt.mpq, the results are now as follows:

| Status             | Numbers |
| :----------------- | ------: |
| Identical          |    1072 |
| GRPs differ        |      18 |
| Ratio of identical |     98% |

We're getting there! The offending GRPs are:

 1. StarDat.mpq: unit/neutral/nddsha2.grp
 2. StarDat.mpq: unit/thingy/dbl_exp.grp
 3. StarDat.mpq: unit/thingy/nukebeam.grp
 4. StarDat.mpq: unit/thingy/sbalarge.grp
 5. Patch_rt.mpq: dlgs/protoss.grp *
 6. Patch_rt.mpq: dlgs/terran.grp *
 7. Patch_rt.mpq: dlgs/zerg.grp *
 8. Patch_rt.mpq: glue/PalNl/Dlg.grp *
 9. BrooDat.mpq: glue/ScorePd/iScore.grp *
10. BrooDat.mpq: glue/ScorePv/iScore.grp *
11. BrooDat.mpq: glue/ScoreTd/iScore.grp *
12. BrooDat.mpq: glue/ScoreTv/iScore.grp *
13. BrooDat.mpq: glue/ScoreZd/iScore.grp *
14. BrooDat.mpq: glue/ScoreZv/iScore.grp *
15. BrooDat.mpq: unit/neutral/ncicShad.grp
16. BrooDat.mpq: unit/neutral/nckShad.grp
17. BrooDat.mpq: unit/neutral/nddSha2.grp
18. BrooDat.mpq: unit/wirefram/wirefram.grp

The ones marked with * are uncompressed I believe, for which there is no support yet. As for the rest, I did a quick analysis. None have unused "residue" bytes (which is a good thing), but they all have several sets of identical GRP frames. My hunch is that it is related to that, or to some corner case regarding vertical and horisontal offsets.
{{end-newsitem}}


{{begin-newsitem |time=2025-04-14T19:05:13Z |title=IronGRP is getting preciser |author=Ojan |email=ojan@jorsys.org}}

I have continued to look at how the GRP converter, {{highlight |text=IronGRP}}, decodes and re-encodes the GRP files of StarCraft. I have examined the output of the Terran Battlecruiser, the Protoss Dragoon and the Protoss Nexus GRPs, since those were three random GRPs out of the bunch where my tool failed to perfectly convert the GRP to PNGs and then back to GRP again.

I have found the root causes of why it would differ: for the Battlecruiser, it was a corner case where my algorithm was somewhat more efficient than Blizzard's. For the Dragoon, I mistakenly printed out all image data of duplicated frames, which not only resulted in the GRPs to differ, but for mine to be nearly eight times as large as the original. Ooops. For the Nexus, it was a type conversion error that resulted in integer overflow errors. These things are now fixed so that it matches Blizzard's way.

So like last time, I converted all GRPs to PNGs, and then back to GRPs again, for all GRPs in unit/protoss, unit/thingy, unit/terran and unit/zerg from StarDat.mpq. The results are now as follows:

| Status             | Numbers |
| :----------------- | ------: |
| Identical          |     323 |
| GRPs differ        |      79 |
| Ratio of identical |     80% |

Much better than last time, but still some work to be done.
{{end-newsitem}}


{{begin-newsitem |time=2025-04-10T21:09:02Z |title=Work on TBL converter |author=Ojan |email=ojan@jorsys.org}}

I started working on a TBL converter. TBL files are used in WarCraft I, WarCraft II and StarCraft for holding text data, such as unit names, menu text, and other game strings. They also act as mappings to sprite and sound files. Since I've written the tool in Rust, I went with the same naming as the previous tool, and called it {{highlight |text=IronTBL}}.

{{img |file=irontbl.png |title=IronTBL logo}}

It can convert TBL files to plain text files and back. As a little extra, I also added [yazi](https://yazi-rs.github.io/) preview integration. There's some minor things I still want to fix for it, such as adding a Readme file, and provide a way to autogenerate shell completions (because why not).
{{end-newsitem}}


{{begin-newsitem |time=2025-04-07T21:26:41Z |title=More progress on IronGRP |author=Ojan |email=ojan@jorsys.org}}

Work continues on the GRP converter, {{highlight |text=IronGRP}}, when time permits. It can now detect duplicated frames and reuse them, instead of copying identical frames multiple times.

The GRP format has no concept of transparency, whereas PNGs do, in their alpha channel. {{highlight |text=IronGRP}} can now handle PNGs with alpha channels, in the sense that completely transparent pixels are treated as belonging to palette index 0, which is the transparent colour in the GRP format. Pixels with complete opacity are treated as normal pixels. Any other value in the alpha channel gives rise to a warning, but is otherwise treated as a normal pixel.

In the previous news item, I claimed that {{highlight |text=IronGRP}} converts flawlessly, but this turned out to be a premature claim. I converted all GRPs to PNGs, and then back to GRPs again, for all GRPs in unit/protoss, unit/thingy, unit/terran and unit/zerg from StarDat.mpq. The results are as follows:

| Status             | Numbers |
| :----------------- | ------: |
| Identical          |     183 |
| GRPs differ        |     219 |
| Ratio of identical |     45% |

I was hoping for more identical GRPs, and I'll need some time to investigate what these differences are. I doubt they are really visible; this is probably more encoding differences making individual bytes different, or perhaps "residue" bytes that are not actually read by the game.

Still remaining is also to handle Uncompressed GRPs.
{{end-newsitem}}


{{begin-newsitem |time=2025-04-03T22:22:30Z |title=IronGRP now converts flawlessly |author=Ojan |email=ojan@jorsys.org}}

The GRP converter, {{highlight |text=IronGRP}}, that I've been working on for the past few days, now seems to work flawlessly (at least on the Valkyrie GRP; I need to test on more GRPs). Previously, it would sometimes fail to consume enough pixels when reading a row of pixels, which caused slight deviations when converting from GRP to PNG and back to GRP. That was the cause of the slight difference in output that I referred to in the last post. Now, GRP to PNG to GRP conversion is byte-to-byte identical (for the Valkyrie).

Since it now produces identical output to its input, I've promoted the code to version 0.1. The code is available on [GitHub](https://github.com/sjoblomj/irongrp).

As I wrote in last post, there are some things I still want to add:
* Handling of Uncompressed GRPs.
* Handling PNGs with alpha channels (transparency).
* Detecting duplicated frames and reusing them rather than writing them anew.

Once that is in place, it seems fitting to call it version 1.0.
{{end-newsitem}}


{{begin-newsitem |time=2025-04-02T22:15:02Z |title=New tool: IronGRP |author=Ojan |email=ojan@jorsys.org}}

The unit and building sprites of WarCraft I, WarCraft II and StarCraft I are found in GRP files, which need to be converted into other image formats in order to be edited. For that, I'm working on a little GRP to PNG converter tool, called {{highlight |text=IronGRP}}.

Back in the day, {{highlight |text=RetroGRP}} was used by everyone, but it is a closed source Windows only utility. {{highlight |text=ShadowFlare}} made [grpapi](https://sfsrealm.hopto.org/projects/gitweb.cgi?p=grpapi.git;a=summary) which is no doubt very competent, but not too straight-forward to compile on Linux (probably speaks more about my own short-comings than anything else). There is also [PyGRP as part of PyMS](https://github.com/poiuyqwert/PyMS/) by {{highlight |text=poiuyqwert}}, but it seems to be stuck in Python 2 land. Worth mentioning is also [libgrp](https://github.com/Stratagus/libgrp/) by {{highlight |text=Bradley Clemetson}}.

Instead of fighting to compile 20 year old source code, I decided to take a shot at creating a utility from scratch. {{highlight |text=IronGRP}} is the fruit of that labour. As of this writing, it can convert GRPs to PNGs and vice versa, and it can create tiled images, where all frames are in one tiled image:

{{img |file=valkyrie.png |title=Converted Valkyrie GRP}}

The decoding and encoding algorithm appears to create near-perfect results compared to Blizzard's own file, but there are some instances where the output differs ever so slightly.

I'm trying to see if these differences are fixable. I also want to handle uncompressed GRPs, and more gracefully handle PNGs with alpha channels (transparency). Support for detecting duplicated frames and re-using them should be added as well. But for now, I'm happy to say that what I have feels like a pretty solid start.
{{end-newsitem}}


{{begin-newsitem |time=2025-03-20T21:19:22Z |title=First update of Jorvik Systems |author=Ojan |email=ojan@jorsys.org}}

With this post, I want to open the gates of {{highlight |text=Jorvik Systems}}.

This site is a long-overdue return to an old passion of mine: digging deep into the internals of some of the most iconic games of the '90s {{dash}} WarCraft: Orcs and Humans, WarCraft II, and StarCraft. These titles defined a generation of real-time strategy gaming, and for many of us, they also opened the door to a world of creativity through modding the games, where we changed their visuals and dynamics.

Roughly 25 years ago (!!!), I was very active in the modding community. Back then, we reverse-engineered file formats, hex-edited game data, created tools and programs to make it all more accessible, and shared our findings on forums, chats, and IRC channels. It was a different era {{dash}} the Internet of old before social media, filled with curiosity and ingenuity. As for myself, while life has pulled me in other directions, I never truly lost that fascination with how the games work under the hood.

This site is my attempt to reconnect with that world. I hope this site will grow to host format specifications of files, modding tools, old mod files, tutorials and guides. As an avid Linux user, I also wish to present tools that hopefully are cross-platform and open source, so that anyone can use them.

The site itself draws much inspiration from the legendary {{highlight |text=Camelot Systems}}, or CamSys, and the website design is indeed visually very similar. CamSys, its members and forum were in many ways the driving force in the modding community of WarCraft II and StarCraft, although plenty of sites, groups and other forums followed in its wake.

Whether you're a veteran modder from the old days, someone who wishes to understand how the games and formats worked, or just someone with a soft spot for late-90s PC gaming, I hope you’ll find something interesting here.

Let’s dive in {{dash}} there's a lot of magic buried in those old bytes.
{{end-newsitem}}
