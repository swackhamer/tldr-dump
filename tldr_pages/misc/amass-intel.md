# amass-intel

> Collect open source intel on an organisation like root domains and ASNs. More information: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

## Examples

### Find root domains in an IP [addr]ess range

```bash
amass intel -addr 192.168.0.1-254
```

### Use active recon methods

```bash
amass intel -active -addr 192.168.0.1-254
```

### Find root domains related to a [d]omain

```bash
amass intel -whois -d domain_name
```

### Find ASNs belonging to an [org]anisation

```bash
amass intel -org organisation_name
```

### Find root domains belonging to a given Autonomous System Number

```bash
amass intel -asn asn
```

### Save results to a text file

```bash
amass intel -o output_file -whois -d domain_name
```

### List all available data sources

```bash
amass intel -list
```
