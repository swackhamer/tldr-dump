# mkfifo

> Make FIFOs (named pipes). More information: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

## Examples

### Create a named pipe at a given path

```bash
mkfifo path/to/pipe
```

### Send data through a named pipe and send the command to the background

```bash
echo "Hello World" > path/to/pipe &
```

### Receive data through a named pipe

```bash
cat path/to/pipe
```

### Share your terminal session in real-time

```bash
mkfifo path/to/pipe; script [-f|--flush] path/to/pipe
```
