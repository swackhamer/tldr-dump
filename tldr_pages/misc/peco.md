# peco

> Interactive filtering tool. More information: <https://github.com/peco/peco>.

## Examples

### Start `peco` on all files in the specified directory

```bash
find path/to/directory -type f | peco
```

### Start `peco` for running processes

```bash
ps aux | peco
```

### Start `peco` with a specified query

```bash
peco --query "query"
```
