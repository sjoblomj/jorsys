# portdata.dat Format

portdata.dat lists the portraits: the video shown in the status panel for the selected unit, and in mission briefings (see Appendix: Portraits list). units.dat's Portrait field picks the entry. Each portrait has fidget videos, played while it idles, and talking videos, played while the unit speaks. It is the file arr\portdata.dat in the game's MPQ archives and is 1320 bytes long. Each field below is a list with one entry for each of the 110 portraits, and the lists are stored one after another with nothing in between, so the offsets are from the start of the file. StarEdit does not use it. The layout is the same in every version from 1.04 to 1.17, of both StarCraft and Brood War. StarCraft 1.00 to 1.03 used an older layout with 90 portraits (1080 bytes); the older file is still in StarDat.mpq in later versions but is never loaded, because the copy in BrooDat.mpq (or patch_rt.mpq) is found first. The game loads the file each time a game or a mission briefing starts. Fields are read in order, and the game stops with a file error if the file is longer than the layout. A shorter file that ends exactly where a field ends loads without an error; the fields after the end then keep whatever they held before. No field is checked when the game uses it, so an out-of-range value reads whatever follows the table it points into.

The video files are found from a name in arr\portdata.tbl: the game plays portrait\<name><n>.smk, where n is the number of the video, 0 to 3 for fidgets and 0 to 2 for talking. For example the Marine's fidget name tmarine\TMaFid0 gives portrait\tmarine\TMaFid00.smk to TMaFid03.smk. If a video is missing, the game tries the next lower number. With the portrait setting below full animation, only video 0 is played.

## Fidget Video Name
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=440 bytes (4 bytes / Portrait)}}
  {{formatlbl |label=Description |value=A string number in arr\portdata.tbl, counting from 1: 1 is the first string. The game turns it into the string itself when it loads the file. Only the lowest 16 bits are used; 0 means no string, and a number beyond the last string gives an empty string. The string is a folder and the start of a file name, to which the game adds the video number and .smk (see the description above).}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\portdata.tbl.}}
{{end-formattable}}

## Talking Video Name
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x01B8}}
  {{formatlbl |label=Length |value=440 bytes (4 bytes / Portrait)}}
  {{formatlbl |label=Description |value=A string number in arr\portdata.tbl, counting from 1: 1 is the first string. The game turns it into the string itself when it loads the file. Only the lowest 16 bits are used; 0 means no string, and a number beyond the last string gives an empty string. Used like Fidget Video Name for the talking videos. The game picks talking video 0, 1 or 2 at random, never the same one twice in a row. Some portraits that never talk use their fidget name here.}}
  {{formatlbl |label=Values |value=Integer value between 0 and the number of strings in arr\portdata.tbl.}}
{{end-formattable}}

## Fidget 0 Chance
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x0370}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / Portrait)}}
  {{formatlbl |label=Description |value=How likely fidget video 0 is to be picked, out of 101. The game rolls a number from 0 to 100 and walks through the four chances in order, adding each to a running total, until the total reaches the roll. The four chances should add up to at least 100: the game tests for the end of the list only after reading the next chance, so a roll above the total reads a fifth, nonexistent chance. It reads it through whatever variable follows the four field addresses the game keeps, taken as an address, and that variable differs between versions. In a game, 1.05 and 1.17 have the address of a status panel text there, so a byte in or just after that text is read and video 0 is picked; 1.15.0 and 1.16.1 have a flag that is 0 or 1, which is not a readable address, so the game crashes with an access violation. Mission briefings keep their own copy of the four addresses: after it, 1.05 has such a flag and crashes, and 1.15.0 has the width and height of a briefing frame picture, which as an address may or may not be readable (if it is, video 0 is picked). Every shipped portrait adds up to exactly 100.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. Shipped: 85, 5, 5 and 5 for most units; 100, 0, 0 and 0 for beacons, flags, powerups and resources.}}
{{end-formattable}}

## Fidget 1 Chance
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x03DE}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / Portrait)}}
  {{formatlbl |label=Description |value=How likely fidget video 1 is to be picked, out of 101. The game rolls a number from 0 to 100 and walks through the four chances in order, adding each to a running total, until the total reaches the roll. See Fidget 0 Chance.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. Shipped: 85, 5, 5 and 5 for most units; 100, 0, 0 and 0 for beacons, flags, powerups and resources.}}
{{end-formattable}}

## Fidget 2 Chance
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x044C}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / Portrait)}}
  {{formatlbl |label=Description |value=How likely fidget video 2 is to be picked, out of 101. The game rolls a number from 0 to 100 and walks through the four chances in order, adding each to a running total, until the total reaches the roll. See Fidget 0 Chance.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. Shipped: 85, 5, 5 and 5 for most units; 100, 0, 0 and 0 for beacons, flags, powerups and resources.}}
{{end-formattable}}

## Fidget 3 Chance
{{begin-formattable}}
  {{formathexlbl |label=Offset |value=0x04BA}}
  {{formatlbl |label=Length |value=110 bytes (1 byte / Portrait)}}
  {{formatlbl |label=Description |value=How likely fidget video 3 is to be picked, out of 101. The game rolls a number from 0 to 100 and walks through the four chances in order, adding each to a running total, until the total reaches the roll. See Fidget 0 Chance.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 255. Shipped: 85, 5, 5 and 5 for most units; 100, 0, 0 and 0 for beacons, flags, powerups and resources.}}
{{end-formattable}}

---

## Appendix: Portraits list
{{begin-formattable}}
  {{formatlbl |label=Description |value=Every portrait, with its fidget and talking names from arr\portdata.tbl and its four fidget chances in the shipped data.}}
  {{formatlbl |label=Bits |value={{begin-bittable}}
    {{formatbitlbl |label=0x00 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x01 |value=tghost\TGhFid0 / tghost\TGhTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x02 |value=tfirebat\TFbFid0 / tfirebat\TFbTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x03 |value=tvulture\TVuFid0 / tvulture\TVuTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x04 |value=TSpider\TMnFid0 / TSpider\TMnTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x05 |value=tgoliath\TGoFid0 / tgoliath\TGoTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x06 |value=ttank\TTaFid0 / ttank\TTaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x07 |value=tSCV\TSCFid0 / tSCV\TSCTlk0 (87/5/5/3)}}
    {{formatbitlbl |label=0x08 |value=tphoenix\TPhFid0 / tphoenix\TPhTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x09 |value=tvessel\TVeFid0 / tvessel\TVeTlk0 (89/5/5/1)}}
    {{formatbitlbl |label=0x0A |value=tdropshi\TDrFid0 / tdropshi\TDrTlk0 (90/5/0/5)}}
    {{formatbitlbl |label=0x0B |value=tbattlec\TBaFid0 / tbattlec\TBaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x0C |value=UKerr\UKeFid0 / UKerr\UKeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x0D |value=UJim\URaFid0 / UJim\URaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x0E |value=UDuke\UDuFid0 / UDuke\UDuTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x0F |value=Ncivilian\NCiFid0 / Ncivilian\NCiFid0 (85/5/5/5)}}
    {{formatbitlbl |label=0x10 |value=Umengsk\UMeFid0 / Umengsk\UMeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x11 |value=TAdvisor\TAdFid0 / TAdvisor\TAdTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x12 |value=ZLarva\ZLaFid0 / ZLarva\ZLaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x13 |value=ZEgg\ZEgFid0 / ZEgg\ZEgTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x14 |value=ZZergl\ZZeFid0 / ZZergl\ZZeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x15 |value=ZHydra\ZHyFid0 / ZHydra\ZHyTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x16 |value=ZUltra\ZUlFid0 / ZUltra\ZUlTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x17 |value=ZBrood\ZBrFid0 / ZBrood\ZBrTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x18 |value=ZDrone\ZDrFid0 / ZDrone\ZDrTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x19 |value=ZOver\ZOvFid0 / ZOver\ZOvTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x1A |value=ZMutalid\ZMuFid0 / ZMutalid\ZMuTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x1B |value=ZGuard\ZGuFid0 / ZGuard\ZGuTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x1C |value=ZQueen\ZQuFid0 / ZQueen\ZQuTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x1D |value=ZDefiler\ZDeFid0 / ZDefiler\ZDeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x1E |value=ZAvenger\ZAvFid0 / ZAvenger\ZAvTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x1F |value=Zcocoon\ZCoFid0 / Zcocoon\ZCoFid0 (85/5/5/5)}}
    {{formatbitlbl |label=0x20 |value=ZChrysalis\ZChFid0 / ZChrysalis\ZChFid0 (85/5/5/5)}}
    {{formatbitlbl |label=0x21 |value=ZInfestT\ZBGFid0 / ZInfestT\ZBGTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x22 |value=UZasz\Fid0 / UZasz\Tlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x23 |value=UDagg\UDgFid0 / UDagg\UDgTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x24 |value=UIKerr\UIKFid0 / UIKerr\UIKTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x25 |value=UHunters\UHuFid0 / UHunters\UHuTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x26 |value=ZAdvisor\ZAdFid0 / ZAdvisor\ZAdTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x27 |value=PProbe\PPrFid0 / PProbe\PPrTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x28 |value=PZealot\PZeFid0 / PZealot\PZeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x29 |value=PDragoon\PDrFid0 / PDragoon\PDrTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x2A |value=PTemplar\PTeFid0 / PTemplar\PTeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x2B |value=parchon\PArFid0 / parchon\PArTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x2C |value=pshuttle\PShFid0 / pshuttle\PShTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x2D |value=PScout\PScFid0 / PScout\PScTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x2E |value=PArbiter\PAbFid0 / PArbiter\PAbTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x2F |value=pcarrier\PCaFid0 / pcarrier\PCaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x30 |value=PInterce\PInFid0 / PInterce\PInTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x31 |value=UDTemplar\UDTFid0 / UDTemplar\UDTTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x32 |value=UFenZeal\UFeFid0 / UFenZeal\UFeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x33 |value=UFenDrag\UFdFid0 / UFenDrag\UFdTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x34 |value=UZeratul\UZeFid0 / UZeratul\UZeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x35 |value=UTassadar\UTaFid0 / UTassadar\UTaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x36 |value=UTassadar\UTaFid0 / UTassadar\UTaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x37 |value=PWitness\PWiFid0 / PWitness\PWiTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x38 |value=PTrilo\PTrFid0 / PTrilo\PTrTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x39 |value=PTrilo\PTrFid0 / PTrilo\PTrTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x3A |value=Ukhad\NCrFid0 / Ukhad\NCrTlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x3B |value=PAdvisor\PAdFid0 / PAdvisor\PAdTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x3C |value=PAdvisor\PAdFid0 / PAdvisor\PAdTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x3D |value=nbiker\NBiFid0 / nbiker\NBiTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x3E |value=NBadCrit\NBCFid0 / NBadCrit\NBCTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x3F |value=NJungCrit\NJCFid0 / NJungCrit\NJCTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x40 |value=NLavaCrit\NLCFid0 / NLavaCrit\NLCTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x41 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x42 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x43 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x44 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x45 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x46 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x47 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x48 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x49 |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x4A |value=tmarine\TMaFid0 / tmarine\TMaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x4B |value=NGasTank\NGTFid0 / NGasTank\NGTFid0 (100/0/0/0)}}
    {{formatbitlbl |label=0x4C |value=NGOrb\NGOFid0 / NGOrb\NGOFid0 (100/0/0/0)}}
    {{formatbitlbl |label=0x4D |value=NGasSac\NGSFid0 / NGasSac\NGSFid0 (100/0/0/0)}}
    {{formatbitlbl |label=0x4E |value=NOre\NOCFid0 / NOre\NOCFid0 (100/0/0/0)}}
    {{formatbitlbl |label=0x4F |value=UDisk\UDdFid0 / Udisk\UDdTlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x50 |value=Upsi\UPsFid0 / Upsi\UPsTlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x51 |value=Ushard\UShFid0 / Ushard\UShTlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x52 |value=UFlag1\UF1Fid0 / UFlag1\UF1Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x53 |value=UFlag2\UF2Fid0 / UFlag2\UF2Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x54 |value=UFlag3\UF3Fid0 / UFlag3\UF3Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x55 |value=UFlag4\UF4Fid0 / UFlag4\UF4Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x56 |value=UFlag5\UF5Fid0 / UFlag5\UF5Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x57 |value=UFlag6\UF6Fid0 / UFlag6\UF6Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x58 |value=UFlag7\UF7Fid0 / UFlag7\UF7Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x59 |value=UFlag8\UF8Fid0 / UFlag8\UF8Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x5A |value=tmedic\TMeFid0 / tmedic\TMeTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x5B |value=Tbomber\TBmFid0 / TBomber\TBmTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x5C |value=TDugal\UdgFid0 / TDugal\UdgTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x5D |value=Talex\TaxFid0 / Talex\TaxTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x5E |value=TSam\TsmFid0 / TSam\TsmTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x5F |value=PArtanis\PatFid0 / PArtanis\PatTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x60 |value=PRaz\PRzFid0 / PRaz\PRzTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x61 |value=Zdevour\ZDvfid0 / Zdevour\ZDvtlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x62 |value=ZLurker\ZLufid0 / ZLurker\ZLutlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x63 |value=PDarchon\PDaFid0 / PDarchon\PDaTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x64 |value=PCorsair\PCsFid0 / PCorsair\PCsTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x65 |value=NRedCrit\NRDFid0 / NRedCrit\NRDTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x66 |value=NBluCrit\NLCFid0 / NBluCrit\NLCTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x67 |value=NIceCrit\NICFid0 / NIceCrit\NICTlk0 (85/5/5/5)}}
    {{formatbitlbl |label=0x68 |value=UUraj\UUjFid0 / UUraj\UUjTlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x69 |value=UKhalis\UKsFid0 / UKhalis\UKsTlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x6A |value=UFlag9\UF9Fid0 / UFlag9\UF9Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x6B |value=UFlag10\UF10Fid0 / UFlag10\UF10Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x6C |value=UFlag11\UF11Fid0 / UFlag11\UF11Tlk0 (100/0/0/0)}}
    {{formatbitlbl |label=0x6D |value=UFlag12\UF12Fid0 / UFlag12\UF12Tlk0 (100/0/0/0)}}
  {{end-bittable}} }}
{{end-formattable}}

