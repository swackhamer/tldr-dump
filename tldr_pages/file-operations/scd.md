# scd

> File manager focused on shell integration. More information: <https://github.com/cshuaimin/scd>.

## Examples

### Index paths recursively for the very first run

```bash
scd -ar path/to/directory
```

### Change to a specific directory

```bash
scd path/to/directory
```

### Change to a path matching specific patterns

```bash
scd "pattern1 pattern2 ..."
```

### Show selection menu and ranking of 20 most likely directories

```bash
scd -v
```

### Add a specific alias for the current directory

```bash
scd --alias=word
```

### Change to a directory using a specific alias

```bash
scd word
```
