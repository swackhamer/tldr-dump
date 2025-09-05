# tre

> Show the contents of the current directory as a tree. Respects the `.gitignore` settings by default. More information: <https://github.com/dduan/tre>.

## Examples

### Print directories only

```bash
tre --directories
```

### Print JSON containing files in the tree hierarchy instead of the normal tree diagram

```bash
tre --json
```

### Print files and directories up to the specified depth limit (where 1 means the current directory)

```bash
tre --limit depth
```

### Print all hidden files and directories using the specified colorization mode

```bash
tre --all --color automatic|always|never
```

### Print files within the tree hierarchy, assigning a shell alias to each file that, when called, will open the associated file using the provided `command` (or in `$EDITOR` by default)

```bash
tre --editor command
```

### Print files within the tree hierarchy, excluding all paths that match the provided `regex`

```bash
tre --exclude regex
```

### Display version

```bash
tre --version
```

### Display help

```bash
tre --help
```
