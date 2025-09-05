# drill

> Perform various DNS queries. More information: <https://manned.org/drill>.

## Examples

### Lookup the IP(s) associated with a hostname (A records)

```bash
drill example.com
```

### Lookup the mail server(s) associated with a given domain name (MX record)

```bash
drill mx example.com
```

### Get all types of records for a given domain name

```bash
drill any example.com
```

### Specify an alternate DNS server to query

```bash
drill example.com @8.8.8.8
```

### Perform a reverse DNS lookup on an IP address (PTR record)

```bash
drill -x 8.8.8.8
```

### Perform DNSSEC trace from root servers down to a domain name

```bash
drill -TD example.com
```

### Show DNSKEY record(s) for a domain name

```bash
drill -s dnskey example.com
```
