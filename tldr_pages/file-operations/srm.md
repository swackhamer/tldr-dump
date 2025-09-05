# srm

> Securely remove files or directories. Overwrites the existing data one or multiple times. Drop in replacement for rm. More information: <https://srm.sourceforge.net/srm.html>.

## Examples

### Remove a file after a single-pass overwriting with random data

```bash
srm [-s|--simple] path/to/file
```

### Remove a file after seven passes of overwriting with random data

```bash
srm -m path/to/file
```

### Recursively remove a directory and its contents overwriting each file with a single-pass of random data

```bash
srm [-r|--recursive] [-s|--simple] path/to/directory
```

### Prompt before every removal

```bash
srm [-i|--interactive] \*
```
