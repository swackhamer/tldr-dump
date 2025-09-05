# hashid

> Python3 program that identifies data and password hashes. More information: <https://github.com/psypanda/hashID>.

## Examples

### Identify hashes from `stdin` (through typing, copying and pasting, or piping the hash into the program)

```bash
hashid
```

### Identify one or more hashes

```bash
hashid hash1 hash2 ...
```

### Identify hashes on a file (one hash per line)

```bash
hashid path/to/hashes.txt
```

### Show all possible hash types (including salted hashes)

```bash
hashid --extended hash
```

### Show `hashcat`'s mode number and `john`'s format string of the hash types

```bash
hashid --mode --john hash
```

### Save output to a file instead of printing to `stdout`

```bash
hashid --outfile path/to/output.txt hash
```
