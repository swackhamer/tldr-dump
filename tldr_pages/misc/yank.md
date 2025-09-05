# yank

> Read input from `stdin` and display a selection interface that allows a field to be selected and copied to the clipboard. More information: <https://manned.org/yank>.

## Examples

### Yank using the default delimiters (\f, \n, \r, \s, \t)

```bash
sudo dmesg | yank
```

### Yank an entire line

```bash
sudo dmesg | yank -l
```

### Yank using a specific delimiter

```bash
echo hello=world | yank -d =
```

### Only yank fields matching a specific pattern

```bash
ps ux | yank -g "[0-9]+"
```
