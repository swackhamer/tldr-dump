# dash

> Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not Bash-compatible). More information: <https://manned.org/dash>.

## Examples

### Start an interactive shell session

```bash
dash
```

### Execute specific [c]ommands

```bash
dash -c "echo 'dash is executed'"
```

### Execute a specific script

```bash
dash path/to/script.sh
```

### Check a specific script for syntax errors

```bash
dash -n path/to/script.sh
```

### Execute a specific script while printing each command before executing it

```bash
dash -x path/to/script.sh
```

### Execute a specific script and stop at the first [e]rror

```bash
dash -e path/to/script.sh
```

### Execute specific commands from `stdin`

```bash
echo "echo 'dash is executed'" | dash
```
