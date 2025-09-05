# syncthing

> Continuous bidirectional decentralised folder synchronisation tool. More information: <https://docs.syncthing.net/users/syncthing.html>.

## Examples

### Start Syncthing

```bash
syncthing
```

### Start Syncthing without opening a web browser

```bash
syncthing --no-browser
```

### Change the home directory

```bash
syncthing --home path/to/directory
```

### Run Syncthing with increased logging

```bash
syncthing --verbose
```

### Pause all devices

```bash
syncthing cli config devices pause --all
```

### Resume all devices

```bash
syncthing cli config devices resume --all
```

### Change the address upon which the web interface listens

```bash
syncthing --gui-address ip_address:port|path/to/socket.sock
```

### Set the log level for output

```bash
syncthing --log-level info|warning|error|debug
```
