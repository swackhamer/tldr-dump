# httpry

> A lightweight packet sniffer for displaying and logging HTTP traffic. It can be run in real-time displaying the traffic as it is parsed, or as a daemon process that logs to an output file. More information: <https://dumpsterventures.com/jason/httpry/>.

## Examples

### Save output to a file

```bash
httpry -o path/to/file.log
```

### Listen on a specific interface and save output to a binary PCAP format file

```bash
httpry eth0 -b path/to/file.pcap
```

### Filter output by a comma-separated list of HTTP verbs

```bash
httpry -m get|post|put|head|options|delete|trace|connect|patch
```

### Read from an input capture file and filter by IP

```bash
httpry -r path/to/file.log 'host 192.168.5.25'
```

### Run as daemon process

```bash
httpry -d -o path/to/file.log
```
