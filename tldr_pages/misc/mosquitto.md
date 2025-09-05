# mosquitto

> An MQTT broker. More information: <https://mosquitto.org/man/mosquitto-8.html>.

## Examples

### Start Mosquitto

```bash
mosquitto
```

### Specify a configuration file to use

```bash
mosquitto [-c|--config-file] path/to/file.conf
```

### Listen on a specific port

```bash
mosquitto [-p|--port] 8883
```

### Daemonize by forking into the background

```bash
mosquitto [-d|--daemon]
```
