# iotop

> Display a table of current I/O usage by processes or threads. More information: <https://manned.org/iotop>.

## Examples

### Start top-like I/O monitor

```bash
sudo iotop
```

### Show only processes or threads actually doing I/O

```bash
sudo iotop [-o|--only]
```

### Show I/O usage in non-interactive mode

```bash
sudo iotop [-b|--batch]
```

### Show only I/O usage of processes (default is to show all threads)

```bash
sudo iotop [-P|--processes]
```

### Show I/O usage of given PID(s)

```bash
sudo iotop [-p|--pid] PID
```

### Show I/O usage of a given user

```bash
sudo iotop [-u|--user] user
```

### Show accumulated I/O instead of bandwidth

```bash
sudo iotop [-a|--accumulated]
```
