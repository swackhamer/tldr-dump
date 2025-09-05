# pbmtextps

> Render text as a PBM image using PostScript. See also: `pbmtext`. More information: <https://netpbm.sourceforge.net/doc/pbmtextps.html>.

## Examples

### Render a single line of text as a PBM image

```bash
pbmtextps "Hello World!" > path/to/output.pbm
```

### Specify the font and font size

```bash
pbmtextps -font Times-Roman -fontsize 30 "Hello World!" > path/to/output.pbm
```

### Specify the desired left and top margins

```bash
pbmtextps [-l|-leftmargin] 70 [-t|-topmargin] 162 "Hello World!" > path/to/output.pbm
```

### Do not output the rendered text as a PBM image, but a PostScript program that would create this image

```bash
pbmtextps [-du|-dump-ps] "Hello World!" > path/to/output.ps
```
