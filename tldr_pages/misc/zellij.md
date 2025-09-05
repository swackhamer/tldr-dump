# zellij

> Terminal multiplexer with batteries included. See also: `tmux`, `screen`. More information: <https://zellij.dev/documentation/>.

## Examples

### Start a new named session

```bash
zellij [-s|--session] name
```

### List existing sessions

```bash
zellij [ls|list-sessions]
```

### Attach to the most recently used session

```bash
zellij [a|attach]
```

### Open a new pane (inside a zellij session)

```bash
<Alt n>
```

### Detach from the current session (inside a zellij session)

```bash
<Ctrl o><d>
```
