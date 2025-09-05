# httpflow

> A utility to capture and dump HTTP streams. More information: <https://github.com/six-ddc/httpflow>.

## Examples

### Capture traffic on all interfaces

```bash
httpflow -i any
```

### Use a bpf-style capture to filter the results

```bash
httpflow host httpbin.org or host baidu.com
```

### Use a `regex` to filter requests by URLs

```bash
httpflow -u 'regex'
```

### Read packets from PCAP format binary file

```bash
httpflow -r out.cap
```

### Write the output to a directory

```bash
httpflow -w path/to/directory
```
