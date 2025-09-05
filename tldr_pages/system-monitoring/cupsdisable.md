# cupsdisable

> Stop printers and classes. Note: Destination is referred as a printer or a class of printers. See also: `cupsenable`, `cupsaccept`, `cupsreject`, `lpstat`. More information: <https://openprinting.github.io/cups/doc/man-cupsenable.html>.

## Examples

### Stop one or more destination(s)

```bash
cupsdisable destination1 destination2 ...
```

### Cancel all jobs of the specified destination(s)

```bash
cupsdisable -c destination1 destination2 ...
```
