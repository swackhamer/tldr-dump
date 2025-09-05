# chronic

> Display `stdout` and `stderr` of a command if and only if it fails. More information: <https://manned.org/chronic>.

## Examples

### Display `stdout` and `stderr` of the specified command if and only if it produces a non-zero exit code or crashes

```bash
chronic command option1 option2 ...
```

### Display `stdout` and `stderr` of the specified command if and only if it produces a non-empty `stderr`

```bash
chronic -e command option1 option2 ...
```

### Enable [v]erbose mode

```bash
chronic -v command option1 option2 ...
```
