# xzgrep

> Search files possibly compressed with `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd` using `regex`. See also: `grep`. More information: <https://manned.org/xzgrep>.

## Examples

### Search for a pattern within a file

```bash
xzgrep "search_pattern" path/to/file
```

### Search for an exact string (disables `regex`)

```bash
xzgrep [-F|--fixed-strings] "exact_string" path/to/file
```

### Search for a pattern in all files showing line numbers of matches

```bash
xzgrep [-n|--line-number] "search_pattern" path/to/file
```

### Use extended `regex` (supports `?`, `+`, `{}`, `()` and `|`), in case-insensitive mode

```bash
xzgrep [-E|--extended-regexp] [-i|--ignore-case] "search_pattern" path/to/file
```

### Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match

```bash
xzgrep --context|before-context|after-context 3 "search_pattern" path/to/file
```

### Print file name and line number for each match with color output

```bash
xzgrep [-H|--with-filename] [-n|--line-number] --color=always "search_pattern" path/to/file
```

### Search for lines matching a pattern, printing only the matched text

```bash
xzgrep [-o|--only-matching] "search_pattern" path/to/file
```
