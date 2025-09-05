# gron

> Transform `JSON` into individual assignments for easier management. More information: <https://manned.org/gron>.

## Examples

### Process `JSON` file into individual assignments

```bash
gron path/to/file|url
```

### Don't sort output data

```bash
gron --no-sort path/to/file|url
```

### Disable certificate validation

```bash
gron [-k|--insecure] url
```

### Display values of `gron` assignments

```bash
gron [-v|--values] path/to/file|url
```

### Turn assignments converted with `gron` back into `JSON`

```bash
gron [-u|--ungron] path/to/file|url
```

### Process individual lines of input as separate `JSON` objects

```bash
gron [-s|--stream] path/to/file|url
```

### Represent processed data as a `JSON` stream

```bash
gron [-j|--json] path/to/file|url
```
