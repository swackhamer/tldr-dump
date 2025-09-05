# {

> Multipurpose shell syntax. More information: <https://www.gnu.org/software/bash/manual/bash.html>.

## Examples

### Isolate variable names

```bash
echo ${HOME}work
```

### Brace expand sequences

```bash
echo {1..3} {a..c}{dir1,dir2,dir3}
```

### Check if `variable` is set before returning text

```bash
echo ${variable:+variable is set and contains $variable}
```

### Set default values in case `variable` is unset

```bash
echo ${variable:-default}
```

### Return `variable` length in characters

```bash
echo ${#variable}
```

### Return a string slice

```bash
echo ${variable:3:7}
```

### Recursively expand a `variable`

```bash
echo ${!variable}
```

### Group command output together

```bash
{ command1; command2; ... } | another_command
```
