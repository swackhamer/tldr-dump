# mtr

> Matt's Traceroute: combined traceroute and ping tool. More information: <https://manned.org/mtr>.

## Examples

### Traceroute to a host and continuously ping all intermediary hops

```bash
mtr example.com
```

### Disable IP address and host name mapping

```bash
mtr [-n|--no-dns] example.com
```

### Generate output after pinging each hop 10 times

```bash
mtr [-w|--report-wide] example.com
```

### Force IP IPv4 or IPV6

```bash
mtr -4 example.com
```

### Wait for a given time (in seconds) before sending another packet to the same hop

```bash
mtr [-i|--interval] 10 example.com
```

### Display the Autonomous System Number (ASN) for each hop

```bash
mtr [-z|--aslookup] example.com
```

### Display both IP address and reverse DNS name

```bash
mtr [-b|--show-ips] example.com
```
