# hipstopgm

> Read a HIPS file as input and return a PGM image as output. If the HIPS file contains more than one frame in sequence, `hipstopgm` will concatenate all the frames vertically. More information: <https://netpbm.sourceforge.net/doc/hipstopgm.html>.

## Examples

### Convert a HIPS file into a PGM image

```bash
hipstopgm path/to/file.hips
```

### Suppress all informational messages

```bash
hipstopgm [-q|-quiet]
```

### Display version

```bash
hipstopgm [-v|-version]
```
