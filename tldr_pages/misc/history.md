# history

> Manage command-line history. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-history>.

## Examples

### Display the commands history list with line numbers

```bash
history
```

### Display the last 20 commands (in Zsh it displays all commands starting from the 20th)

```bash
history 20
```

### Display history with timestamps in different formats (only available in Zsh)

```bash
history -d|f|i|E
```

### [c]lear the commands history list (only for current Bash shell)

```bash
history -c
```

### Over[w]rite history file with history of current Bash shell (often combined with `history -c` to purge history)

```bash
history -w
```

### [d]elete the history entry at the specified offset

```bash
history -d offset
```

### Add a command to history without running it

```bash
history -s command
```
