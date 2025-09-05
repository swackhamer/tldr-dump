# !

> Reuse and expand the shell history in `sh`, Bash, Zsh, `rbash` and `ksh`. More information: <https://gnu.org/software/bash/manual/bash.html#Event-Designators>.

## Examples

### Substitute with the previous command and run it with `sudo`

```bash
sudo !!
```

### Substitute with a command based on its line number found with `history`

```bash
!number
```

### Substitute with a command that was used a specified number of lines back

```bash
!-number
```

### Substitute with the most recent command that starts with a string

```bash
!string
```

### Substitute with the arguments of the latest command

```bash
command !*
```

### Substitute with the last argument of the latest command

```bash
command !$
```

### Substitute with the last command but without the last argument

```bash
!:-
```

### Print last command that starts with a string without executing it

```bash
!string:p
```
