# type

> Display the type of command the shell will execute. Note: All examples are not POSIX compliant. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-type>.

## Examples

### Display the type of a command

```bash
type command
```

### Display all locations containing the specified executable (works only in Bash/fish/Zsh shells)

```bash
type -a command
```

### Display the name of the disk file that would be executed (works only in Bash/fish/Zsh shells)

```bash
type -p command
```

### Display the type of a specific command, alias/keyword/function/builtin/file (works only in Bash/fish shells)

```bash
type -t command
```
