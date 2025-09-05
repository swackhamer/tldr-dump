# nettop

> Display updated information about the network. More information: <https://keith.github.io/xcode-man-pages/nettop.1.html>.

## Examples

### Monitor TCP and UDP sockets from all interfaces

```bash
nettop
```

### Monitor TCP sockets from Loopback interfaces

```bash
nettop -m tcp -t loopback
```

### Monitor a specific process

```bash
nettop -p "process_id|process_name"
```

### Display a per-process summary

```bash
nettop -P
```

### Print 10 samples of network information

```bash
nettop -l 10
```

### Monitor changes every 5 seconds

```bash
nettop -d -s 5
```

### While running nettop, list interactive commands

```bash
<h>
```

### Display help

```bash
nettop -h
```
