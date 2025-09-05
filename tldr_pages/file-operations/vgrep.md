# vgrep

> A user friendly pager for grep. See also: `ugrep`, `rg`. More information: <https://github.com/vrothberg/vgrep/blob/main/docs/vgrep.1.md>.

## Examples

### Recursively search the current directory for a pattern and cache it

```bash
vgrep search_pattern
```

### Display the contents of the cache

```bash
vgrep
```

### Open the "4th" match from the cache in the default editor

```bash
vgrep [-s|--show] 4
```

### Display a context of "3" lines for each match in the cache

```bash
vgrep [-s|--show] [c|context]3
```

### Display the number of matches for each directory in the tree

```bash
vgrep [-s|--show] [t|tree]
```

### Display the number of matches for each file in the tree

```bash
vgrep [-s|--show] [f|files]
```

### Start an interactive shell with cached matches

```bash
vgrep [-i|--interactive]
```
