# sniff.py

> Capture and display network packets using the `pcapy` library. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### List available network interfaces and select one to start capturing packets (requires `sudo`)

```bash
sudo sniff.py
```

### Capture packets and save output to a file while displaying it on the terminal

```bash
sudo sniff.py | sudo tee path/to/output_file
```
