# vimdiff

> Open up two or more files in vim and show the differences between them. See also: `vim`, `vimtutor`, `nvim`. More information: <https://www.vim.org>.

## Examples

### Open two files and show the differences

```bash
vimdiff path/to/file1 path/to/file2
```

### Move the cursor to the window on the left|right

```bash
<Ctrl w><h>|<l>
```

### Jump to the previous difference

```bash
<[><c>
```

### Jump to the next difference

```bash
<]><c>
```

### Copy the highlighted difference from the other window to the current window

```bash
<d><o>
```

### Copy the highlighted difference from the current window to the other window

```bash
<d><p>
```

### Update all highlights and folds

```bash
<:>diffupdate
```

### Toggle the highlighted code fold

```bash
<z><a>
```
