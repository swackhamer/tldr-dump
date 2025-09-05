# nvim

> Neovim, a programmer's text editor based on Vim, provides several modes for different kinds of text manipulation. Pressing `<i>` in normal mode enters insert mode. `<Esc>` or `<Ctrl c>` goes back to normal mode, which doesn't allow regular text insertion. See also: `vim`, `vimtutor`, `vimdiff`. More information: <https://neovim.io>.

## Examples

### Open a file

```bash
nvim path/to/file
```

### Enter text editing mode (insert mode)

```bash
<Esc><i>
```

### Copy ("yank") or cut ("delete") the current line (paste it with `<p>`)

```bash
<Esc><y><y>|<d><d>
```

### Enter normal mode and undo the last operation

```bash
<Esc><u>
```

### Search for a pattern in the file (press `<n>`/`<N>` to go to next/previous match)

```bash
<Esc></>search_pattern<Enter>
```

### Perform a `regex` substitution in the whole file

```bash
<Esc><:>%s/regex/replacement/g<Enter>
```

### Enter normal mode and save (write) the file, and quit

```bash
<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>
```

### Quit without saving

```bash
<Esc><:>q!<Enter>
```
