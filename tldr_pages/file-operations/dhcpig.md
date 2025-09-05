# dhcpig

> Initiates an advanced DHCP exhaustion attack and stress test. DHCPig needs to be run with root privileges. More information: <https://github.com/kamorin/DHCPig>.

## Examples

### Exhaust all of the available DHCP addresses using the specified interface

```bash
sudo ./pig.py eth0
```

### Exhaust IPv6 addresses using eth1 interface

```bash
sudo ./pig.py [-6|--ipv6] eth1
```

### Send fuzzed/malformed data packets using the interface

```bash
sudo ./pig.py [-f|--fuzz] eth1
```

### Enable color output

```bash
sudo ./pig.py [-c|--color] eth1
```

### Enable minimal verbosity and color output

```bash
sudo ./pig.py [-c|--color] [-v|--verbosity] 1 eth1
```

### Use a debug verbosity of 100 and scan network of neighboring devices using ARP packets

```bash
sudo ./pig.py [-c|--color] [-v|--verbosity] 100 [-n|--neighbors-scan-arp] eth1
```

### Enable printing lease information, attempt to scan and release all neighbor IP addresses

```bash
sudo ./pig.py [-n|--neighbors-scan-arp] [-r|--neighbors-attack-release] [-o|--show-options] eth1
```
