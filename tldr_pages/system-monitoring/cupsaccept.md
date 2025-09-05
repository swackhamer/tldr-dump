# cupsaccept

> Accept jobs sent to destinations. Note: Destination is referred as a printer or a class of printers. See also: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`. More information: <https://www.cups.org/doc/man-cupsaccept.html>.

## Examples

### Accept print jobs to the specified destinations

```bash
cupsaccept destination1 destination2 ...
```

### Specify a different server

```bash
cupsaccept -h server destination1 destination2 ...
```
