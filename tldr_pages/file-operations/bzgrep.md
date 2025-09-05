# bzgrep

> Find patterns in `bzip2` compressed files using `grep`. More information: <https://manned.org/bzgrep>.

## Examples

### Search for a pattern within a compressed file

```bash
bzgrep "search_pattern" path/to/file
```

### Use extended `regex` (supports `?`, `+`, `{}`, `()` and `|`), in case-insensitive mode

```bash
bzgrep [-E|--extended-regexp] [-i|--ignore-case] "search_pattern" path/to/file
```

### Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match

```bash
bzgrep --context|before-context|after-context 3 "search_pattern" path/to/file
```

### Print file name and line number for each match

```bash
bzgrep [-H|--with-filename] [-n|--line-number] "search_pattern" path/to/file
```

### Search for lines matching a pattern, printing only the matched text

```bash
bzgrep [-o|--only-matching] "search_pattern" path/to/file
```

### Recursively search files in a bzip2 compressed tar archive for a pattern

```bash
bzgrep [-r|--recursive] "search_pattern" path/to/tar/file
```

### Search `stdin` for lines that do not match a pattern

```bash
cat path/to/bz/compressed/file | bzgrep [-v|--invert-match] "search_pattern"
```
