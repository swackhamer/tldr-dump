# procs

> Display information about the active processes. More information: <https://github.com/dalance/procs>.

## Examples

### List all processes showing the PID, user, CPU usage, memory usage, and the command which started them

```bash
procs
```

### List all processes as a tree

```bash
procs --tree
```

### List information about processes, if the commands which started them contain Zsh

```bash
procs zsh
```

### List information about all processes sorted by CPU time in [a]scending or [d]escending order

```bash
procs --sorta|--sortd cpu
```

### List information about processes with either a PID, command, or user containing `41` or `firefox`

```bash
procs --or PID|command|user 41 firefox
```

### List information about processes with both PID `41` and a command or user containing `zsh`

```bash
procs --and 41 zsh
```
