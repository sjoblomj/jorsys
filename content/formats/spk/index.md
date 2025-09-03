# SPK Format

SPK files are the star backgrounds of the Space tileset in StarCraft I.

* Download [SPK hexpat](spk-files/spk.hexpat) file for the [ImHex](https://imhex.werwolv.net/) hex editor.

## Layer count
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0000}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=Number of layers.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}



{{begin-formatbox |title=Image count for each layer}}

## Image count
{{begin-formattable}}
  {{formatlbl |label=Offset |value=0x0002}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=Number of images in the current layer.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}
{{end-formatbox}}



{{begin-formatbox |title=Star data for each layer}}

## Star X position
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=X position of the current star.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Star Y position
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=Y position of the current star.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Bitmap offset
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value=4 bytes}}
  {{formatlbl |label=Description |value=Offset to the image data.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 4294967295.}}
{{end-formattable}}
{{end-formatbox}}



{{begin-formatbox |title=Bitmap data for each star in each layer}}

## Bitmap width
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=Width of the image in pixels.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Bitmap height
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value=2 bytes}}
  {{formatlbl |label=Description |value=Height of the image in pixels.}}
  {{formatlbl |label=Values |value=Integer value between 0 and 65535.}}
{{end-formattable}}

## Bitmap data
{{begin-formattable}}
  {{formatlbl |label=Offset |value=Variable}}
  {{formatlbl |label=Length |value=bitmap width * bitmap height}}
  {{formatlbl |label=Description |value=Image data. Each byte is an offset to a palette image.}}
  {{formatlbl |label=Values |value=Each byte is an index value between 0 and 255.}}
{{end-formattable}}
{{end-formatbox}}
