# pio-debug

> Debug PlatformIO projects. More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

## Examples

### Debug the PlatformIO project in the current directory

```bash
pio debug
```

### Debug a specific PlatformIO project

```bash
pio debug [-d|--project-dir] path/to/platformio_project
```

### Debug a specific environment

```bash
pio debug [-e|--environment] environment
```

### Debug a PlatformIO project using a specific configuration file

```bash
pio debug [-c|--project-conf] path/to/platformio.ini
```

### Debug a PlatformIO project using the `gdb` debugger

```bash
pio debug --interface gdb gdb_options
```
