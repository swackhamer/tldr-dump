# bzegrep

> Find extended `regex` patterns in `bzip2` compressed files using `egrep`. More information: <https://manned.org/bzegrep>.

## Examples

### Search for extended `regex` (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-sensitive)

```bash
bzegrep "search_pattern" path/to/file
```

### Search for extended `regex` (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-insensitive)

```bash
bzegrep [-i|--ignore-case] "search_pattern" path/to/file
```

### Search for lines that do not match a pattern

```bash
bzegrep [-v|--invert-match] "search_pattern" path/to/file
```

### Print file name and line number for each match

```bash
bzegrep [-H|--with-filename] [-n|--line-number] "search_pattern" path/to/file
```

### Search for lines matching a pattern, printing only the matched text

```bash
bzegrep [-o|--only-matching] "search_pattern" path/to/file
```

### Recursively search files in a bzip2 compressed tar archive for a pattern

```bash
bzegrep [-r|--recursive] "search_pattern" path/to/file
```
