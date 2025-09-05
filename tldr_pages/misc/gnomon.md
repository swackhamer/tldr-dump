# gnomon

> Utility to annotate console logging statements with timestamps and find slow processes. More information: <https://github.com/paypal/gnomon>.

## Examples

### Use UNIX (or DOS) pipes to pipe `stdout` of any command through gnomon

```bash
npm test | gnomon
```

### Show number of seconds since the start of the process

```bash
npm test | gnomon --type=elapsed-total
```

### Show an absolute timestamp in UTC

```bash
npm test | gnomon --type=absolute
```

### Use a high threshold of 0.5 seconds, exceeding which the timestamp will be colored bright red

```bash
npm test | gnomon --high 0.5
```

### Use a medium threshold of 0.2 seconds, exceeding which the timestamp will be colored bright yellow

```bash
npm test | gnomon --medium 0.2
```
