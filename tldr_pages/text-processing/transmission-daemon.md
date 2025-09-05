# transmission-daemon

> Daemon controlled with `transmission-remote` or its web interface. See also: `transmission`. More information: <https://manned.org/transmission-daemon>.

## Examples

### Start a headless `transmission` session

```bash
transmission-daemon
```

### Start and watch a specific directory for new torrents

```bash
transmission-daemon [-c|--watch-dir] path/to/directory
```

### Dump daemon settings in JSON format

```bash
transmission-daemon [-d|--dump-settings] > path/to/file.json
```

### Start with specific settings for the web interface

```bash
transmission-daemon [-t|--auth] [-u|--username] username [-v|--password] password [-p|--port] 9091 [-a|--allowed] 127.0.0.1
```
