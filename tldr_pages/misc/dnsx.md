# dnsx

> A fast and multi-purpose DNS toolkit to run multiple DNS queries. Note: Input to `dnsx` needs to be passed through `stdin` (pipe `|`) in some cases. See also: `dig`, `dog`, `dnstracer`. More information: <https://docs.projectdiscovery.io/tools/dnsx/running>.

## Examples

### Query the A record of a (sub)domain and show [re]sponse received

```bash
echo example.com | dnsx -a [-re|-resp]
```

### Query all the DNS records (A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR, CAA)

```bash
dnsx -recon [-re|-resp] <<< example.com
```

### Query a specific type of DNS record

```bash
echo example.com | dnsx [-re|-resp] -a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa
```

### Output response only (do not show the queried domain or subdomain)

```bash
echo example.com | dnsx [-ro|-resp-only]
```

### Display raw response of a query, specifying resolvers to use and retry attempts for failures

```bash
echo example.com | dnsx -debug|raw [-r|-resolver] 1.1.1.1,8.8.8.8,... -retry number
```

### Brute force DNS records using a placeholder

```bash
dnsx [-d|-domain] FUZZ.example.com [-w|-wordlist] path/to/wordlist.txt [-re|-resp]
```

### Brute force DNS records from a list of domains and wordlists, appending output to a file with no color codes

```bash
dnsx [-d|-domain] path/to/domain.txt [-w|-wordlist] path/to/wordlist.txt [-re|-resp] [-o|-output] path/to/output.txt [-nc|-no-color]
```

### Extract `CNAME` records for the given list of subdomains, with rate limiting DNS queries per second

```bash
subfinder -silent [-d|-domain] example.com | dnsx -cname [-re|-resp] [-rl|-rate-limit] number
```
