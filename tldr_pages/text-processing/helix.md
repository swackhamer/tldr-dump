# helix

> Helix, A post-modern text editor, provides several modes for different kinds of text manipulation. Pressing `<i>` enters insert mode. `<Esc>` enters normal mode, which enables the use of Helix commands. More information: <https://helix-editor.com>.

## Examples

### Open a file

```bash
helix path/to/file
```

### Open files and show them one next each other

```bash
helix --vsplit path/to/file1 path/to/file2
```

### Show the tutorial to learn Helix (or access it within Helix by pressing `<Esc>` and typing `<:>tutor<Enter>`)

```bash
helix --tutor
```

### Change the Helix theme

```bash
<:>theme theme_name
```

### Save and Quit

```bash
<:>wq<Enter>
```

### Force-quit without saving

```bash
<:>q!<Enter>
```

### Undo the last operation

```bash
<u>
```

### Search for a pattern in the file (press `<n>`/`<N>` to go to next/previous match)

```bash
</>search_pattern<Enter>
```
