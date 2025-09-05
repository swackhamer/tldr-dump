# zgrep

> Grep text patterns from files within compressed file (equivalent to `grep -Z`). More information: <https://manned.org/zgrep>.

## Examples

### Grep a pattern in a compressed file (case-sensitive)

```bash
zgrep pattern path/to/compressed/file
```

### Grep a pattern in a compressed file (case-insensitive)

```bash
zgrep [-i|--ignore-case] pattern path/to/compressed/file
```

### Output count of lines containing matched pattern in a compressed file

```bash
zgrep [-c|--count] pattern path/to/compressed/file
```

### Display the lines which don't have the pattern present (Invert the search function)

```bash
zgrep [-v|--invert-match] pattern path/to/compressed/file
```

### Grep a compressed file for multiple patterns

```bash
zgrep [-e|--regexp] "pattern_1" [-e|--regexp] "pattern_2" path/to/compressed/file
```

### Use extended `regex` (supporting `?`, `+`, `{}`, `()` and `|`)

```bash
zgrep [-E|--extended-regexp] regex path/to/file
```

### Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match

```bash
zgrep --context|before-context|after-context 3 pattern path/to/compressed/file
```
