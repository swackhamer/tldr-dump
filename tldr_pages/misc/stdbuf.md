# stdbuf

> Run a command with modified buffering operations for its standard streams. More information: <https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>.

## Examples

### Change `stdin` buffer size to 512 KiB

```bash
stdbuf [-i|--input] 512K command
```

### Change `stdout` buffer to line-buffered

```bash
stdbuf [-o|--output] L command
```

### Change `stderr` buffer to unbuffered

```bash
stdbuf [-e|--error] 0 command
```
