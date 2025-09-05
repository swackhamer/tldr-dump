# mtm

> Minimal terminal multiplexer. See also: `tmux`, `screen`. More information: <https://github.com/deadpixi/mtm>.

## Examples

### Start the program with default command chord (`<Ctrl g>`)

```bash
mtm
```

### Use `<Ctrl q>` as the command chord

```bash
mtm -c q
```

### Split and stack horizontally

```bash
<Ctrl g><h>
```

### Split and stack vertically

```bash
<Ctrl g><v>
```

### View scrollback buffer

```bash
<Ctrl g><PageUp>
```

### Switch terminals

```bash
<Ctrl g><ArrowKeys>
```

### Close current terminal

```bash
<Ctrl g><w>
```
