# pbmmask

> Create a mask bitmap from a regular bitmap. See also: `pambackground`. More information: <https://netpbm.sourceforge.net/doc/pbmmask.html>.

## Examples

### Create a mask bitmap separating background from foreground

```bash
pbmmask path/to/image.pbm > path/to/output.pbm
```

### Expand the generated mask by one pixel

```bash
pbmmask [-r|-expand] path/to/image.pbm > path/to/output.pbm
```
