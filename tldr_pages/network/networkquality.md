# networkquality

> Measure the network quality by connecting to the internet. More information: <https://support.apple.com/101942>.

## Examples

### Test the network quality for the default interface

```bash
networkQuality
```

### Test the upload and download speeds sequentially instead of in parallel

```bash
networkQuality -s
```

### Test a specified network interface

```bash
networkQuality -I en0
```

### Test the network quality with verbose output

```bash
networkQuality -v
```
