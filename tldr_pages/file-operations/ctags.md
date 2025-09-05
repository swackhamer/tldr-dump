# ctags

> Generate an index (or tag) file of language objects found in source files for many popular programming languages. More information: <https://docs.ctags.io/en/latest/man/ctags.1.html>.

## Examples

### Generate tags for a single file, and output them to a file named "tags" in the current directory, overwriting the file if it exists

```bash
ctags path/to/file
```

### Generate tags for all files in the current directory, and output them to a specific file, overwriting the file if it exists

```bash
ctags -f path/to/file *
```

### Generate tags for all files in the current directory and all subdirectories

```bash
ctags --recurse
```

### Generate tags for a single file, and output them with start line number and end line number in JSON format

```bash
ctags --fields=+ne --output-format=json path/to/file
```
