# lstopo

> Show the hardware topology of the system. More information: <https://manned.org/lstopo>.

## Examples

### Show the summarized system topology in a graphical window (or print to console if no graphical display is available)

```bash
lstopo
```

### Show the full system topology without summarizations

```bash
lstopo --no-factorize
```

### Show the summarized system topology with only physical indices (i.e. as seen by the OS)

```bash
lstopo [-p|--physical]
```

### Write the full system topology to a file in the specified format

```bash
lstopo --no-factorize [--of|--output-format] console|ascii|tex|fig|svg|pdf|ps|png|xml path/to/file
```

### Output in monochrome or greyscale

```bash
lstopo --palette none|grey
```
