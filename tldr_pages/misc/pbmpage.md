# pbmpage

> Generate a test pattern for printing. More information: <https://netpbm.sourceforge.net/doc/pbmpage.html>.

## Examples

### Generate a test pattern for printing onto US standard paper

```bash
pbmpage > path/to/file.pbm
```

### Generate a test pattern for printing onto A4 paper

```bash
pbmpage -a4 > path/to/file.pbm
```

### Specify the pattern to use

```bash
pbmpage 1|2|3 > path/to/file.pbm
```
