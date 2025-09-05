# set

> Toggle shell options or set the values of positional parameters. More information: <https://www.gnu.org/software/bash/manual/bash.html#The-Set-Builtin>.

## Examples

### Display the names and values of shell variables

```bash
set
```

### Export newly initialized variables to child processes

```bash
set -a
```

### Write formatted messages to `stderr` when jobs finish

```bash
set -b
```

### Write and edit text in the command-line with `vi`-like keybindings (e.g. `yy`)

```bash
set -o vi
```

### Return to default mode

```bash
set -o emacs
```

### List all modes

```bash
set -o
```

### Exit the shell when (some) command fails

```bash
set -e
```

### Reset all shell parameters and assign new ones

```bash
set -- argument1 argument2 ...
```
