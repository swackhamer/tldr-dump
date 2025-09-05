# tcsh

> C shell with file name completion and command-line editing. See also: `csh`. More information: <https://manned.org/tcsh>.

## Examples

### Start an interactive shell session

```bash
tcsh
```

### Start an interactive shell session without loading startup configs

```bash
tcsh -f
```

### Execute specific [c]ommands

```bash
tcsh -c "echo 'tcsh is executed'"
```

### Execute a specific script

```bash
tcsh path/to/script.tcsh
```

### Check a specific script for syntax errors

```bash
tcsh -n path/to/script.tcsh
```

### Execute specific commands from `stdin`

```bash
echo "echo 'tcsh is executed'" | tcsh
```
