# lpq

> Show printer queue status. More information: <https://openprinting.github.io/cups/doc/man-lpq.html>.

## Examples

### Show the queued jobs of the default destination

```bash
lpq
```

### Show the queued jobs of all printers enforcing encryption

```bash
lpq -a -E
```

### Show the queued jobs in a long format

```bash
lpq -l
```

### Show the queued jobs of a specific printer or class

```bash
lpq -P destination[/instance]
```

### Show the queued jobs once every n seconds until the queue is empty

```bash
lpq +interval
```
