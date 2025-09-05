# gobuster

> Brute-forces hidden paths on web servers and more. More information: <https://github.com/OJ/gobuster#modes>.

## Examples

### Discover directories and files that match in the wordlist

```bash
gobuster dir [-u|--url] https://example.com/ [-w|--wordlist] path/to/file
```

### Discover subdomains

```bash
gobuster dns [-d|--domain] example.com [-w|--wordlist] path/to/file
```

### Discover Amazon S3 buckets

```bash
gobuster s3 [-w|--wordlist] path/to/file
```

### Discover other virtual hosts on the server

```bash
gobuster vhost [-u|--url] https://example.com/ [-w|--wordlist] path/to/file
```

### Fuzz the value of a parameter

```bash
gobuster fuzz [-u|--url] https://example.com/?parameter=FUZZ [-w|--wordlist] path/to/file
```

### Fuzz the name of a parameter

```bash
gobuster fuzz [-u|--url] https://example.com/?FUZZ=value [-w|--wordlist] path/to/file
```
