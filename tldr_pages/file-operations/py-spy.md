# py-spy

> A sampling profiler for Python programs. More information: <https://github.com/benfred/py-spy>.

## Examples

### Show a live view of the functions that take the most execution time of a running process

```bash
py-spy top [-p|--pid] pid
```

### Start a program and show a live view of the functions that take the most execution time

```bash
py-spy top -- python path/to/file.py
```

### Produce an SVG flame graph of the function call execution time

```bash
py-spy record [-o|--output] path/to/profile.svg [-p|--pid] pid
```

### Dump the call stack of a running process

```bash
py-spy dump [-p|--pid] pid
```
