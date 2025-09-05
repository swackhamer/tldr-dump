# tcpdump

> Dump traffic on a network. More information: <https://www.tcpdump.org>.

## Examples

### List available network interfaces

```bash
tcpdump [-D|--list-interfaces]
```

### Capture the traffic of a specific interface

```bash
sudo tcpdump [-i|--interface] eth0
```

### Capture all TCP traffic showing contents ([A]SCII) in console

```bash
sudo tcpdump -A tcp
```

### Capture the traffic from or to a host

```bash
sudo tcpdump host www.example.com
```

### Capture the traffic from a specific interface, source, destination and destination port

```bash
sudo tcpdump [-i|--interface] eth0 src 192.168.1.1 and dst 192.168.1.2 and dst port 80
```

### Capture the traffic of a network

```bash
sudo tcpdump net 192.168.1.0/24
```

### Capture all traffic except traffic over port 22 and [w]rite to a dump file

```bash
sudo tcpdump -w dumpfile.pcap port not 22
```

### [r]ead from a given dump file

```bash
tcpdump -r dumpfile.pcap
```
