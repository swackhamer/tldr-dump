# bindkey

> Add keybindings to Z-Shell. More information: <https://zsh.sourceforge.io/Guide/zshguide04.html>.

## Examples

### Bind a hotkey to a specific command

```bash
bindkey "^k" kill-line
```

### Bind a hotkey to a specific key [s]equence

```bash
bindkey -s '^o' 'cd ..\n'
```

### [l]ist keymaps

```bash
bindkey -l
```

### View the hotkey in a key[M]ap

```bash
bindkey -M main
```
