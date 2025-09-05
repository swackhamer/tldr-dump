# opensnoop

> Track file opens on your system. More information: <https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

## Examples

### Print all file opens as they occur

```bash
sudo opensnoop
```

### Track all file opens by a process by name

```bash
sudo opensnoop -n "process_name"
```

### Track all file opens by a process by PID

```bash
sudo opensnoop -p PID
```

### Track which processes open a specified file

```bash
sudo opensnoop -f path/to/file
```
