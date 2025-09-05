# egrep

> Find patterns in files using extended `regex` (supports `?`, `+`, `{}`, `()`, and `|`). More information: <https://manned.org/egrep>.

## Examples

### Search for a pattern within a file

```bash
egrep "search_pattern" path/to/file
```

### Search for a pattern within multiple files

```bash
egrep "search_pattern" path/to/file1 path/to/file2 ...
```

### Search `stdin` for a pattern

```bash
cat path/to/file | egrep search_pattern
```

### Print file name and line number for each match

```bash
egrep [-H|--with-filename] [-n|--line-number] "search_pattern" path/to/file
```

### Search for a pattern in all files recursively in a directory, ignoring binary files

```bash
egrep [-r|--recursive] --binary-files=without-match "search_pattern" path/to/directory
```

### Search for lines that do not match a pattern

```bash
egrep [-v|--invert-match] "search_pattern" path/to/file
```
