# picocom

> Minimal program to emulate serial consoles. More information: <https://manned.org/picocom>.

## Examples

### Connect to a serial console with the default baud rate of 9600

```bash
sudo picocom /dev/ttyXYZ
```

### Connect to a serial console with a specified baud rate

```bash
sudo picocom /dev/ttyXYZ [-b|--baud] baud_rate
```

### Map special characters (e.g. `LF` to `CRLF`)

```bash
sudo picocom /dev/ttyXYZ --imap lfcrlf
```

### Exit picocom

```bash
<Ctrl a><Ctrl x>
```

### Display help

```bash
picocom [-h|--help]
```
