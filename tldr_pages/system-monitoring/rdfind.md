# rdfind

> Find files with duplicate content and get rid of them. More information: <https://rdfind.pauldreik.se/rdfind.1.html>.

## Examples

### Identify all duplicates in a given directory and output a summary

```bash
rdfind -dryrun true path/to/directory
```

### Replace all duplicates with hardlinks

```bash
rdfind -makehardlinks true path/to/directory
```

### Replace all duplicates with symlinks/soft links

```bash
rdfind -makesymlinks true path/to/directory
```

### Delete all duplicates and do not ignore empty files

```bash
rdfind -deleteduplicates true -ignoreempty false path/to/directory
```
