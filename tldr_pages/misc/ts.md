# ts

> Add timestamps to every line from `stdin`. More information: <https://manned.org/ts>.

## Examples

### Add a timestamp to the beginning of each line

```bash
command | ts
```

### Add timestamps with microsecond precision

```bash
command | ts "%b %d %H:%M:%.S"
```

### Add [i]ncremental timestamps with microsecond precision, starting from zero

```bash
command | ts -i "%H:%M:%.S"
```

### Convert existing timestamps in a text file (eg. a log file) into [r]elative format

```bash
cat path/to/file | ts -r
```
