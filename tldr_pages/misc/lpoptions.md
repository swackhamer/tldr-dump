# lpoptions

> Display or set printer options and defaults. See also: `lpadmin`. More information: <https://openprinting.github.io/cups/doc/man-lpoptions.html>.

## Examples

### Set the default printer

```bash
lpoptions -d printer[/instance]
```

### List printer-specific options of a specific printer

```bash
lpoptions -d printer -l
```

### Set a new option on a specific printer

```bash
lpoptions -d printer -o option
```

### Remove the options of a specific printer

```bash
lpoptions -d printer -x
```
