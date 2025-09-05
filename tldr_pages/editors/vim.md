# vim

> Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation. Pressing `<i>` in normal mode enters insert mode. Pressing `<Esc>` goes back to normal mode, which enables the use of Vim commands. See also: `vimdiff`, `vimtutor`, `nvim`, `gvim`. More information: <https://www.vim.org>.

## Examples

### Open a file

```bash
vim path/to/file
```

### Open a file at a specified line number

```bash
vim +line_number path/to/file
```

### View Vim's help manual

```bash
<:>help<Enter>
```

### Save and quit the current buffer

```bash
<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>
```

### Enter normal mode and undo the last operation

```bash
<Esc><u>
```

### Search for a pattern in the file (press `<n>`/`<N>` to go to next/previous match)

```bash
</>search_pattern<Enter>
```

### Perform a `regex` substitution in the whole file

```bash
<:>%s/regex/replacement/g<Enter>
```

### Display the line numbers

```bash
<:>set nu<Enter>
```
