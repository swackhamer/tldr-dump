# top

> Display dynamic real-time information about running processes. More information: <https://keith.github.io/xcode-man-pages/top.1.html>.

## Examples

### Start `top`, all options are available in the interface

```bash
top
```

### Start `top` sorting processes by internal memory size (default order - process ID)

```bash
top -o mem
```

### Start `top` sorting processes first by CPU, then by running time

```bash
top -o cpu -O time
```

### Start `top` displaying only processes owned by given user

```bash
top -user user_name
```

### Display help about interactive commands

```bash
<?>
```
