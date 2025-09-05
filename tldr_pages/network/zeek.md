# zeek

> Passive network traffic analyzer. Any output and log files will be saved to the current working directory. More information: <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

## Examples

### Analyze live traffic from a network interface

```bash
sudo zeek --iface interface
```

### Analyze live traffic from a network interface and load custom scripts

```bash
sudo zeek --iface interface script1 script2 ...
```

### Analyze live traffic from a network interface, without loading any scripts

```bash
sudo zeek --bare-mode --iface interface
```

### Analyze live traffic from a network interface, applying a `tcpdump` filter

```bash
sudo zeek --filter path/to/filter --iface interface
```

### Analyze live traffic from a network interface using a watchdog timer

```bash
sudo zeek --watchdog --iface interface
```

### Analyze traffic from a PCAP file

```bash
zeek --readfile path/to/file.trace
```
