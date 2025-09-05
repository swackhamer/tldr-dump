# rpcdump.py

> Dump remote RPC endpoints information via the Endpoint Mapper. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Dump RPC endpoints using username and password

```bash
rpcdump.py domain/username:password@target
```

### Dump RPC endpoints using NTLM hashes

```bash
rpcdump.py -hashes LMHASH:NTHASH domain/username:password@target
```

### Specify a target IP address explicitly (useful if the target name is a NetBIOS name)

```bash
rpcdump.py -target-ip target_ip domain/username:password@target
```

### Connect to a specific port (default is 135 for RPC Endpoint Mapper)

```bash
rpcdump.py -port port_number domain/username:password@target
```

### Enable debug output

```bash
rpcdump.py -debug domain/username:password@target
```
