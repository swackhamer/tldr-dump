# unset

> Remove shell variables or functions. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-unset>.

## Examples

### Remove the variable `foo`, or if the variable doesn't exist, remove the function `foo`

```bash
unset foo
```

### Remove the variables foo and bar

```bash
unset -v foo bar
```

### Remove the function my_func

```bash
unset -f my_func
```
