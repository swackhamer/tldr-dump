# rbash

> Restricted Bash shell, equivalent to `bash --restricted`. Does not permit changing the working directory, redirecting command output, or modifying environment variables, among other things. See also: `histexpand` for history expansion. More information: <https://www.gnu.org/software/bash/manual/bash.html#The-Restricted-Shell>.

## Examples

### Start an interactive shell session

```bash
rbash
```

### Execute a command and then exit

```bash
rbash -c "command"
```

### Execute a script

```bash
rbash path/to/script.sh
```

### Execute a script, printing each command before executing it

```bash
rbash -x path/to/script.sh
```

### Execute commands from a script, stopping at the first error

```bash
rbash -e path/to/script.sh
```

### Read and execute commands from `stdin`

```bash
rbash -s
```
