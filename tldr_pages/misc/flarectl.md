# flarectl

> Official CLI for Cloudflare. More information: <https://github.com/cloudflare/cloudflare-go/blob/master/cmd/flarectl/README.md>.

## Examples

### Block a specific IP

```bash
flarectl firewall rules create --zone="example.com" --value="8.8.8.8" --mode="block" --notes="Block bad actor"
```

### Add a DNS record

```bash
flarectl dns create --zone="example.com" --name="app" --type="CNAME" --content="myapp.herokuapp.com" --proxy
```

### List all Cloudflare IPv4/IPv6 ranges

```bash
flarectl ips --ip-type ipv4|ipv6|all
```

### Create many new Cloudflare zones automatically with names from `domains.txt`

```bash
for domain in $(cat domains.txt); do flarectl zone info --zone=$domain; done
```

### List all firewall rules

```bash
flarectl firewall rules list
```
