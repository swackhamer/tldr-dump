# ruff-format

> An extremely fast Python code formatter. If no files or directories are specified, the current working directory is used by default. More information: <https://docs.astral.sh/ruff/formatter>.

## Examples

### Format given files or directories in-place

```bash
ruff format path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Print which files would have been modified and return a non-zero exit code if there are files to reformat, and zero otherwise

```bash
ruff format --check
```

### Print what changes would be made without modifying the files

```bash
ruff format --diff
```
