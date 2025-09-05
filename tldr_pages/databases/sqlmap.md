# sqlmap

> Detect and exploit SQL injection flaws. More information: <https://sqlmap.org>.

## Examples

### Run sqlmap against a single target URL

```bash
python sqlmap.py [-u|--url] "http://www.example.com/vuln.php?id=1"
```

### Send data in a POST request (`--data` implies POST request)

```bash
python sqlmap.py [-u|--url] "http://www.example.com/vuln.php" --data="id=1"
```

### Change the parameter delimiter (& is the default)

```bash
python sqlmap.py [-u|--url] "http://www.example.com/vuln.php" --data="query=foobar;id=1" --param-del=";"
```

### Select a random `User-Agent` from `./txt/user-agents.txt` and use it

```bash
python sqlmap.py [-u|--url] "http://www.example.com/vuln.php" --random-agent
```

### Provide user credentials for HTTP protocol authentication

```bash
python sqlmap.py [-u|--url] "http://www.example.com/vuln.php" --auth-type Basic --auth-cred "testuser:testpass"
```
