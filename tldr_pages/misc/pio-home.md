# pio-home

> Launch the PlatformIO Home web server. More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

## Examples

### Open PlatformIO Home in the default web browser

```bash
pio home
```

### Use a specific HTTP port (defaults to 8008)

```bash
pio home --port port
```

### Bind to a specific IP address (defaults to 127.0.0.1)

```bash
pio home --host ip_address
```

### Do not automatically open PlatformIO Home in the default web browser

```bash
pio home --no-open
```

### Automatically shutdown the server on timeout (in seconds) when no clients are connected

```bash
pio home --shutdown-timeout time
```

### Specify a unique session identifier to keep PlatformIO Home isolated from other instances and protected from 3rd party access

```bash
pio home --session-id id
```
