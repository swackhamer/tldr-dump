# openconnect

> A VPN client, for Cisco AnyConnect VPNs and others. More information: <https://www.infradead.org/openconnect/manual.html>.

## Examples

### Connect to a server

```bash
openconnect vpn.example.org
```

### Connect to a server, forking into the background

```bash
openconnect --background vpn.example.org
```

### Terminate the connection that is running in the background

```bash
killall -SIGINT openconnect
```

### Connect to a server, reading options from a configuration file

```bash
openconnect --config=path/to/file vpn.example.org
```

### Connect to a server and authenticate with a specific SSL client certificate

```bash
openconnect --certificate=path/to/file vpn.example.org
```
