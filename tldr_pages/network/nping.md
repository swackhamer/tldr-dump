# nping

> Network packet generation tool/ping utility. More information: <https://nmap.org/nping/>.

## Examples

### Ping a specified host using ICMP if the user is allowed to, otherwise using TCP

```bash
nping example.com
```

### Ping a specified host using ICMP assuming that the user is allowed to do so

```bash
nping --icmp --privileged example.com
```

### Ping a specified host using UDP

```bash
nping --udp example.com
```

### Ping a specified host on a given port using TCP

```bash
nping --tcp --dest-port 443 example.com
```

### Ping a certain number of times

```bash
nping --count 10 example.com
```

### Wait a certain amount of time between each ping

```bash
nping --delay 5s example.com
```

### Send the request over a specified interface

```bash
nping --interface eth0 example.com
```

### Ping an IP range

```bash
nping 10.0.0.1-10
```
