# rg

> Ripgrep, a recursive line-oriented search tool. Aims to be a faster alternative to `grep`. More information: <https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md>.

## Examples

### Recursively search current directory for a pattern (`regex`)

```bash
rg pattern
```

### Recursively search for a pattern in a file or directory

```bash
rg pattern path/to/file_or_directory
```

### Include hidden files and entries listed in `.gitignore`

```bash
rg [-.|--hidden] --no-ignore pattern
```

### Only search the files whose names match the glob pattern(s) (e.g. `README.*`)

```bash
rg pattern [-g|--glob] filename_glob_pattern
```

### Recursively list filenames in the current directory that match a pattern

```bash
rg --files | rg pattern
```

### Only list matched files (useful when piping to other commands)

```bash
rg [-l|--files-with-matches] pattern
```

### Show lines that do not match the pattern

```bash
rg [-v|--invert-match] pattern
```

### Search for a literal string pattern

```bash
rg [-F|--fixed-strings] -- string
```
