# screen

> Hold a session open on a remote server. Manage multiple windows with a single SSH connection. See also: `tmux`, `zellij`. More information: <https://manned.org/screen>.

## Examples

### Start a new screen session

```bash
screen
```

### Start a new named screen session

```bash
screen -S session_name
```

### Start a new daemon and log the output to `screenlog.x`

```bash
screen -dmLS session_name command
```

### Show open screen sessions

```bash
screen -ls
```

### Reattach to an open screen

```bash
screen -r session_name
```

### Detach from inside a screen

```bash
<Ctrl a><d>
```

### Kill the current screen session

```bash
<Ctrl a><k>
```

### Kill a detached screen

```bash
screen -X -S session_name quit
```
