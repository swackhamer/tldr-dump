# dexdump

> Display information about Android DEX files. More information: <https://manned.org/man/debian-stretch/dexdump>.

## Examples

### Extract classes and methods from an APK file

```bash
dexdump path/to/file.apk
```

### Display header information of DEX files contained in an APK file

```bash
dexdump -f path/to/file.apk
```

### Display the dis-assembled output of executable sections

```bash
dexdump -d path/to/file.apk
```

### Output results to a file

```bash
dexdump -o path/to/file path/to/file.apk
```
