# knotc

> Control knot DNS server. More information: <https://www.knot-dns.cz/docs/latest/html/man_knotc.html>.

## Examples

### Start editing a zone

```bash
knotc zone-begin zone
```

### Set an A record with TTL of 3600

```bash
knotc zone-set zone subdomain 3600 A ip_address
```

### Finish editing the zone

```bash
knotc zone-commit zone
```

### Get the current zone data

```bash
knotc zone-read zone
```

### Get the current server configuration

```bash
knotc conf-read server
```
