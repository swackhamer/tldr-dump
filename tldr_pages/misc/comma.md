# ,

> Run commands without installing them. More information: <https://github.com/nix-community/comma>.

## Examples

### Run a command

```bash
, command -with -flags
```

### Add a command to a child shell

```bash
, [-s|--shell] command
```

### Clear the cache

```bash
, [-e|--empty-cache]
```
