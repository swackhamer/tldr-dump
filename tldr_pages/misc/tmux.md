# tmux

> Terminal multiplexer. It allows multiple sessions with windows, panes, and more. See also: `zellij`, `screen`. More information: <https://github.com/tmux/tmux>.

## Examples

### Start a new session

```bash
tmux
```

### Start a new named [s]ession

```bash
tmux [new|new-session] -s name
```

### List existing sessions

```bash
tmux [ls|list-sessions]
```

### Attach to the most recently used session

```bash
tmux [a|attach]
```

### Detach from the current session (inside a tmux session)

```bash
<Ctrl b><d>
```

### Create a new window (inside a tmux session)

```bash
<Ctrl b><c>
```

### Switch between sessions and windows (inside a tmux session)

```bash
<Ctrl b><w>
```

### Kill a session by [t]arget name

```bash
tmux kill-session -t name
```
