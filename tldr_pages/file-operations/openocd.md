# openocd

> Debug and program embedded systems with OpenOCD. More information: <https://manned.org/openocd>.

## Examples

### Attach OpenOCD session to a board with a configuration file

```bash
openocd [-f|--file] config_file.cfg
```

### Attach OpenOCD session to a board with multiple configuration files

```bash
openocd [-f|--file] config_file1.cfg [-f|--file] config_file2.cfg
```

### Attach OpenOCD session to a board with configuration files and a list of commands to be executed on server startup

```bash
openocd [-f|--file] config_file.cfg [-c|--command] "command"
```

### Use configuration files in the specified path

```bash
openocd [-s|--search] path/to/search [-f|--file] config_file.cfg
```

### After OpenOCD startup, connect GDB to OpenOCD default port 3333

```bash
target extended-remote localhost
```

### List site-wide script library

```bash
ls /usr/local/share/openocd/scripts
```
