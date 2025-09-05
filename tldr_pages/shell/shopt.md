# shopt

> Manage Bash shell options: variables (stored in `$BASHOPTS`) that control behavior specific to the Bash shell. Generic POSIX shell variables (stored in `$SHELLOPTS`) are managed with the `set` command instead. More information: <https://www.gnu.org/software/bash/manual/bash.html#The-Shopt-Builtin>.

## Examples

### List of all settable options and whether they are set

```bash
shopt
```

### Set an option

```bash
shopt -s option_name
```

### Unset an option

```bash
shopt -u option_name
```

### Print a list of all options and their status formatted as runnable `shopt` commands

```bash
shopt -p
```

### Display help

```bash
help shopt
```
