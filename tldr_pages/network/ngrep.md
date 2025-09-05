# ngrep

> Filter network traffic packets using `regex`. More information: <https://github.com/jpr5/ngrep/blob/master/EXAMPLES.md>.

## Examples

### Capture traffic of all interfaces

```bash
ngrep -d any
```

### Capture traffic of a specific interface

```bash
ngrep -d eth0
```

### Capture traffic crossing port 22 of interface eth0

```bash
ngrep -d eth0 port 22
```

### Capture traffic from or to a host

```bash
ngrep host www.example.com
```

### Filter keyword 'User-Agent:' of interface eth0

```bash
ngrep -d eth0 'User-Agent:'
```
