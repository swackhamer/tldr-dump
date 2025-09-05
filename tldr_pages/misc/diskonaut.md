# diskonaut

> Terminal disk space navigator, written in Rust. More information: <https://github.com/imsnif/diskonaut>.

## Examples

### Start `diskonaut` in the current directory

```bash
diskonaut
```

### Start `diskonaut` in a specific directory

```bash
diskonaut path/to/directory
```

### Show file sizes rather than their block usage on the disk

```bash
diskonaut --apparent-size path/to/directory
```

### Disable deletion confirmation

```bash
diskonaut --disable-delete-confirmation
```
