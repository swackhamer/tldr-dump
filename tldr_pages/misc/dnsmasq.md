# dnsmasq

> Lightweight DNS, DHCP, TFTP, and PXE server. More information: <https://manned.org/dnsmasq>.

## Examples

### Start dnsmasq with default configuration

```bash
dnsmasq
```

### Run dnsmasq in the foreground (for debugging)

```bash
dnsmasq --no-daemon
```

### Specify a custom configuration file

```bash
dnsmasq --conf-file=path/to/config.conf
```

### Enable verbose logging

```bash
dnsmasq --log-queries --log-facility=-
```

### Set a DHCP range and lease time

```bash
dnsmasq --dhcp-range=192.168.0.50,192.168.0.150,12h
```

### Print dnsmasq version

```bash
dnsmasq --version
```
