# csh

> The shell (command interpreter) with C-like syntax. See also: `tcsh`. More information: <https://www.mkssoftware.com/docs/man1/csh.1.asp>.

## Examples

### Start an interactive shell session

```bash
csh
```

### Start an interactive shell session without loading startup configs

```bash
csh -f
```

### Execute specific [c]ommands

```bash
csh -c "echo 'csh is executed'"
```

### Execute a specific script

```bash
csh path/to/script.csh
```
