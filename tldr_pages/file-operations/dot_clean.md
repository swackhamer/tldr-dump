# dot_clean

> Merge ._* files with corresponding native files. More information: <https://keith.github.io/xcode-man-pages/dot_clean.1.html>.

## Examples

### Merge all `._*` files recursively

```bash
dot_clean path/to/directory
```

### Don't recursively merge all `._*` in a directory (flat merge)

```bash
dot_clean -f path/to/directory
```

### Merge and delete all `._*` files

```bash
dot_clean -m path/to/directory
```

### Only delete `._*` files if there's a matching native file

```bash
dot_clean -n path/to/directory
```

### Follow symlinks

```bash
dot_clean -s path/to/directory
```

### Print verbose output

```bash
dot_clean -v path/to/directory
```
