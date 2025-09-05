# ag

> The Silver Searcher. Like `ack`, but aims to be faster. More information: <https://manned.org/ag>.

## Examples

### Find files containing "foo", and print the line matches in context

```bash
ag foo
```

### Find files containing "foo" in a specific directory

```bash
ag foo path/to/directory
```

### Find files containing "foo", but only list the filenames

```bash
ag [-l|--files-with-matches] foo
```

### Find files containing "FOO" case-insensitively, and print only the match, rather than the whole line

```bash
ag [-i|--ignore-case] [-o|--only-matching] FOO
```

### Find "foo" in files with a name matching "bar"

```bash
ag foo [-G|--file-search-regex] bar
```

### Find files whose contents match a `regex`

```bash
ag '^ba(r|z)$'
```

### Find files with a name matching "foo"

```bash
ag [-g|--filename-pattern] foo
```
