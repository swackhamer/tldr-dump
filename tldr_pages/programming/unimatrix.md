# unimatrix

> Simulate the Matrix look with Unicode characters. See also: `cmatrix`. More information: <https://github.com/will8211/unimatrix>.

## Examples

### Mimic the default output of `cmatrix` (no unicode, works in a TTY)

```bash
unimatrix --no-bold --speed 96 --character-list o
```

### No bold characters, slowly, with emojis, numbers, and a few symbols

```bash
unimatrix --no-bold --speed 50 --character-list ens
```

### Change the color of characters

```bash
unimatrix --color red|green|blue|white|...
```

### Select character set(s) using letter codes (see `unimatrix --help` for available character sets)

```bash
unimatrix --character-list character_sets
```

### Change the scrolling speed

```bash
unimatrix --speed number
```
