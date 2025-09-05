# magick-import

> Capture some or all of an X server screen and save the image to a file. See also: `magick`. More information: <https://imagemagick.org/script/import.php>.

## Examples

### Capture the entire X server screen into a PostScript file

```bash
magick import -window root path/to/output.ps
```

### Capture contents of a remote X server screen into a PNG image

```bash
magick import -window root -display remote_host:screen.display path/to/output.png
```

### Capture a specific window given its ID as displayed by `xwininfo` into a JPEG image

```bash
magick import -window window_id path/to/output.jpg
```
