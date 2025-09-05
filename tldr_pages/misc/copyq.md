# copyq

> Clipboard manager with advanced features. More information: <https://copyq.readthedocs.io/en/latest/command-line.html>.

## Examples

### Launch CopyQ to store clipboard history

```bash
copyq
```

### Show current clipboard content

```bash
copyq clipboard
```

### Insert raw text into the clipboard history

```bash
copyq add -- text1 text2 text3
```

### Insert text containing escape sequences ('\n', '\t') into the clipboard history

```bash
copyq add firstline\nsecondline
```

### Print the content of the first 3 items in the clipboard history

```bash
copyq read 0 1 2
```

### Copy a file's contents into the clipboard

```bash
copyq copy < path/to/file.txt
```

### Copy a JPEG image into the clipboard

```bash
copyq copy image/jpeg < path/to/image.jpg
```
