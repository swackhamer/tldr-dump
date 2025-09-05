# asnmap

> A Go CLI tool for mapping organization network ranges using ASN information. Note: An API key is required from ProjectDiscovery Cloud Platform for the tool to work. More information: <https://github.com/projectdiscovery/asnmap>.

## Examples

### Lookup CIDR ranges for an ASN

```bash
asnmap [-a|-asn] AS5650 -silent
```

### Lookup CIDR ranges for an IP address

```bash
asnmap [-i|-ip] 100.19.12.21 -silent
```

### Lookup CIDR ranges for a domain

```bash
asnmap [-d|-domain] example.com -silent
```

### Lookup CIDR ranges for an organization

```bash
asnmap -org GOOGLE -silent
```

### Lookup CIDR ranges from a file of targets

```bash
asnmap [-f|-file] targets.txt -silent
```

### Output results in JSON format

```bash
asnmap [-d|-domain] facebook.com [-j|-json] -silent
```

### Output results in CSV format

```bash
asnmap [-a|-asn] AS394161 [-c|-csv] -silent
```

### Update asnmap to the latest version

```bash
asnmap [-up|-update]
```
