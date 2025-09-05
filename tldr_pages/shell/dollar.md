# $

> Expand a Bash variable. More information: <https://gnu.org/software/bash/manual/bash.html#Shell-Variables>.

## Examples

### Print a variable

```bash
echo $VARIABLE
```

### Run variable contents as a command

```bash
$VARIABLE
```

### Print the exit status of the previous command

```bash
echo $?
```

### Print a random number between 0 and 32767

```bash
echo $RANDOM
```

### Print one of the prompt strings

```bash
echo $PS0|PS1|PS2|PS3|PS4
```

### Expand with the output of `command` and run it. Same as enclosing `command` in backtics

```bash
$(command)
```

### List how many arguments the current context has

```bash
echo $#
```

### Print out a Bash array

```bash
echo ${array_name[@]}
```
