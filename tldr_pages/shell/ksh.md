# ksh

> Korn Shell, a Bash-compatible command-line interpreter. See also: `!`, `^`. More information: <https://manned.org/ksh>.

## Examples

### Start an interactive shell session

```bash
ksh
```

### Execute specific [c]ommands

```bash
ksh -c "echo 'ksh is executed'"
```

### Execute a specific script

```bash
ksh path/to/script.ksh
```

### Check a specific script for syntax errors without executing it

```bash
ksh -n path/to/script.ksh
```

### Execute a specific script, printing each command in the script before executing it

```bash
ksh -x path/to/script.ksh
```
