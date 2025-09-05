# colorpicker

> A minimalist X11 colorpicker. Any mouse gesture except `<LeftClick>` will exit the program. More information: <https://github.com/ym1234/colorpicker>.

## Examples

### Launch colorpicker and print the hexadecimal and RGB value of each clicked pixel to `stdout`

```bash
colorpicker
```

### Only print the color of one clicked pixel and then exit

```bash
colorpicker --one-shot
```

### Print the color of each clicked pixel and quit when a key is pressed

```bash
colorpicker --quit-on-keypress
```

### Only print the RGB value

```bash
colorpicker --rgb
```

### Only print the hexadecimal value

```bash
colorpicker --hex
```
