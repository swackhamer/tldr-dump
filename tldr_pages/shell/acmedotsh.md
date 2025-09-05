# acme.sh

> Shell script implementing ACME client protocol, an alternative to `certbot`. See also: `acme.sh dns`. More information: <https://github.com/acmesh-official/acme.sh>.

## Examples

### Issue a certificate using webroot mode

```bash
acme.sh --issue [-d|--domain] example.com [-w|--webroot] /path/to/webroot
```

### Issue a certificate for multiple domains using standalone mode using port 80

```bash
acme.sh --issue --standalone [-d|--domain] example.com [-d|--domain] www.example.com
```

### Issue a certificate using standalone TLS mode using port 443

```bash
acme.sh --issue --alpn [-d|--domain] example.com
```

### Issue a certificate using a working Nginx configuration

```bash
acme.sh --issue --nginx [-d|--domain] example.com
```

### Issue a certificate using a working Apache configuration

```bash
acme.sh --issue --apache [-d|--domain] example.com
```

### Issue a wildcard (\*) certificate using an automatic DNS API mode

```bash
acme.sh --issue --dns dns_cf [-d|--domain] *.example.com
```

### Install certificate files into the specified locations (useful for automatic certificate renewal)

```bash
acme.sh [-i|--install-cert] [-d|--domain] example.com --key-file /path/to/example.com.key --fullchain-file /path/to/example.com.cer --reloadcmd "systemctl force-reload nginx"
```
