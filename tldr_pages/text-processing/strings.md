# strings

> Find printable strings in an object file or binary. More information: <https://manned.org/strings>.

## Examples

### Print all strings in a binary

```bash
strings path/to/file
```

### Limit results to strings at least n characters long

```bash
strings [-n|--bytes] n path/to/file
```

### Prefix each result with its offset within the file

```bash
strings [-t|--radix] d path/to/file
```

### Prefix each result with its offset within the file in hexadecimal

```bash
strings [-t|--radix] x path/to/file
```
