# john

> Password cracker. More information: <https://www.openwall.com/john/>.

## Examples

### Crack password hashes

```bash
john path/to/hashes.txt
```

### Show passwords cracked

```bash
john --show path/to/hashes.txt
```

### Display users' cracked passwords by user identifier from multiple files

```bash
john --show --users=user_ids path/to/hashes1.txt path/to/hashes2.txt ...
```

### Crack password hashes, using a custom wordlist

```bash
john --wordlist=path/to/wordlist.txt path/to/hashes.txt
```

### List available hash formats

```bash
john --list=formats
```

### Crack password hashes, using a specific hash format

```bash
john --format=md5crypt path/to/hashes.txt
```

### Crack password hashes, enabling word mangling rules

```bash
john --rules path/to/hashes.txt
```

### Restore an interrupted cracking session from a state file, e.g. `mycrack.rec`

```bash
john --restore=path/to/mycrack.rec
```
