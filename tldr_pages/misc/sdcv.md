# sdcv

> StarDict, a dictionary client. Dictionaries are provided separately from the client. More information: <https://manned.org/sdcv>.

## Examples

### Start `sdcv` interactively

```bash
sdcv
```

### List installed dictionaries

```bash
sdcv --list-dicts
```

### Display a definition from a specific dictionary

```bash
sdcv --use-dict dictionary_name search_term
```

### Look up a definition with a fuzzy search

```bash
sdcv search_term
```

### Look up a definition with an exact search

```bash
sdcv --exact-search search_term
```

### Look up a definition and format the output as JSON

```bash
sdcv --json search_term
```

### Search for dictionaries in a specific directory

```bash
sdcv --data-dir path/to/directory search_term
```
