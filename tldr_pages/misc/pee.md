# pee

> Tee `stdin` to pipes. See also: `tee`. More information: <https://manned.org/pee>.

## Examples

### Run each command, providing each one with a distinct copy of `stdin`

```bash
pee command1 command2 ...
```

### Write a copy of `stdin` to `stdout` (like `tee`)

```bash
pee cat command1 command2 ...
```

### Immediately terminate upon SIGPIPEs and write errors

```bash
pee --no-ignore-sigpipe --no-ignore-write-errors command1 command2 ...
```
