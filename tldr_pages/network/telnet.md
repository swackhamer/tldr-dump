# telnet

> Connect to a specified port of a host using the telnet protocol. More information: <https://manned.org/telnet>.

## Examples

### Telnet to the default port of a host

```bash
telnet host
```

### Telnet to a specific port of a host

```bash
telnet ip_address port
```

### Exit a telnet session

```bash
quit
```

### Emit the default escape character combination for terminating the session

```bash
<Ctrl ]>
```

### Start `telnet` with "x" as the session termination character

```bash
telnet [-e|--escape] x ip_address port
```

### Telnet to Star Wars animation

```bash
telnet towel.blinkenlights.nl
```
