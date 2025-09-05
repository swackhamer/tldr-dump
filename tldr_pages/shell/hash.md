# hash

> View cached executable locations. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-hash>.

## Examples

### View cached command locations for the current shell

```bash
hash
```

### Clear the hash table

```bash
hash -r
```

### Delete a specific command from the hash table

```bash
hash -d command
```

### Print the full path of `command`

```bash
hash -t command
```

### Display help

```bash
hash --help
```
