# dog

> DNS lookup utility. It has colorful output, supports DNS-over-TLS and DNS-over-HTTPS protocols, and can emit JSON. More information: <https://github.com/ogham/dog#examples>.

## Examples

### Lookup the IP(s) associated with a hostname (A records)

```bash
dog example.com
```

### Query the MX records type associated with a given domain name

```bash
dog example.com MX
```

### Specify a specific DNS server to query (e.g. Cloudflare)

```bash
dog example.com MX @1.1.1.1
```

### Query over TCP rather than UDP

```bash
dog example.com MX @1.1.1.1 [-T|--tcp]
```

### Query the MX records type associated with a given domain name over TCP using explicit arguments

```bash
dog [-q|--query] example.com [-t|--type] MX [-n|--nameserver] 1.1.1.1 [-T|--tcp]
```

### Lookup the IP(s) associated with a hostname (A records) using DNS over HTTPS (DoH)

```bash
dog example.com [-H|--https] @https://cloudflare-dns.com/dns-query
```
