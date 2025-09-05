# loc

> Count lines of code. Written in Rust. More information: <https://github.com/cgag/loc>.

## Examples

### Print lines of code in the current directory

```bash
loc
```

### Print lines of code in the target directory

```bash
loc path/to/directory
```

### Print lines of code with stats for individual files

```bash
loc --files
```

### Print lines of code without .gitignore (etc.) files (e.g. two -u flags will additionally count hidden files and dirs)

```bash
loc [-u|--unrestricted]
```
