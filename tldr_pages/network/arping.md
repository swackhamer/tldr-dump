# arping

> Discover and probe hosts in a network using the ARP protocol. Useful for MAC address discovery. More information: <https://manned.org/arping>.

## Examples

### Ping a host by ARP request packets

```bash
arping host_ip
```

### Ping a host on a specific interface

```bash
arping -I interface host_ip
```

### Ping a host and [f]inish after the first reply

```bash
arping -f host_ip
```

### Ping a host a specific number ([c]ount) of times

```bash
arping -c count host_ip
```

### Broadcast ARP request packets to update neighbours' ARP caches ([U]nsolicited ARP mode)

```bash
arping -U ip_to_broadcast
```

### [D]etect duplicated IP addresses in the network by sending ARP requests with a 3 second timeout

```bash
arping -D -w 3 ip_to_check
```
