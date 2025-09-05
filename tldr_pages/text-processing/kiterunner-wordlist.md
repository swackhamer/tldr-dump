# kiterunner-wordlist

> A contextual web scanner for managing wordlists used in API and web endpoint discovery. The `wordlist` subcommand handles listing and saving wordlists in `~/.cache/kiterunner`. More information: <https://github.com/assetnote/kiterunner>.

## Examples

### List all cached and available Assetnote wordlists

```bash
kiterunner wordlist list
```

### List wordlists with JSON output

```bash
kiterunner wordlist list [-o|--output] json
```

### List wordlists with verbose debug output

```bash
kiterunner wordlist list [-v|--verbose] debug
```

### Save a specific Assetnote wordlist by alias

```bash
kiterunner wordlist save apiroutes-210328
```

### Save a specific Assetnote wordlist by full filename

```bash
kiterunner wordlist save path/to/httparchive_apiroutes_2024_05_28.txt
```

### Save multiple wordlists by alias

```bash
kiterunner wordlist save apiroutes-210328,aspx-210328
```

### Save a wordlist with quiet mode to suppress output

```bash
kiterunner wordlist save apiroutes-210328 [-q|--quiet]
```
