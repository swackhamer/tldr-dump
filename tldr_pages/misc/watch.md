# watch

> Execute a program periodically and monitor the output in full-screen mode. More information: <https://manned.org/watch>.

## Examples

### Repeatedly run a command and show the result

```bash
watch command
```

### Re-run a command every 60 seconds

```bash
watch [-n|--interval] 60 command
```

### Monitor disk space, highlighting differences as they appear

```bash
watch [-d|--differences] df
```

### Repeatedly run a pipeline and show the result

```bash
watch "command_1 | command_2 | command_3"
```

### Exit `watch` if the visible output changes

```bash
watch [-g|--chgexit] lsblk
```

### Interpret terminal control characters

```bash
watch [-c|--color] ls --color=always
```
