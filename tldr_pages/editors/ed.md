# ed

> The original Unix text editor. See also: `awk`, `sed`. More information: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

## Examples

### Start an interactive editor session with an empty document

```bash
ed
```

### Start an interactive editor session with an empty document and a specific prompt

```bash
ed [-p|--prompt] '> '
```

### Start an interactive editor session with user-friendly errors

```bash
ed [-v|--verbose]
```

### Start an interactive editor session with an empty document and without diagnostics, byte counts and '!' prompt

```bash
ed [-q|--quiet] [-s|--script]
```

### Start an interactive editor session without exit status change when command fails

```bash
ed [-l|--loose-exit-status]
```

### Edit a specific file (this shows the byte count of the loaded file)

```bash
ed path/to/file
```

### Replace a string with a specific replacement for all lines

```bash
,s/regex/replacement/g<Enter>
```

### Exit `ed`

```bash
q<Enter>
```
