# netstat

> Display network-related information such as open connections, open socket ports, etc. See also: `lsof` for listing network connections, including listening ports. More information: <https://keith.github.io/xcode-man-pages/netstat.1.html>.

## Examples

### Display the PID and program name listening on a specific protocol

```bash
netstat -p protocol
```

### Print the routing table and do not resolve IP addresses to hostnames

```bash
netstat -nr
```

### Print the routing table of IPv4 addresses

```bash
netstat -nr -f inet
```
