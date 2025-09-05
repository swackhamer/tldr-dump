# masscan

> A very fast network scanner. Works best with elevated privileges. For help with Nmap compatibility, run `masscan --nmap`. More information: <https://manned.org/masscan>.

## Examples

### Scan an IP or network subnet for port 80

```bash
masscan ip_address|network_prefix [-p|--ports] 80
```

### Scan a class B subnet for the top 100 ports at 100,000 packets per second

```bash
masscan 10.0.0.0/16 --top-ports 100 --rate 100000
```

### Scan a class B subnet avoiding ranges from a specific exclude file

```bash
masscan 10.0.0.0/16 --top-ports 100 --excludefile path/to/file
```

### Scan a class B subnet with Nmap-like version detection (banner grabbing)

```bash
masscan 10.0.0.0/16 [-p|--ports] 22,80 --banners --rate 100000
```

### Scan the Internet for web servers running on port 80 and 443

```bash
masscan 0.0.0.0/0 [-p|--ports] 80,443 --rate 10000000
```

### Scan the Internet for DNS servers running on UDP port 53

```bash
masscan 0.0.0.0/0 [-p|--ports] U:53 --rate 10000000
```

### Scan the Internet for a specific port range and export to a file

```bash
masscan 0.0.0.0/0 [-p|--ports] 0-65535 --output-format binary|grepable|json|list|xml --output-filename path/to/file
```

### Read binary scan results from a file and output to `stdout`

```bash
masscan --readscan path/to/file
```
