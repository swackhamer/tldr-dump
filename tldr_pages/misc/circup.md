# circup

> The CircuitPython library updater. More information: <https://github.com/adafruit/circup>.

## Examples

### Interactively update modules on a device

```bash
circup update
```

### Install a new library

```bash
circup install library_name
```

### Search for a library

```bash
circup show partial_name
```

### List all libraries on a connected device in `requirements.txt` format

```bash
circup freeze
```

### Save all libraries on a connected device in `requirements.txt` in current directory

```bash
circup freeze [-r|--requirement]
```
