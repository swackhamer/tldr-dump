# pt

> Platinum Searcher. A code search tool similar to `ag`. More information: <https://github.com/monochromegane/the_platinum_searcher>.

## Examples

### Find files containing "foo" and print the files with highlighted matches

```bash
pt foo
```

### Find files containing "foo" and display count of matches in each file

```bash
pt [-c|--count] foo
```

### Find files containing "foo" as a whole word and ignore its case

```bash
pt [-wi|--word-regexp --ignore-case] foo
```

### Find "foo" in files with a given extension using a `regex`

```bash
pt [-G|--file-search-regexp]='\.bar$' foo
```

### Find files whose contents match the `regex`, up to 2 directories deep

```bash
pt --depth=2 -e '^ba[rz]*$'
```
