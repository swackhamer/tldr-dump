# killall

> Send kill signal to all instances of a process by name (must be exact name). All signals except SIGKILL and SIGSTOP can be intercepted by the process, allowing a clean exit. More information: <https://manned.org/killall>.

## Examples

### Terminate a process using the default SIGTERM (terminate) signal

```bash
killall process_name
```

### List available signal names (to be used without the 'SIG' prefix)

```bash
killall [-l|--list]
```

### Interactively ask for confirmation before termination

```bash
killall [-i|--interactive] process_name
```

### Terminate a process using the SIGINT (interrupt) signal, which is the same signal sent by pressing `<Ctrl c>`

```bash
killall -INT process_name
```

### Force kill a process

```bash
killall -KILL process_name
```
