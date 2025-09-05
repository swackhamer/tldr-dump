# ipaggcreate

> Produce aggregate statistics of TCP/IP dumps. More information: <https://manned.org/ipaggcreate>.

## Examples

### Count the number of packets sent from each source address appearing in a PCAP file

```bash
ipaggcreate --src path/to/file.pcap
```

### Group and count packets read from a network interface by IP packet length

```bash
ipaggcreate --interface eth0 --length
```

### Count the number of bytes sent between each address pair appearing in a PCAP file

```bash
ipaggcreate --address-pairs --bytes path/to/file.pcap
```
