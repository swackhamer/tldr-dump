# fish

> The Friendly Interactive SHell, a command-line interpreter designed to be user friendly. More information: <https://fishshell.com/docs/current/cmds/fish.html>.

## Examples

### Start an interactive shell session

```bash
fish
```

### Start an interactive shell session without loading startup configs

```bash
fish [-N|--no-config]
```

### Execute specific commands

```bash
fish [-c|--command] "echo 'fish is executed'"
```

### Execute a specific script

```bash
fish path/to/script.fish
```

### Check a specific script for syntax errors

```bash
fish [-N|--no-execute] path/to/script.fish
```

### Execute specific commands from `stdin`

```bash
echo "echo 'fish is executed'" | fish
```

### Start an interactive shell session in private mode, where the shell does not access old history or save new history

```bash
fish [-P|--private]
```

### Define and export an environmental variable that persists across shell restarts (builtin)

```bash
set [-U|--universal] [-x|--export] variable_name variable_value
```
