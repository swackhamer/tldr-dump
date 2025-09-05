# dict

> Command line dictionary using the DICT protocol. More information: <https://github.com/cheusov/dictd>.

## Examples

### List available databases

```bash
dict [-D|--dbs]
```

### Get information about a database

```bash
dict [-i|--info] database_name
```

### Look up a word in a specific database

```bash
dict [-d|--database] database_name word
```

### Look up a word in all available databases

```bash
dict word
```

### Show information about the DICT server

```bash
dict [-I|--serverinfo]
```
