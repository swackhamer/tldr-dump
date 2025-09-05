# watchexec

> Run arbitrary commands when files change. More information: <https://manned.org/watchexec>.

## Examples

### Call `ls -la` when any file in the current directory changes

```bash
watchexec ls -la
```

### Run `make` when any JavaScript, CSS and HTML file in the current directory changes

```bash
watchexec [-e|--exts] js,css,html make
```

### Run `make` when any file in the `lib` or `src` directory changes

```bash
watchexec [-w|--watch] lib [-w|--watch] src make
```

### Call/restart `my_server` when any file in the current directory changes, sending `SIGKILL` to stop the child process

```bash
watchexec [-r|--restart] --stop-signal SIGKILL my_server
```

### Restart the execution of a command when any Java source file in the current directory changes, sending `SIGKILL` and only checking for updates every `n`ms

```bash
watchexec [-r|--restart] --stop-signal SIGKILL --poll 10000 [-e|--exts] java command
```
