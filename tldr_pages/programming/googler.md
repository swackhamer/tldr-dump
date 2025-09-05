# googler

> Search Google from the command-line. More information: <https://github.com/jarun/googler>.

## Examples

### Search Google for a keyword

```bash
googler keyword
```

### Search Google and open the first result in web browser

```bash
googler [-j|--first] keyword
```

### Show `n` search results (default: 10)

```bash
googler [-n|--count] n keyword
```

### Disable automatic spelling correction

```bash
googler [-x|--exact] keyword
```

### Search one site for a keyword

```bash
googler [-w|--site] site keyword
```

### Show Google search result in JSON format

```bash
googler --json keyword
```

### Perform in-place self-upgrade

```bash
googler [-u|--upgrade]
```

### Display help in interactive mode

```bash
<?>
```
