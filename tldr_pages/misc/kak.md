# kak

> Kakoune is a mode-based code editor implementing the "multiple selections" paradigm. Data can be selected and simultaneously edited in different locations, using multiple selections; users can also connect to the same session for collaborative editing. More information: <https://kakoune.org>.

## Examples

### Open a file and enter normal mode, to execute commands

```bash
kak path/to/file
```

### Enter insert mode from normal mode, to write text into the file

```bash
<i>
```

### Escape insert mode, to go back to normal mode

```bash
<Esc>
```

### Replace all instances of "foo" in the current file with "bar"

```bash
%sfoo<Enter>cbar<Esc>
```

### Unselect all secondary selections, and keep only the main one

```bash
<Space>
```

### Search for numbers and select the first two

```bash
/\d+<Enter>N
```

### Insert the contents of a file

```bash
<!>cat path/to/file<Enter>
```

### Save the current file

```bash
<:>w<Enter>
```
