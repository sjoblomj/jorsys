# The MoPaQ Archive Format

By Justin Olbrantz (Quantam) and Jean-Francois Roy (BahamutZERO), 2006-2010

{{heading |level=2 |title=Introduction to the MoPaQ Format}}

The MoPaQ (or MPQ) format is an archive file format designed by Mike O'Brien (hence the name Mike O'brien PaCK) at Blizzard Entertainment. The format has been used in all Blizzard games since (and including) Diablo. It is heavily optimized to be a read-only game archive format, and excels at this role.

The Blizzard MoPaQ-reading functions are contained in the Storm module, which my be either statically or dynamically linked. Traditionally, the Blizzard MoPaQ-writing functions are contained in the MPQAPI module, which is always statically linked; in StarCraft II, however, the MoPaQ-writing functions are now contained in Storm.

[StormLib](https://github.com/ladislav-zezula/StormLib) - mentioned several times in this specification - is an open-source MoPaQ reading and writing library written by Ladislav Zezula (no affiliation with Blizzard Entertainment). While it's a bit dated as of this writing (2010), and does not support all of the newer MoPaQ features, it contains source code to the more exotic compression methods used by MoPaQ, such as the PKWare implode algorithm, MoPaQ's huffman compression algorithm, and the IMA ADPCM compression used by MoPaQ.


{{heading |level=3 |title=The MoPaQ Format}}

All numbers in the MoPaQ format are in little endian byte order; signed numbers use the two's complement system. Data types are listed either as int (integer, the number of bits specified), byte (8 bits), or char (bytes which contain ASCII characters). All sizes and offsets are in bytes, unless specified otherwise. Structure members are listed in the following general form: offset from the beginning of the structure: data type(array size) member name : member description

{{heading |level=3 |title=General Archive Layout}}

* [Archive Header](#Archive-Header)
* [File Data](#File-Data)
* File Data - Special Files
* [Hash Table](#Hash-Table)
* [Block Table](#Block-Table)
* [Extended Block Table](#Extended-Block-Table)
* [Strong Digital signature](#Strong-Digital-Signature---Generics)

This is the usual archive layout, but it is not mandatory. Some archives have been observed placing the hash table and file table after the archive header, and before the file data.

However, beginning with StarCraft II, the block table must immediately follow the hash table.


{{heading |level=3 |title=Archive Header}}

{{heading |level=4 |link=archive-header-magic |title=Magic}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Indicates that the file is a MoPaQ archive.}}
  {{formatlbl |label=Values |value=Must be ASCII "MPQ" 0x1A.}}
{{end-formattable}}

{{heading |level=4 |title=Header Size}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0004}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Size of the archive header.}}
{{end-formattable}}

{{heading |level=4 |title=Archive Size}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0008}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Size of the whole archive, including the header. Does not include the strong digital signature, if present. This size is used, among other things, for determining the region to hash in computing the digital signature. This field is deprecated in the Burning Crusade MoPaQ format, and the size of the archive is calculated as the size from the beginning of the archive to the end of the hash table, block table, or extended block table (whichever is largest).}}
{{end-formattable}}

{{heading |level=4 |title=Format Version}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x000C}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=MoPaQ format version. MPQAPI will not open archives where this is negative. Known versions:}}
  {{formatlbl |label=Versions |value={{begin-bittable}}
    {{formatbitlbl |label=0x0000 |value=Original format. Header Size should be 0x20, and large archives are not supported.}}
    {{formatbitlbl |label=0x0001 |value=Burning Crusade format. Header size should be 0x2C, and large archives are supported.}}
  {{end-bittable}} }}
{{end-formattable}}

{{heading |level=4 |title=Sector Size Shift}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x000E}}
  {{formatlbl |label=Length |value=1 byte}}
  {{formatlbl |label=Description |value=Power of two exponent specifying the number of 512-byte disk sectors in each logical sector in the archive. The size of each logical sector in the archive is {{math |eq=512 \cdot 2^\text{Sector Size Shift} }}. Bugs in the Storm library dictate that this should always be 3 (4096 byte sectors).}}
{{end-formattable}}

{{heading |level=4 |title=Hash Table Offset}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0010}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Offset to the beginning of the hash table, relative to the beginning of the archive.}}
{{end-formattable}}

{{heading |level=4 |title=Block Table Offset}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0014}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Offset to the beginning of the block table, relative to the beginning of the archive.}}
{{end-formattable}}

{{heading |level=4 |title=Hash Table Entries}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0018}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Number of entries in the hash table.}}
  {{formatlbl |label=Values |value=Must be a power of two, and must be less than {{math |eq=2^16}} for the original MoPaQ format, or less than {{math |eq=2^20}} for the Burning Crusade format.}}
{{end-formattable}}

{{heading |level=4 |title=Block Table Entries}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x001C}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Number of entries in the block table.}}
{{end-formattable}}

Fields only present in the Burning Crusade format and later:

{{heading |level=4 |title=Extended Block Table Offset}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0020}}
  {{formatlbl |label=Length |value=8 bytes}}
  {{formatlbl |label=Description |value=Offset to the beginning of the extended block table, relative to the beginning of the archive.}}
{{end-formattable}}

{{heading |level=4 |title=Hash Table Offset High}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0028}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=High 16 bits of the hash table offset for large archives.}}
{{end-formattable}}

{{heading |level=4 |title=Block Table Offset High}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x002A}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=High 16 bits of the block table offset for large archives.}}
{{end-formattable}}

The archive header is the first structure in the archive, at archive offset 0; however, the archive does not need to be at offset 0 of the containing file. The offset of the archive in the file is referred to here as ArchiveOffset. If the archive is not at the beginning of the file, it must begin at a disk sector boundary (512 bytes). Early versions of Storm require that the archive be at the end of the containing file (ArchiveOffset + ArchiveSize = file size), but this is not required in newer versions (due to the strong digital signature not being considered a part of the archive).

{{heading |level=3 |title=Block Table}}

The block table contains entries for each region in the archive. Regions may be either files, empty space, which may be overwritten by new files (typically this space is from deleted file data), or unused block table entries. Empty space entries should have BlockOffset and BlockSize nonzero, and FileSize and Flags zero; unused block table entries should have BlockSize, FileSize, and Flags zero. The block table is encrypted, using the hash of "(block table)" as the key. Each entry is structured as follows:

{{heading |level=4 |title=Block Offset}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Offset of the beginning of the block, relative to the beginning of the archive.}}
{{end-formattable}}

{{heading |level=4 |title=Block Size}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0004}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Size of the block in the archive.}}
{{end-formattable}}

{{heading |level=4 |title=File Size}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0008}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Size of the file data stored in the block. Only valid if the block is a file; otherwise meaningless, and should be 0. If the file is compressed, this is the size of the uncompressed file data.}}
{{end-formattable}}

{{heading |level=4 |title=Flags}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x000C}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Bit mask of the flags for the block. The following values are conclusively identified:}}
  {{formatlbl |label=Flags  |value={{begin-bittable}}
    {{formatbitlbl |label=0x80000000 |value=Block is a file, and follows the file data format; otherwise, block is free space or unused. If the block is not a file, all other flags should be cleared, and FileSize should be 0.}}
    {{formatbitlbl |label=0x04000000 |value=File has checksums for each sector (explained in the File Data section). Ignored if file is not compressed or imploded.}}
    {{formatbitlbl |label=0x02000000 |value=File is a deletion marker, indicating that the file no longer exists. This is used to allow patch archives to delete files present in lower-priority archives in the search chain.}}
    {{formatbitlbl |label=0x01000000 |value=File is stored as a single unit, rather than split into sectors.}}
    {{formatbitlbl |label=0x00020000 |value=The file's encryption key is adjusted by the block offset and file size (explained in detail in the File Data section). File must be encrypted.}}
    {{formatbitlbl |label=0x00010000 |value=File is encrypted.}}
    {{formatbitlbl |label=0x00000200 |value=File is compressed. File cannot be imploded.}}
    {{formatbitlbl |label=0x00000100 |value=File is imploded. File cannot be compressed.}}
  {{end-bittable}} }}
{{end-formattable}}


{{heading |level=3 |title=Extended Block Table}}

The extended block table was added to support archives larger than 4 gigabytes ({{math |eq=2^32}} bytes). The table contains the upper bits of the archive offsets for each block in the block table. It is simply an array of int16s, which become bits 32-47 of the archive offsets for each block, with bits 48-63 being zero. Individual blocks in the archive are still limited to 4 gigabytes in size. This table is only present in Burning Crusade format archives that exceed 4 gigabytes size.

Unlike the hash and block tables, the extended block table is not encrypted nor compressed.


{{heading |level=3 |title=Hash Table}}

Instead of storing file names, for quick access MoPaQs use a fixed, power of two-size hash table of files in the archive. A file is uniquely identified by its file path, its language, and its platform.

The home entry for a file in the hash table is computed as a hash of the file path. In the event of a collision (the home entry is occupied by another file), progressive overflow is used, and the file is placed in the next available hash table entry. Searches for a desired file in the hash table proceed from the home entry for the file until either the file is found, the entire hash table is searched, or an empty hash table entry (FileBlockIndex of 0xFFFFFFFF) is encountered.

The hash table is always encrypted, using the hash of "(hash table)" as the key.

Prior to StarCraft II, the hash table is stored uncompressed. In StarCraft II, however, the table may optionally be compressed. If the offset of the block table is not equal to the offset of the hash table plus the uncompressed size, StarCraft II interprets the hash table as being compressed (not imploded). This calculation assumes that the block table immediately follows the hash table, and will fail or crash otherwise.

Each entry is structured as follows:

{{heading |level=4 |title=File Path Hash A}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=The hash of the file path, using method A.}}
{{end-formattable}}

{{heading |level=4 |title=File Path Hash B}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0004}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=The hash of the file path, using method B.}}
{{end-formattable}}

{{heading |level=4 |title=Language}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0008}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=The language of the file. This is a Windows LANGID data type, and uses the same values. 0 indicates the default language (American English), or that the file is language-neutral.}}
{{end-formattable}}

{{heading |level=4 |title=Platform}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x000A}}
  {{formatlbl |label=Length |value=1 byte}}
  {{formatlbl |label=Description |value=The platform the file is used for. 0 indicates the default platform. No other values have been observed.}}
{{end-formattable}}

{{heading |level=4 |title=File Block Index}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x000C}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=If the hash table entry is valid, this is the index into the block table of the file. Otherwise, one of the following two values:{{linebreak}} 0xFFFFFFFF: Hash table entry is empty, and has always been empty. Terminates searches for a given file.{{linebreak}} 0xFFFFFFFE: Hash table entry is empty, but was valid at some point (in other words, the file was deleted). Does not terminate searches for a given file.}}
{{end-formattable}}


{{heading |level=3 |title=Extended Attributes}}

The extended attributes are optional file attributes for files in the block table. These attributes were added at times after the MoPaQ format was already finalized, and it is not necessary for every archive to have all (or any) of the extended attributes. If an archive contains a given attribute, there will be an instance of that attribute for every block in the block table, although the attribute will be meaningless if the block is not a file. The order of the attributes for blocks correspond to the order of the blocks in the block table, and are of the same number. The attributes are stored in parallel arrays in the "(attributes)" file (default language and platform), in the archive. The attributes corresponding to this file need not be valid (and logically cannot be). Unlike all the other structures in the MoPaQ format, entries in the extended attributes are NOT guaranteed to be aligned. Also note that in some archives, malicious zeroing of the attributes has been observed, perhaps with the intent of breaking archive viewers. This file is structured as follows:

{{heading |level=4 |title=Version}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Specifies the extended attributes format version. For now, must be 100.}}
{{end-formattable}}

{{heading |level=4 |title=Attributes Present}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0004}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Bit mask of the extended attributes present in the archive:}}
  {{formatlbl |label=Attributes  |value={{begin-bittable}}
    {{formatbitlbl |label=0x00000001 |value=File CRC32s.}}
    {{formatbitlbl |label=0x00000002 |value=File timestamps.}}
    {{formatbitlbl |label=0x00000004 |value=File MD5s.}}
  {{end-bittable}} }}
{{end-formattable}}

{{heading |level=4 |title=CSC32s}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0008}}
  {{formatlbl |label=Length |value={{math |eq=4\: \text{bytes} \cdot \text{Block Table Entries} }}}}
  {{formatlbl |label=Description |value=CRC32s of the (uncompressed) file data for each block in the archive. Omitted if the archive does not have CRC32s.}}
{{end-formattable}}

{{heading |level=4 |title=Timestamps}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value={{math |eq=\text{sizeof}(FILETIME) \cdot \text{Block Table Entries} }}}}
  {{formatlbl |label=Description |value=Timestamps for each block in the archive. The format is that of the Windows FILETIME structure. Omitted if the archive does not have timestamps.}}
{{end-formattable}}

{{heading |level=4 |title=MD5s}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value={{math |eq=\text{sizeof}(MD5) \cdot \text{Block Table Entries} }}}}
  {{formatlbl |label=Description |value=MD5s of the (uncompressed) file data for each block in the archive. Omitted if the archive does not have MD5s.}}
{{end-formattable}}


{{heading |level=3 |title=File Data}}

The data for each file is composed of the following structure:

{{heading |level=4 |title=Sector Offset Table}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value={{math |eq=4\: \text{bytes} \cdot (\text{Sectors In File}* + 1)}}}}
  {{formatlbl |label=Description |value=Offsets to the start of each sector, relative to the beginning of the file data. The last entry contains the total compressed file size, making it possible to easily calculate the size of any given sector by simple subtraction. This table is not present or necessary if the file is not compressed.}}
{{end-formattable}}

{{heading |level=4 |title=Sectors In File}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value={{math |eq=\text{sizeof}(SECTOR)}}}}
  {{formatlbl |label=Description |value=Data of each sector in the file, packed end to end (see details below).}}
{{end-formattable}}

Normally, file data is split up into sectors, for simple streaming. All sectors, save for the last, will contain as many bytes of file data as specified in the archive header's [Sector Size Shift](#Sector-Size-Shift); the last sector may contain less than this, depending on the size of the entire file's data. If the file is compressed or imploded, the sector will be smaller or the same size as the file data it contains. Individual sectors in a compressed or imploded file may be stored uncompressed; this occurs if and only if the file data the sector contains could not be compressed by the algorithm(s) used (if the compressed sector size was greater than or equal to the size of the file data), and is indicated by the sector's size in [Sector Offset Table](#Sector-Offset-Table) being equal to the size of the file data in the sector (which may be calculated from the [File Size](#File-Size)).

Sector checksums, when present, are stored as an additional sector at the end of the file, and such files consequently have an additional entry in the sector table; however, unlike the other sectors in the file, this sector is always compressed (not imploded) and unencrypted. This sector consists of an array of checksums, one for each sector in the file minus the checksum sector itself. Each checksum is computed from a compressed but unencrypted sector; for further details of the implementation of sector checksums, see [Verifying a Sector Checksum](#Verifying-a-Sector-Checksum) below.

The format of each sector depends on the kind of sector it is. Uncompressed sectors are simply the the raw file data contained in the sector. Imploded sectors are the raw compressed data following compression with the implode algorithm (these sectors can only be in imploded files). Compressed sectors (only found in compressed - not imploded - files) are compressed with one or more compression algorithms, and have the following structure:

{{heading |level=4 |title=Compression Mask}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=1 byte}}
  {{formatlbl |label=Description |value=Mask of the compression types applied to this sector.}}
{{end-formattable}}

{{heading |level=4 |title=Sector Data}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0001}}
  {{formatlbl |label=Length |value={{math |eq=1\: \text{byte} \cdot (\text{Sector Size} - 1)}}}}
  {{formatlbl |label=Description |value=The compressed data for the sector.}}
{{end-formattable}}

[Compression Mask](#Compression-Mask) indicates which compression algorithm(s) to apply to the compressed sector. This byte counts towards the total sector size, and the sector will be stored uncompressed if the data cannot be compressed by at least two bytes; in other words, there must be an overall gain of at least one byte through compression. As well, this byte is encrypted with the sector data, if applicable. The following compression algorithms are defined (for implementations of these algorithms, see [StormLib](https://github.com/ladislav-zezula/StormLib)):

{{begin-bittable}}
  {{formatbitlbl |label=0x20 |value=Sparse compressed. Added in StarCraft II.}}
  {{formatbitlbl |label=0x40 |value=IMA ADPCM mono.}}
  {{formatbitlbl |label=0x80 |value=IMA ADPCM stereo.}}
  {{formatbitlbl |label=0x01 |value=Huffman encoded.}}
  {{formatbitlbl |label=0x02 |value=Deflated (see ZLib). Added in WarCraft III.}}
  {{formatbitlbl |label=0x08 |value=Imploded (see PKWare Data Compression Library).}}
  {{formatbitlbl |label=0x10 |value=BZip2 compressed (see BZip2). Added in World of WarCraft: The Burning Crusade.}}
{{end-bittable}}

Prior to StarCraft II, this byte is interpreted as a bit mask of algorithms to apply. Algorithms, which may be combined arbitrarily, are applied in the order entries are shown above during compression, and in the opposite order during decompression.

In StarCraft II, this byte is now processed via a single large lookup table of values, which translates each possible value into either one or two different compression algorithms. Algorithms may no longer be arbitrarily combined, but must come from a list of valid combinations; specifically, most compression types (e.g. Deflate and Implode) are now mutually exclusive, and may only be combined with a small number of other algorithms (e.g. IMA ADPCM), which themselves are mutually exclusive. Furthermore, there is one exception (12h) where the value is not two algorithms combined, but a single, new algorithm (LZMA). The list of valid combinations:

{{begin-bittable}}
  {{formatbitlbl |label=0x12 |value=LZMA compression. Added in StarCraft II.}}
  {{formatbitlbl |label=0x22 |value=Sparse compression + Deflate}}
  {{formatbitlbl |label=0x30 |value=Sparse compression + BZip2}}
  {{formatbitlbl |label=0x41 |value=Mono IMA ADPCM + Huffman encoding}}
  {{formatbitlbl |label=0x48 |value=Mono IMA ADPCM + Implode}}
  {{formatbitlbl |label=0x81 |value=Stereo IMA ADPCM + Huffman encoding}}
  {{formatbitlbl |label=0x88 |value=Stereo IMA ADPCM + Implode}}
{{end-bittable}}

If the file is stored as a single unit (indicated in the file's Flags), there is effectively only a single sector, which contains the entire file data.

If the file is encrypted, each sector (after compression/implosion, if applicable) is encrypted with the file's key. The base key for a file is determined by a hash of the file name stripped of the directory (i.e. the key for a file named "directory\\\\file" would be computed as the hash of "file"). If this key is adjusted, as indicated in the file's Flags, the final key is calculated as ((base key + [Block Offset](#Block-Offset)) XOR [File Size](#File-Size)). Each sector is encrypted using the key + the 0-based index of the sector in the file. The [Sector Offset Table](#Sector-Offset-Table), if present, is encrypted using the key - 1.

The [Sector Offset Table](#Sector-Offset-Table) is omitted when the sizes and offsets of all sectors in the file are calculatable from the [File Size](#File-Size). This can happen in several circumstances. If the file is not compressed/imploded, then the size and offset of all sectors is known, based on the archive's [Sector Size Shift](#Sector-Size-Shift). If the file is stored as a single unit compressed/imploded, then the [Sector Offset Table](#Sector-Offset-Table) is omitted, as the single file "sector" corresponds to [Block Size](#Block-Size) and [File Size](#File-Size), as mentioned previously. However, the [Sector Offset Table](#Sector-Offset-Table) will be present if the file is compressed/imploded and the file is not stored as a single unit, even if there is only a single sector in the file (the size of the file is less than or equal to the archive's sector size).


{{heading |level=3 |title=Listfile}}

The listfile is a very simple extension to the MoPaQ format that contains the file paths of (most) files in the archive. The languages and platforms of the files are not stored in the listfile. The listfile is contained in the file "(listfile)" (default language and platform), and is simply a text file with file paths separated by `;`, 0x0D, 0x0A, or some combination of these. The file "(listfile)" may not be listed in the listfile.


{{heading |level=3 |title=Weak Digital Signature}}

The weak digital signature is a RSASSA-PKCS1-v1_5 digital signature, using the MD5 hashing algorithm and a 512-bit (weak) RSA key (for more information about this protocol, see the RSA Labs PKCS1 specification). The public key and exponent are stored in a resource in Storm, the private key is stored in a separate file, whose filename is passed to MPQAPI (the private key is not stored in MPQAPI). The signature is stored uncompressed, unencrypted in the file "(signature)" (default language and platform) in the archive. The archive is hashed from the beginning of the archive (ArchiveOffset in the containing file) to the end of the archive (the length indicated by ArchiveSize, or calculated in the Extended MoPaQ format); the signature file is added to the archive before signing, and the space occupied by the file is considered to be all binary 0s during signing/verification. This file is structured as follows:

{{heading |level=4 |link=weak-signature-unknown1 |title=Unknown}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Unknown.}}
  {{formatlbl |label=Values |value=Must be 0.}}
{{end-formattable}}

{{heading |level=4 |link=weak-signature-unknown2 |title=Unknown}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0004}}
  {{formatlbl |label=Length |value=1 bytes}}
  {{formatlbl |label=Description |value=Unknown.}}
  {{formatlbl |label=Values |value=Must be 0.}}
{{end-formattable}}

{{heading |level=4 |link=weak-signature-signature |title=Signature}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0008}}
  {{formatlbl |label=Length |value=64 bytes}}
  {{formatlbl |label=Description |value=The digital signature. Like all other numbers in the MoPaQ format, this is stored in little-endian order.}}
{{end-formattable}}

The structure of the signature, when decrypted, follows the RSASSA-PKCS1-v1_5 specification; this format is rather icky to work with (Quantam wrote a program to verify this signature using nothing but an MD5 function and huge integer functions; it wasn't pleasant), and best left to an encryption library, such as OpenSSL as shown below:

{{begincode}}
int mpq_verify_weak_signature(RSA *public_key, const unsigned char *signature, const unsigned char *digest) {
    unsigned char reversed_signature[MPQ_WEAK_SIGNATURE_SIZE];
    memcpy(reversed_signature, signature + 8, MPQ_WEAK_SIGNATURE_SIZE);
    memrev(reversed_signature, MPQ_WEAK_SIGNATURE_SIZE);

    return RSA_verify(NID_md5, digest, MD5_DIGEST_LENGTH, reversed_signature, MPQ_WEAK_SIGNATURE_SIZE, public_key);
}
{{endcode}}

MPQKit includes the weak signature public RSA key in PEM format since r73.


{{heading |level=3 |title=Strong Digital Signature - Generics}}

The strong digital signature consists of a SHA-1 digest with extremely simple padding, encrypted using straight RSA encryption. All known Blizzard keys are 2048-bit (strong) RSA keys; a default key is stored in Storm. Obviously, any RSA key may be used; in fact, an archive signed with the default key has never been seen in the wild. The strong digital signature is stored immediately after the archive, in the containing file. The entire archive (ArchiveSize bytes, starting at ArchiveOffset in the containing file) is hashed as a single block (there is one known exception to that algorithm, see below). In addition, a signature tail may be appended to the SHA-1 digest before it is finalized; this can be any arbitrary blob of data. The signature has the following format:

{{heading |level=4 |link=strong-signature-magic |title=Magic}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Indicates the presence of a digital signature.}}
  {{formatlbl |label=Values |value=Must be "NGIS" ("SIGN" backwards).}}
{{end-formattable}}

{{heading |level=4 |link=strong-signature-signature |title=Signature}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0004}}
  {{formatlbl |label=Length |value=256 bytes}}
  {{formatlbl |label=Description |value=The digital signature, stored in little-endian format.}}
{{end-formattable}}

When the Signature field is decrypted with the public key, and the resulting large integer is stored in little-endian order, it is structured as follows:

{{heading |level=4 |link=strong-signature-padding1 |title=Padding}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=1 byte}}
  {{formatlbl |label=Description |value=Padding.}}
  {{formatlbl |label=Values |value=Must be 0x0B.}}
{{end-formattable}}

{{heading |level=4 |link=strong-signature-padding2 |title=Padding}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0001}}
  {{formatlbl |label=Length |value=235 bytes}}
  {{formatlbl |label=Description |value=Padding.}}
  {{formatlbl |label=Values |value=Must be 0xBB.}}
{{end-formattable}}

{{heading |level=4 |title=SHA-1}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x00EC}}
  {{formatlbl |label=Length |value=20 bytes}}
  {{formatlbl |label=Description |value=SHA-1 digest of the archive, in standard SHA-1 byte order.}}
{{end-formattable}}


{{heading |level=3 |title=Strong Digital Signature - Specifics}}

This section aims at giving specific information about the usage of the various known Blizzard public keys, as well as known SHA-1 digest tails.

{{heading |level=4 |title=Warcraft 3 maps}}

Warcraft 3 maps (.w3m and .w3x) are composed of a map header, followed by an MPQ archive at offset 512, followed by a strong digital signature. The Warcraft 3 Map key is used for Warcraft 3 map signatures; the SHA-1 digest is constructed from the content of the entire file, including the map header, up to the end of the archive. That is, (MapHeaderSize + ArchiveSize bytes, starting at 0 in the containing file). Once the map file has been digested, a tail is appended to the SHA-1 digest; the tail is the uppercased file name of the map.

{{heading |level=4 |title=World of Warcraft Macintosh patches}}

World of Warcraft Macintosh patches are embodied by a patch program ("patcher"), which contains in its bundle resources a standalone.MPQ archive, which stores the patch's content. standalone.MPQ archives are signed with the World of Warcraft Macintosh Patch key; the SHA-1 digest is constructed normally as described in the general case. Once the archive has been digested, a tail is appended to the SHA-1 digest; the tail is "ARCHIVE".

It should be noted that World of Warcraft Windows patches are signed using the weak signature scheme.

{{heading |level=4 |title=World of Warcraft survey}}

World of Warcraft stores a Survey.MPQ archive in its WDB directory. Survey.MPQ archives are signed with the World of Warcraft Survey key; the SHA-1 digest is constructed normally as described in the general case. Once the archive has been digested, a tail is appended to the SHA-1 digest; the tail is "ARCHIVE".

It should be noted that the Survey.MPQ archive has not yet been observed in publicly available builds of Burning Crusade.


{{heading |level=3 |title=User Data}}

The second version of the MoPaQ format, first used in Burning Crusade, features a mechanism to store some amount of data outside the archive proper, though the reason for this mechanism is not known. This is implemented by means of a shunt block that precedes the archive itself. The format of this block is as follows:

{{heading |level=4 |link=user-data-magic |title=Magic}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Indicates that this is a shunt block.}}
  {{formatlbl |label=Values |value=Must be ASCII "MPQ" 0x1B.}}
{{end-formattable}}

{{heading |level=4 |title=User Data Size}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0004}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=The number of bytes that have been allocated in this archive for user data. This does not need to be the exact size of the data itself, but merely the maximum amount of data which may be stored in this archive.}}
{{end-formattable}}

{{heading |level=4 |title=Archive Header Offset}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0008}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=The offset in the file at which to continue the search for the archive header.}}
{{end-formattable}}

{{heading |level=4 |link=user-data-user-data |title=User Data}}
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x000C}}
  {{formatlbl |label=Length |value=`User Data Size`}}
  {{formatlbl |label=Description |value=The block to store user data in.}}
{{end-formattable}}

When Storm encounters this block in its search for the archive header, it saves the location of the shunt block and resumes its search for the archive header at the offset specified in the shunt.

Blizzard-generated archives place the shunt at the beginning of the file, and begin the archive itself at the next 512-byte boundary after the end of the shunt block.


{{heading |level=3 |title=User Data File}}

Some archives, based on criteria that are not yet known, are unable to contain a shunt block. In this case, user data is stored in a normal file inside the archive named "(user data)".


{{heading |level=2 |title=Algorithm Source Code}}

All of the sample code here assumes little endian machine byte order, that the short type is 16 bits, that the long type is 32 bits, and that the long long type is 64 bits. Adjustments must be made if these assumptions are not correct on a given platform. All code not credited otherwise was written by myself in the writing of this specification.


{{heading |level=3 |title=Encryption/Decryption}}

Based on code from [StormLib](https://github.com/ladislav-zezula/StormLib).

{{begincode}}
unsigned long dwCryptTable[0x500];

// The encryption and hashing functions use a number table in their procedures.
// This table must be initialized before the functions are called the first time.
void InitializeCryptTable()
{
    unsigned long seed   = 0x00100001;
    unsigned long index1 = 0;
    unsigned long index2 = 0;
    int i;

    for (index1 = 0; index1 < 0x100; index1++)
    {
        for (index2 = index1, i = 0; i < 5; i++, index2 += 0x100)
        {
            unsigned long temp1, temp2;

            seed  = (seed * 125 + 3) % 0x2AAAAB;
            temp1 = (seed & 0xFFFF) << 0x10;

            seed  = (seed * 125 + 3) % 0x2AAAAB;
            temp2 = (seed & 0xFFFF);

            dwCryptTable[index2] = (temp1 | temp2);
        }
    }
}

void EncryptData(void *lpbyBuffer, unsigned long dwLength, unsigned long dwKey)
{
    assert(lpbyBuffer);

    unsigned long *lpdwBuffer = (unsigned long *)lpbyBuffer;
    unsigned long seed = 0xEEEEEEEE;
    unsigned long ch;

    dwLength /= sizeof(unsigned long);

    while(dwLength-- > 0)
    {
        seed += dwCryptTable[0x400 + (dwKey & 0xFF)];
        ch = *lpdwBuffer ^ (dwKey + seed);

        dwKey = ((~dwKey << 0x15) + 0x11111111) | (dwKey >> 0x0B);
        seed = *lpdwBuffer + seed + (seed << 5) + 3;

        *lpdwBuffer++ = ch;
    }
}

void DecryptData(void *lpbyBuffer, unsigned long dwLength, unsigned long dwKey)
{
    assert(lpbyBuffer);

    unsigned long *lpdwBuffer = (unsigned long *)lpbyBuffer;
    unsigned long seed = 0xEEEEEEEEL;
    unsigned long ch;

    dwLength /= sizeof(unsigned long);

    while(dwLength-- > 0)
    {
        seed += dwCryptTable[0x400 + (dwKey & 0xFF)];
        ch = *lpdwBuffer ^ (dwKey + seed);

        dwKey = ((~dwKey << 0x15) + 0x11111111L) | (dwKey >> 0x0B);
        seed = ch + seed + (seed << 5) + 3;

        *lpdwBuffer++ = ch;
    }
}
{{endcode}}


{{heading |level=3 |title=Hashing And File Key Computation}}

These functions may have been derived from [StormLib code](https://github.com/ladislav-zezula/StormLib) at some point in the very distant past. It was so long ago that I don't remember for certain.

{{begincode}}
// Different types of hashes to make with HashString
#define MPQ_HASH_TABLE_OFFSET 0
#define MPQ_HASH_NAME_A       1
#define MPQ_HASH_NAME_B       2
#define MPQ_HASH_FILE_KEY     3

// Based on code from StormLib.
unsigned long HashString(const char *lpszString, unsigned long dwHashType)
{
    assert(lpszString);
    assert(dwHashType <= MPQ_HASH_FILE_KEY);

    unsigned long  seed1 = 0x7FED7FEDL;
    unsigned long  seed2 = 0xEEEEEEEEL;
    int    ch;

    while (*lpszString != 0)
    {
        ch = toupper(*lpszString++);

        seed1 = dwCryptTable[(dwHashType * 0x100) + ch] ^ (seed1 + seed2);
        seed2 = ch + seed1 + seed2 + (seed2 << 5) + 3;
    }
    return seed1;
}

#define BLOCK_OFFSET_ADJUSTED_KEY 0x00020000L

unsigned long ComputeFileKey(
        const char *lpszFilePath,
        const BlockTableEntry &blockEntry,
        unsigned long nArchiveOffset
) {
    assert(lpszFilePath);

    // Find the file name part of the path
    const char *lpszFileName = strrchr(lpszFilePath, '\\\\');
    if (lpszFileName)
        lpszFileName++; // Skip the \\
    else
        lpszFileName = lpszFilePath;

    // Hash the name to get the base key
    unsigned long nFileKey = HashString(lpszFileName, MPQ_HASH_FILE_KEY);

    // Offset-adjust the key if necessary
    if (blockEntry.Flags & BLOCK_OFFSET_ADJUSTED_KEY)
        nFileKey = (nFileKey + blockEntry.BlockOffset) ^ blockEntry.FileSize;

    return nFileKey;
}
{{endcode}}


{{heading |level=3 |title=Conversion of FILETIME And time_t}}

This code assumes that the base ("zero") date for time_t is 01/01/1970. This is true on Windows, Unix System V systems, and Mac OS X. It is unknown whether this is true on all other platforms. You'll need to research this yourself, if you plan on porting it somewhere else.

**THIS CODE MAY BE INCORRECT, AND HAS NOT BEEN TESTED**

{{begincode}}
#define EPOCH_OFFSET 116444736000000000ULL // Number of 100 ns units between 01/01/1601 and 01/01/1970

bool GetTimeFromFileTime(const FILETIME &fileTime, time_t &time)
{
    // The FILETIME represents a 64-bit integer: the number of 100 ns units since January 1, 1601
    unsigned long long nTime = ((unsigned long long)fileTime.dwHighDateTime << 32) + fileTime.dwLowDateTime;

    if (nTime < EPOCH_OFFSET)
        return false;

    nTime -= EPOCH_OFFSET;  // Convert the time base from 01/01/1601 to 01/01/1970
    nTime /= 10000000ULL;   // Convert 100 ns to sec

    time = (time_t)nTime;

    // Test for overflow (FILETIME is 64 bits, time_t is 32 bits)
    if ((nTime - (unsigned long long)time) > 0)
        return false;

    return true;
}

void GetFileTimeFromTime(const time_t &time, FILETIME &fileTime)
{
    unsigned long long nTime = (unsigned long long)time;

    nTime *= 10000000ULL;
    nTime += EPOCH_OFFSET;

    fileTime.dwLowDateTime = (DWORD)nTime;
    fileTime.dwHighDateTime = (DWORD)(nTime >> 32);
}
{{endcode}}


{{heading |level=3 |title=Conversion of FILETIME And NSDate}}

MPQKit includes a category on [NSDate](https://web.archive.org/web/20120222093346/http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSDate_Class/Reference/Reference.html) to convert to and from NTFS FILETIME, and has been properly tested for correctness.
Forming a 64-Bit Large Archive Offset From 32-Bit And 16-Bit Components

{{begincode}}
unsigned long long MakeLargeArchiveOffset(unsigned long nOffsetLow, unsigned short nOffsetHigh)
{
    return ((unsigned long long)nOffsetHigh << 32) + (unsigned long long)nOffsetLow;
}
{{endcode}}


{{heading |level=3 |title=Verifying a Sector Checksum}}

{{begincode}}
bool VerifySectorChecksum(const void *buffer, unsigned int length, unsigned long checksum)
{
    if (checksum == 0)
        return true;    // Ignore the actual checksum

    unsigned long bufferChecksum = adler32(0, buffer, length);
    if (bufferChecksum == 0)
        // Can't deal with a 0 checksum
        bufferChecksum = (unsigned long)-1;

    return (bufferChecksum == checksum);
}
{{endcode}}


{{heading |level=3 |title=Finding Files}}

{{begincode}}
#define MPQ_HASH_ENTRY_EMPTY 0xFFFFFFFFL
#define MPQ_HASH_ENTRY_DELETED 0xFFFFFFFEL

bool FindFileInHashTable(
        const HashTableEntry *lpHashTable,
        unsigned long nHashTableSize,
        const char *lpszFilePath,
        unsigned short nLang,
        unsigned char nPlatform,
        unsigned long &iFileHashEntry
) {
    assert(lpHashTable);
    assert(nHashTableSize);
    assert(lpszFilePath);

    // Find the home entry in the hash table for the file
    unsigned long iInitEntry = HashString(lpszFilePath, MPQ_HASH_TABLE_OFFSET) & (nHashTableSize - 1);

    // Is there anything there at all?
    if (lpHashTable[iInitEntry].FileBlockIndex == MPQ_HASH_ENTRY_EMPTY)
        return false;

    // Compute the hashes to compare the hash table entry against
    unsigned long nNameHashA = HashString(lpszFilePath, MPQ_HASH_NAME_A),
        nNameHashB = HashString(lpszFilePath, MPQ_HASH_NAME_B),
        iCurEntry = iInitEntry;

    // Check each entry in the hash table till a termination point is reached
    do
    {
        if (lpHashTable[iCurEntry].FileBlockIndex != MPQ_HASH_ENTRY_DELETED)
        {
            if (lpHashTable[iCurEntry].FilePathHashA == nNameHashA
                && lpHashTable[iCurEntry].FilePathHashB == nNameHashB
                && lpHashTable[iCurEntry].Language == nLang
                && lpHashTable[iCurEntry].Platform == nPlatform)
            {
                iFileHashEntry = iCurEntry;

                return true;
            }
        }

        iCurEntry = (iCurEntry + 1) & (nHashTableSize - 1);
    } while (iCurEntry != iInitEntry && lpHashTable[iCurEntry].FileBlockIndex != MPQ_HASH_ENTRY_EMPTY);

    return false;
}
{{endcode}}


{{heading |level=3 |title=Deleting Files}}

{{begincode}}
bool DeleteFile(
        HashTableEntry *lpHashTable,
        unsigned long nHashTableSize,
        BlockTableEntry *lpBlockTable,
        const char *lpszFilePath,
        unsigned short nLang,
        unsigned char nPlatform
) {
    assert(lpHashTable);
    assert(nHashTableSize);
    assert(lpBlockTable);

    // Find the file in the hash table
    unsigned long iFileHashEntry;

    if (!FindFileInHashTable(lpHashTable, nHashTableSize, lpszFilePath, nLang, nPlatform, iFileHashEntry))
        return false;

    // Get the block table index before we nuke the hash table entry
    unsigned long iFileBlockEntry = lpHashTable[iFileHashEntry].FileBlockIndex;

    // Delete the file's entry in the hash table
    memset(&lpHashTable[iFileHashEntry], 0xFF, sizeof(HashTableEntry));

    // If the next entry is empty, mark this one as empty; otherwise, mark this as deleted.
    if (lpHashTable[(iFileHashEntry + 1) & (nHashTableSize - 1)].FileBlockIndex == MPQ_HASH_ENTRY_EMPTY)
        lpHashTable[iFileHashEntry].FileBlockIndex = MPQ_HASH_ENTRY_EMPTY;
    else
        lpHashTable[iFileHashEntry].FileBlockIndex = MPQ_HASH_ENTRY_DELETED;

    // If the block occupies space, mark the block as free space; otherwise, clear the block table entry.
    if (lpBlockTable[iFileBlockEntry].BlockSize > 0)
    {
        lpBlockTable[iFileBlockEntry].FileSize = 0;
        lpBlockTable[iFileBlockEntry].Flags = 0;
    }
    else
        memset(&lpBlockTable[iFileBlockEntry], 0, sizeof(BlockTableEntry);

    return true;
}
{{endcode}}


{{heading |level=2 |title=Constants}}
{{heading |level=3 |title=Locales}}

{{begincode}}
    MPQNeutral      = 0,
    MPQChinese      = 0x404,
    MPQCzech        = 0x405,
    MPQGerman       = 0x407,
    MPQEnglish      = 0x409,
    MPQSpanish      = 0x40a,
    MPQFrench       = 0x40c,
    MPQItalian      = 0x410,
    MPQJapanese     = 0x411,
    MPQKorean       = 0x412,
    MPQDutch        = 0x413,
    MPQPolish       = 0x415,
    MPQPortuguese   = 0x416,
    MPQRusssian     = 0x419,
    MPQEnglishUK    = 0x809
{{endcode}}


{{heading |level=2 |title=Copyright And Distribution}}

© 2006-2010 Justin Olbrantz (Quantam) and Jean-Francois Roy (BahamutZERO). All Rights Reserved.

Distribution and reproduction of this specification are allowed without limitation, as long as it is not altered; however, linking to [this authoritative copy](https://web.archive.org/web/20120222093346/https://wiki.devklog.net/index.php?title=The_MoPaQ_Archive_Format) is preferrable, to ensure that everyone has access to the most recent version. Quotation in other works is freely allowed, as long as the source and author of the quote are stated.
