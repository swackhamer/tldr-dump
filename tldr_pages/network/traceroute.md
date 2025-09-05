# traceroute

> Print the route packets trace to network host. More information: <https://manned.org/traceroute>.

## Examples

### Traceroute to a host

```bash
traceroute example.com
```

### Disable IP address and host name mapping

```bash
traceroute -n example.com
```

### Specify wait time in seconds for response

```bash
traceroute [-w|--wait] 0.5 example.com
```

### Specify number of queries per hop

```bash
traceroute [-q|--queries] 5 example.com
```

### Specify size in bytes of probing packet

```bash
traceroute example.com 42
```

### Determine the MTU to the destination

```bash
traceroute --mtu example.com
```

### Use ICMP instead of UDP for tracerouting

```bash
traceroute [-I|--icmp] example.com
```
