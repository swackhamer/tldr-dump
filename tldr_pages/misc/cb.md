# cb

> Cut, copy, and paste anything in the terminal. More information: <https://github.com/Slackadays/Clipboard>.

## Examples

### Show all clipboards

```bash
cb
```

### Copy a file to the clipboard

```bash
cb copy path/to/file
```

### Copy some text to the clipboard

```bash
cb copy "Some example text"
```

### Copy piped data to the clipboard

```bash
echo "Some example text" | cb
```

### Paste clipboard content

```bash
cb paste
```

### Pipe out clipboard content

```bash
cb | cat
```

### Show clipboard history

```bash
cb history
```

### Show clipboard information

```bash
cb info
```
