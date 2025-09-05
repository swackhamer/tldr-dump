# ndc

> Name daemon control service for name servers. If a command isn't provided, NDC will prompt for one until EOF. More information: <https://manned.org/ndc>.

## Examples

### Set the [c]ontrol channel rendezvous point

```bash
ndc -c channel command
```

### Bind the client side to a specific [l]ocalsock address

```bash
ndc -l localsock command
```

### Set path to [p]idfile for UNIX signal control

```bash
ndc -p path/to/pidfile command
```

### Enable [d]ebugging

```bash
ndc -d command
```

### Enable [q]uiet mode

```bash
ndc -q command
```

### Enable nonfatal error [s]uppression

```bash
ndc -s command
```

### Enable [t]racing for protocol and system debugging

```bash
ndc -t command
```

### List built-in commands

```bash
ndc /help
```
