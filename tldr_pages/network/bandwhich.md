# bandwhich

> Display the current network utilization by process, connection or remote IP/hostname. More information: <https://github.com/imsnif/bandwhich#usage>.

## Examples

### Show the remote addresses table only

```bash
bandwhich [-a|--addresses]
```

### Show DNS queries

```bash
bandwhich [-s|--show-dns]
```

### Show total (cumulative) usage

```bash
bandwhich [-t|--total-utilization]
```

### Show the network utilization for a specific network interface

```bash
bandwhich [-i|--interface] eth0
```

### Show DNS queries with a given DNS server

```bash
bandwhich [-s|--show-dns] [-d|--dns-server] dns_server_ip
```
