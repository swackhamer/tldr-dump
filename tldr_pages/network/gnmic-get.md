# gnmic-get

> Get a snapshot of a gnmi network device operation data. More information: <https://gnmic.kmrd.dev/cmd/get>.

## Examples

### Get a snapshot of the device state at a specific path

```bash
gnmic [-a|--address] ip:port get --path path
```

### Query the device state at multiple paths

```bash
gnmic [-a|--address] ip:port get --path path/to/file_or_directory1 --path path/to/file_or_directory2
```

### Query the device state at multiple paths with a common prefix

```bash
gnmic [-a|--address] ip:port get --prefix prefix --path path/to/file_or_directory1 --path path/to/file_or_directory2
```

### Query the device state and specify response encoding (json_ietf)

```bash
gnmic [-a|--address] ip:port get --path path [-e|--encoding] json_ietf
```
