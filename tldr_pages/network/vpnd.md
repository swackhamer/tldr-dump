# vpnd

> Listens for incoming VPN connections. It should not be invoked manually. More information: <https://keith.github.io/xcode-man-pages/vpnd.8.html>.

## Examples

### Start the daemon

```bash
vpnd
```

### Run the daemon in the foreground

```bash
vpnd -x
```

### Run the daemon in the foreground and print logs to the terminal

```bash
vpnd -d
```

### Run the daemon in the foreground, print logs to the terminal, and quit after validating arguments

```bash
vpnd -n
```

### Run the daemon for a specific server configuration

```bash
vpnd -i server_id
```

### Display help

```bash
vpnd -h
```
