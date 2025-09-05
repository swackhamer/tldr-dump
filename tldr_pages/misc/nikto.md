# nikto

> Web server scanner which performs tests against web servers for multiple items. More information: <https://cirt.net/Nikto2>.

## Examples

### Perform a basic Nikto scan against a target host

```bash
perl nikto.pl [-h|-host] 192.168.0.1
```

### Specify the port number when performing a basic scan

```bash
perl nikto.pl [-h|-host] 192.168.0.1 [-p|-port] 443
```

### Scan ports and protocols with full URL syntax

```bash
perl nikto.pl [-h|-host] https://192.168.0.1:443/
```

### Scan multiple ports in the same scanning session

```bash
perl nikto.pl [-h|-host] 192.168.0.1 [-p|-port] 80,88,443
```

### Update to the latest plugins and databases

```bash
perl nikto.pl [-u|-update]
```
