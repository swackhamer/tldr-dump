# csrutil

> Manage the System Integrity Protection configuration. More information: <https://keith.github.io/xcode-man-pages/csrutil.8.html>.

## Examples

### Display the System Integrity Protection status

```bash
csrutil status
```

### Disable the System Integrity Protection

```bash
csrutil disable
```

### Enable the System Integrity Protection

```bash
csrutil enable
```

### Display the list of allowed NetBoot sources

```bash
csrutil netboot list
```

### Add an IPv4 address to the list of allowed NetBoot sources

```bash
csrutil netboot add ip
```

### Reset the System Integrity Protection status and clear the NetBoot list

```bash
csrutil clear
```
