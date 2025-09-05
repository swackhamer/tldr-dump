# sngrep

> Display SIP calls message flows from terminal. More information: <https://manned.org/sngrep>.

## Examples

### Visualize SIP packets from a PCAP file

```bash
sngrep -I path/to/file.pcap
```

### Visualize only dialogs starting with INVITE packets with RTP packets from a PCAP file

```bash
sngrep -crI path/to/file.pcap
```

### Real-time interface with only dialogs starting with INVITE packets with RTP packets

```bash
sngrep -cr
```

### Only capture packets without interface to a file

```bash
sngrep -NO path/to/file.pcap
```
