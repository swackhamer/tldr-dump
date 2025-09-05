# look

> Display lines beginning with a prefix in a sorted file. See also: `grep`, `sort`. More information: <https://keith.github.io/xcode-man-pages/look.1.html>.

## Examples

### Search for lines beginning with a specific prefix in a specific file

```bash
look prefix path/to/file
```

### Case-insensitively search only on alphanumeric characters

```bash
look [-f|--ignore-case] [-d|--alphanum] prefix path/to/file
```

### Specify a string termination character (space by default)

```bash
look [-t|--terminate] ,
```

### Search in `/usr/share/dict/words` (`--ignore-case` and `--alphanum` are assumed)

```bash
look prefix
```
