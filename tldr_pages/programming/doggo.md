# doggo

> DNS client for Humans. Written in Golang. More information: <https://github.com/mr-karan/doggo/blob/main/docs/src/content/docs/guide/reference.md>.

## Examples

### Perform a simple DNS lookup

```bash
doggo example.com
```

### Query MX records using a specific nameserver

```bash
doggo MX codeberg.org @1.1.1.2
```

### Use DNS over HTTPS

```bash
doggo example.com @https://dns.quad9.net/dns-query
```

### Output in the JSON format

```bash
doggo example.com [-J|--json] | jq '.responses[0].answers[].address'
```

### Perform a reverse DNS lookup

```bash
doggo [-x|--reverse] 8.8.4.4 --short
```
