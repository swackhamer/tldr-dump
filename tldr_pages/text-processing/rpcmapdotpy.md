# rpcmap.py

> Lookup listening MSRPC interfaces using a string binding (e.g., `ncacn_ip_tcp:host[port]`). Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Connect to an MSRPC interface using a string binding (e.g., `ncacn_ip_tcp:host[port]`)

```bash
rpcmap.py stringbinding
```

### Bruteforce UUIDs even if the MGMT interface is available

```bash
rpcmap.py -brute-uuids stringbinding
```

### Bruteforce operation numbers (opnums) for discovered UUIDs

```bash
rpcmap.py -brute-opnums stringbinding
```

### Bruteforce major versions of found UUIDs

```bash
rpcmap.py -brute-versions stringbinding
```

### Specify a target IP address manually

```bash
rpcmap.py -target-ip ip_address stringbinding
```

### Authenticate to the RPC interface with username and password

```bash
rpcmap.py -auth-rpc domain/username:password stringbinding
```

### Authenticate using NTLM hashes for RPC

```bash
rpcmap.py -hashes-rpc LMHASH:NTHASH stringbinding
```

### Enable debug output for verbose information

```bash
rpcmap.py -debug stringbinding
```
