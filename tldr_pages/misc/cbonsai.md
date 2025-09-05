# cbonsai

> A beautifully random bonsai tree generator. More information: <https://gitlab.com/jallbrit/cbonsai>.

## Examples

### Generate a bonsai in live mode

```bash
cbonsai [-l|--live]
```

### Generate a bonsai in infinite mode

```bash
cbonsai [-i|--infinite]
```

### Set the growth factor of the tree (default: 32)

```bash
cbonsai [-L|--life] 0..200
```

### Set the branching factor of the tree (default: 5)

```bash
cbonsai [-M|--multiplier] 0..20
```

### Run in screensaver mode (equivalent to `--live --infinite` but any keypress exits)

```bash
cbonsai [-S|--screensaver]
```

### Append a message to the bonsai

```bash
cbonsai [-m|--message] "message"
```

### Display extra information about the bonsai

```bash
cbonsai [-v|--verbose]
```

### Display help

```bash
cbonsai [-h|--help]
```
