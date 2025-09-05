# ipcalc

> Calculate IP information (subnet, broadcast, host range) from an IP address and netmask. More information: <https://manned.org/ipcalc>.

## Examples

### Display network info for an IP address

```bash
ipcalc 192.168.0.1
```

### Display network info using CIDR notation

```bash
ipcalc 192.168.0.1/24
```

### Display network info using a dotted decimal netmask

```bash
ipcalc 192.168.0.1 255.255.255.0
```

### Suppress bitwise output

```bash
ipcalc [-b|--nobinary] 192.168.0.1
```

### Split a network into specified sized blocks

```bash
ipcalc [-s|--split] size1 size2 size3 ... 192.168.0.1
```

### Display version

```bash
ipcalc [-v|--version]
```
