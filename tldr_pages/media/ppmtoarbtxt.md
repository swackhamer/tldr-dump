# ppmtoarbtxt

> Convert a PPM image to an arbitrary text format according to a template. More information: <https://netpbm.sourceforge.net/doc/ppmtoarbtxt.html>.

## Examples

### Convert a PPM image to text as specified by the given template

```bash
ppmtoarbtxt path/to/template path/to/image.ppm > path/to/output_file.txt
```

### Convert a PPM image to text as specified by the given template, prepend the contents of the specified head template

```bash
ppmtoarbtxt path/to/template -hd path/to/head_template path/to/image.ppm > path/to/output_file.txt
```

### Convert a PPM image to text as specified by the given template, append the contents of the specified tail template

```bash
ppmtoarbtxt path/to/template -hd path/to/tail_template path/to/image.ppm > path/to/output_file.txt
```

### Display version

```bash
ppmtoarbtxt [-v|-version]
```
