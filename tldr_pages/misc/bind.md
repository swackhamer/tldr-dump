# bind

> Bash builtin to manage bash hotkeys and variables. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-bind>.

## Examples

### List all bound commands and their hotkeys

```bash
bind -p|-P
```

### Query a command for its hotkey

```bash
bind -q command
```

### Bind a key

```bash
bind -x '"key_sequence":command'
```

### List user defined bindings

```bash
bind -X
```

### Display help

```bash
help bind
```
