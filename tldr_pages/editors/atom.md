# atom

> A cross-platform pluggable text editor. Plugins are managed by `apm`. Note: Atom has been sunsetted and is no longer actively maintained. More information: <https://atom.io/>.

## Examples

### Open a file or directory

```bash
atom path/to/file_or_directory
```

### Open a file or directory in a [n]ew window

```bash
atom -n path/to/file_or_directory
```

### Open a file or directory in an existing window

```bash
atom --add path/to/file_or_directory
```

### Open Atom in safe mode (does not load any additional packages)

```bash
atom --safe
```

### Prevent Atom from forking into the background, keeping Atom attached to the terminal

```bash
atom --foreground
```

### Wait for Atom window to close before returning (useful for Git commit editor)

```bash
atom --wait
```
