# nbtscan

> Scan networks for NetBIOS name information. More information: <https://github.com/resurrecting-open-source-projects/nbtscan>.

## Examples

### Scan a network for NetBIOS names

```bash
nbtscan 192.168.0.1/24
```

### Scan a single IP address

```bash
nbtscan 192.168.0.1
```

### Display verbose output

```bash
nbtscan -v 192.168.0.1/24
```

### Display output in `/etc/hosts` format

```bash
nbtscan -e 192.168.0.1/24
```

### Read IP addresses/networks to scan from a file

```bash
nbtscan -f path/to/file.txt
```
