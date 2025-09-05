# cidr

> Simplifies IPv4/IPv6 CIDR network prefix management with counting, overlap checking, explanation, and subdivision. More information: <https://github.com/bschaatsbergen/cidr>.

## Examples

### Explain a CIDR range

```bash
cidr explain 10.0.0.0/16
```

### Check whether an address belongs to a CIDR range

```bash
cidr contains 10.0.0.0/16 10.0.14.5
```

### Get a count of all addresses in a CIDR range

```bash
cidr count 10.0.0.0/16
```

### Check whether two CIDR ranges overlap

```bash
cidr overlaps 10.0.0.0/16 10.0.14.0/22
```

### Divide a CIDR range into a specific number of networks

```bash
cidr divide 10.0.0.0/16 9
```
