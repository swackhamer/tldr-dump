# tcpreplay

> Replay network traffic stored in a `pcap` file. More information: <https://tcpreplay.appneta.com/wiki/tcpreplay-man.html>.

## Examples

### List available network interfaces

```bash
tcpreplay --listnics
```

### Replay traffic to interface

```bash
tcpreplay [-i|--intf1] eth0 traffic.pcap
```

### Replay traffic to interface and `stdout`

```bash
tcpreplay [-i|--intf1] eth0 [-v|--verbose] traffic.pcap
```

### Replay traffic to interface as fast as possible

```bash
tcpreplay [-i|--intf1] eth0 [-t|--topspeed] traffic.pcap
```

### Replay traffic to interface at given Mbps

```bash
tcpreplay [-i|--intf1] eth0 [-M|--mbps] 10 traffic.pcap
```

### Replay traffic to interface several times

```bash
tcpreplay [-i|--intf1] eth0 [-l|--loop] num_times traffic.pcap
```
