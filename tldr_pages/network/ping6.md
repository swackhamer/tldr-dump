# ping6

> Send ICMP ECHO_REQUEST packets to network hosts via IPv6 address. More information: <https://manned.org/ping6>.

## Examples

### Ping a host

```bash
ping6 host
```

### Ping a host only a specific number of times

```bash
ping6 -c count host
```

### Ping a host, specifying the interval in seconds between requests (default is 1 second)

```bash
ping6 -i seconds host
```

### Ping a host without trying to lookup symbolic names for addresses

```bash
ping6 -n host
```

### Ping a host and ring the bell when a packet is received (if your terminal supports it)

```bash
ping6 -a host
```
