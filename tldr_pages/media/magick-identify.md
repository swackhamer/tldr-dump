# magick-identify

> Describe the format and characteristics of image files. See also: `magick`. More information: <https://imagemagick.org/script/identify.php>.

## Examples

### Describe the format and basic characteristics of an image

```bash
magick identify path/to/image
```

### Describe the format and verbose characteristics of an image

```bash
magick identify -verbose path/to/image
```

### Collect dimensions of all JPEG files in the current directory and save them into a CSV file

```bash
magick identify -format "%f,%w,%h\n" *.jpg > path/to/filelist.csv
```
