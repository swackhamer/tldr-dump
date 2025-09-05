# wpscan

> WordPress vulnerability scanner. More information: <https://github.com/wpscanteam/wpscan>.

## Examples

### Update the vulnerability database

```bash
wpscan --update
```

### Scan a WordPress website

```bash
wpscan --url url
```

### Scan a WordPress website, using random user agents and passive detection

```bash
wpscan --url url --stealthy
```

### Scan a WordPress website, checking for vulnerable plugins and specifying the path to the `wp-content` directory

```bash
wpscan --url url --enumerate vp --wp-content-dir remote/path/to/wp-content
```

### Scan a WordPress website through a proxy

```bash
wpscan --url url --proxy protocol://ip:port --proxy-auth username:password
```

### Perform user identifiers enumeration on a WordPress website

```bash
wpscan --url url --enumerate u
```

### Execute a password guessing attack on a WordPress website

```bash
wpscan --url url --usernames username|path/to/usernames.txt --passwords path/to/passwords.txt threads 20
```

### Scan a WordPress website, collecting vulnerability data from the WPVulnDB (<https://wpvulndb.com/>)

```bash
wpscan --url url --api-token token
```
