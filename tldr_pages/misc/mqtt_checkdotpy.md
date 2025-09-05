# mqtt_check.py

> Simple utility for testing and validating MQTT login credentials. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Check MQTT login credentials for a target (MQTT broker's hostname)

```bash
mqtt_check.py domain/username:password@targetName
```

### Specify a custom client ID for authentication

```bash
mqtt_check.py -client-id client_id domain/username:password@targetName
```

### Enable SSL for the connection

```bash
mqtt_check.py -ssl domain/username:password@targetName
```

### Connect to a specific port (default is 1883)

```bash
mqtt_check.py -port port domain/username:password@targetName
```

### Enable debug output

```bash
mqtt_check.py -debug domain/username:password@targetName
```

### Display help

```bash
mqtt_check.py --help
```
