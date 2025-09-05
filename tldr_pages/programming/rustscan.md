# rustscan

> Modern Port Scanner written in Rust. Note: `nmap` must be installed for some of the examples below to work. More information: <https://github.com/bee-san/RustScan/wiki>.

## Examples

### Scan all ports of one or more comma-delimited addresses using the default values

```bash
rustscan [-a|--addresses] ip_or_hostname
```

### Scan the top 1000 ports with service and version detection

```bash
rustscan --top [-a|--addresses] address_or_addresses
```

### Scan a specific list of ports

```bash
rustscan [-p|--ports] port1,port2,... [-a|--addresses] address_or_addresses
```

### Scan a specific range of ports

```bash
rustscan [-r|--range] start-end [-a|--addresses] address_or_addresses
```

### Invoke `nmap` functionalities (Nmap's OS detection and default scripts)

```bash
rustscan [-a|--addresses] address_or_addresses -- -O [-sC|--script=default]
```

### Scan with custom batch size (default: 4500) and timeout (default: 1500ms)

```bash
rustscan [-b|--batch-size] batch_size [-t|--timeout] timeout [-a|--addresses] address_or_addresses
```

### Scan with specific port order

```bash
rustscan --scan-order serial|random [-a|--addresses] address_or_addresses
```

### Scan in greppable mode (only output of the ports, no `nmap`)

```bash
rustscan [-g|--greppable] [-a|--addresses] address_or_addresses
```
