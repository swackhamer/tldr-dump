# ping

> Send ICMP ECHO_REQUEST packets to network hosts. More information: <https://keith.github.io/xcode-man-pages/ping.8.html>.

## Examples

### Ping the specified host

```bash
ping "hostname"
```

### Ping a host a specific number of times

```bash
ping -c count "host"
```

### Ping a host, specifying the interval in seconds between requests (default is 1 second)

```bash
ping -i seconds "host"
```

### Ping a host without trying to lookup symbolic names for addresses

```bash
ping -n "host"
```

### Ping a host and ring the bell when a packet is received (if your terminal supports it)

```bash
ping -a "host"
```

### Ping a host and prints the time a packet was received (this option is an Apple addition)

```bash
ping --apple-time "host"
```
