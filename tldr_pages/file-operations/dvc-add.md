# dvc-add

> Add changed files to the index. More information: <https://dvc.org/doc/command-reference/add>.

## Examples

### Add a single target file to the index

```bash
dvc add path/to/file
```

### Add a target directory to the index

```bash
dvc add path/to/directory
```

### Recursively add all the files in a given target directory

```bash
dvc add --recursive path/to/directory
```

### Add a target file with a custom `.dvc` filename

```bash
dvc add --file custom_name.dvc path/to/file
```
