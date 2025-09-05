# sniffer.py

> Capture and display network packets for specified protocols using raw sockets. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Capture packets for default protocols (ICMP, TCP, UDP)

```bash
sniffer.py
```

### Capture packets for specific protocols (e.g., ICMP, TCP)

```bash
sniffer.py protocol1 protocol2 ...
```

### Capture packets for specific protocols (e.g., TCP)

```bash
sniffer.py tcp
```
