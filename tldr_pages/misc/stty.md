# stty

> Set options for a terminal device interface. More information: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

## Examples

### Display current terminal size

```bash
stty size
```

### Display all settings for the current terminal

```bash
stty [-a|--all]
```

### Set the number of rows or columns

```bash
stty rows|cols count
```

### Get the actual transfer speed of a device

```bash
stty [-F|--file] path/to/device_file speed
```

### Reset all modes to reasonable values for the current terminal

```bash
stty sane
```

### Switch between raw and normal mode

```bash
stty raw|cooked
```

### Turn character echoing off or on

```bash
stty -echo|echo
```

### Display help

```bash
stty --help
```
