# pbmtext

> Render text as a PBM image. See also: `pbmtextps`. More information: <https://netpbm.sourceforge.net/doc/pbmtext.html>.

## Examples

### Render a single line of text as a PBM image

```bash
pbmtext "Hello World!" > path/to/output.pbm
```

### Render multiple lines of text as a PBM image

```bash
echo "Hello\nWorld!" | pbmtext > path/to/output.pbm
```

### Render text using a custom font supplied as a PBM file

```bash
pbmtext [-f|-font] path/to/font.pbm "Hello World!" > path/to/output.pbm
```

### Specify the number of pixels between characters and lines

```bash
echo "Hello\nWorld!" | pbmtext [-s|-space] 3 [-ls|-lspace] 10 > path/to/output.pbm
```
