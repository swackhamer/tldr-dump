# host

> Lookup Domain Name Server. More information: <https://manned.org/host>.

## Examples

### Lookup A, AAAA, and MX records of a domain

```bash
host domain
```

### Lookup a field (CNAME, TXT, ...) of a domain

```bash
host -t field domain
```

### Reverse lookup an IP

```bash
host ip_address
```

### Specify an alternate DNS server to query

```bash
host domain 8.8.8.8
```
