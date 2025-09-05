# hping3

> Advanced ping utility which supports protocols such TCP, UDP, and raw IP. Best run with elevated privileges. More information: <https://github.com/antirez/hping>.

## Examples

### Ping a destination with 4 ICMP ping requests

```bash
hping3 --icmp --count 4 ip_or_hostname
```

### Ping an IP address over UDP on port 80

```bash
hping3 --udp --destport 80 --syn ip_or_hostname
```

### Scan TCP port 80, scanning from the specific local source port 5090

```bash
hping3 --verbose --syn --destport 80 --baseport 5090 ip_or_hostname
```

### Traceroute using a TCP scan to a specific destination port

```bash
hping3 --traceroute --verbose --syn --destport 80 ip_or_hostname
```

### Scan a set of TCP ports on a specific IP address

```bash
hping3 --scan 80,3000,9000 --syn ip_or_hostname
```

### Perform a TCP ACK scan to check if a given host is alive

```bash
hping3 --count 2 --verbose --destport 80 --ack ip_or_hostname
```

### Perform a charge test on port 80

```bash
hping3 --flood --destport 80 --syn ip_or_hostname
```
