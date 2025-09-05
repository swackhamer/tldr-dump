# pio-device

> Manage and monitor PlatformIO devices. More information: <https://docs.platformio.org/en/latest/core/userguide/device/>.

## Examples

### List all available serial ports

```bash
pio device list
```

### List all available logical devices

```bash
pio device list --logical
```

### Start an interactive device monitor

```bash
pio device monitor
```

### Start an interactive device monitor and listen to a specific port

```bash
pio device monitor [-p|--port] /dev/ttyUSBX
```

### Start an interactive device monitor and set a specific baud rate (defaults to 9600)

```bash
pio device monitor [-b|--baud] 57600
```

### Start an interactive device monitor and set a specific EOL character (defaults to `CRLF`)

```bash
pio device monitor --eol CRLF|CR|LF
```

### Go to the menu of the interactive device monitor

```bash
<Ctrl t>
```
