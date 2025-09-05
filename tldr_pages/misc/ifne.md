# ifne

> Run a command depending on the emptyness of `stdin`. More information: <https://manned.org/ifne>.

## Examples

### Run the specified command if and only if `stdin` is not empty

```bash
ifne command options ...
```

### Run the specified command if and only if `stdin` is empty, otherwise pass `stdin` to `stdout`

```bash
ifne -n command options ...
```
