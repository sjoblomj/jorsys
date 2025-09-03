# TBL Format

TBL files are lists of strings, and the games use an index to look up the corresponding string. TBL files contain unit names and stats, dialog and game texts, file paths to resources such as graphics or sounds, etc. TBL files are used in StarCraft and WarCraft II.

For a converter between TBL files and TXT files, see [IronTBL](https://github.com/sjoblomj/irontbl).

* Download [TBL hexpat](tbl-files/tbl.hexpat) file for the [ImHex](https://imhex.werwolv.net/) hex editor.

## String count
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=Number of strings in file.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Offsets
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0002}}
  {{formatlbl |label=Length |value=2 bytes * string count}}
  {{formatlbl |label=Description |value=Offset in the file to the corresponding string.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Strings
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value=Offset for next string - offset for current string.}}
  {{formatlbl |label=Description |value=The string data. The string {{math |eq=n}} is between the offset for string {{math |eq=n}} and the offset for string {{math |eq=n+1}}. The last string is between its offset and the end of the file.}}
  {{formatlbl |label=Values |value=Any string data and control characters, including multiple NULL characters.}}
{{end-formattable}}
