# rector

> An automated tool for updating and refactoring PHP 5.3+ code. More information: <https://github.com/rectorphp/rector>.

## Examples

### Process a specific directory

```bash
rector process path/to/directory
```

### Process a directory without applying changes (dry run)

```bash
rector process path/to/directory --dry-run
```

### Process a directory and apply coding standards

```bash
rector process path/to/directory --with-style
```

### Display a list of available levels

```bash
rector levels
```

### Process a directory with a specific level

```bash
rector process path/to/directory --level level_name
```
