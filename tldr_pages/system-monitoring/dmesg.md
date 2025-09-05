# dmesg

> Write the kernel messages to `stdout`. More information: <https://keith.github.io/xcode-man-pages/dmesg.8.html>.

## Examples

### Show kernel messages

```bash
dmesg
```

### Show how much physical memory is available on this system

```bash
dmesg | grep -i memory
```

### Show kernel messages 1 page at a time

```bash
dmesg | less
```
