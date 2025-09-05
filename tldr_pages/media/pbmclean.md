# pbmclean

> Clean up a PBM image by erasing isolated black and white pixels. More information: <https://netpbm.sourceforge.net/doc/pbmclean.html>.

## Examples

### Clean up a PBM image by erasing isolated black and white pixels

```bash
pbmclean path/to/image.pbm > path/to/output.pbm
```

### Clean up only black/white pixels

```bash
pbmclean -black|white path/to/image.pbm > path/to/output.pbm
```

### Specify the minimum number of neighbouring pixels of the same color in order for a pixel not to be considered isolated

```bash
pbmclean [-m|-minneighbours] 3 path/to/image.pbm > path/to/output.pbm
```
