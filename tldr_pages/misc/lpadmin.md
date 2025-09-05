# lpadmin

> Configure CUPS printers and classes. See also: `lpoptions`. More information: <https://openprinting.github.io/cups/doc/man-lpadmin.html>.

## Examples

### Set the default printer

```bash
lpadmin -d printer
```

### Delete a specific printer or class

```bash
lpadmin -x printer|class
```

### Add a printer to a class

```bash
lpadmin -p printer -c class
```

### Remove a printer from a class

```bash
lpadmin -p printer -r class
```
