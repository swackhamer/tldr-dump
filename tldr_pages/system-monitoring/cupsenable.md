# cupsenable

> Start printers and classes. Note: Destination is referred as a printer or a class of printers. See also: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`. More information: <https://www.cups.org/doc/man-cupsenable.html>.

## Examples

### Start one or more destination(s)

```bash
cupsenable destination1 destination2 ...
```

### Resume printing of pending jobs of a destination (use after `cupsdisable` with `--hold`)

```bash
cupsenable --release destination
```

### Cancel all jobs of the specified destination(s)

```bash
cupsenable -c destination1 destination2 ...
```
