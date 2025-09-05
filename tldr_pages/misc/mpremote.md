# mpremote

> Remotely control MicroPython devices. More information: <https://docs.micropython.org/en/latest/reference/mpremote.html>.

## Examples

### List all connected MicroPython devices

```bash
mpremote connect list
```

### Open an interactive REPL session with a connected device

```bash
mpremote connect device
```

### Run a local script on a connected device

```bash
mpremote run path/to/script.py
```

### Mount a local directory to the device

```bash
mpremote mount path/to/directory
```

### Install a mip package on the device

```bash
mpremote mip install package
```
