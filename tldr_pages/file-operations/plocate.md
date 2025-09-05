# plocate

> Find filenames quickly. Make sure to run `sudo updatedb` to include new files. More information: <https://plocate.sesse.net>.

## Examples

### Look for patterns in the database (recomputed periodically)

```bash
plocate pattern
```

### Look for a file by its exact filename (a pattern containing no globbing characters is interpreted as `*pattern*`)

```bash
plocate */filename
```
