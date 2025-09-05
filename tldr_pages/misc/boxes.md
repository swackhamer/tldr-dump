# boxes

> Draw, remove, and repair ASCII art boxes. More information: <https://boxes.thomasjensen.com/boxes-man-1.html>.

## Examples

### Draw a box around a string

```bash
echo "string" | boxes
```

### Remove a box from a string

```bash
echo "string" | boxes [-r|--remove]
```

### Specify the box design

```bash
echo "string" | boxes [-d|--design] parchment
```

### Specify the box size (in columns by lines)

```bash
echo "string" | boxes [-s|--size] 10x5
```

### Align the box text [h]orizonally (at [l]eft, [c]enter or [r]ight)

```bash
echo "string" | boxes [-a|--align] hl|c|r
```

### Align the box text [v]ertically (at [t]op, [c]enter or [b]ottom)

```bash
echo "string" | boxes [-a|--align] vt|c|b
```

### [j]ustify the box text (at [l]eft, [c]enter or [r]ight)

```bash
echo "string" | boxes [-a|--align] jl|c|rvt
```
