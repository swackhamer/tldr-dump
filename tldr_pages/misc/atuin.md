# atuin

> Store your shell history in a searchable database. Optionally sync your encrypted history between machines. More information: <https://atuin.sh/docs/commands>.

## Examples

### Install atuin into your shell

```bash
eval "$(atuin init bash|zsh|fish)"
```

### Import history from the shell default history file

```bash
atuin import auto
```

### Search shell history for a specific command

```bash
atuin search command
```

### Register an account on the default sync server using the specified [u]sername, [e]mail and [p]assword

```bash
atuin register -u username -e email -p password
```

### Login to the default sync server

```bash
atuin login -u username -p password
```

### Sync history with the sync server

```bash
atuin sync
```
