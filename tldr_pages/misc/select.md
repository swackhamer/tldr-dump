# select

> Bash builtin construct for creating menus. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-select>.

## Examples

### Create a menu out of individual words

```bash
select word in apple orange pear banana; do echo $word; done
```

### Create a menu from the output of another command

```bash
select line in $(command); do echo $line; done
```

### Specify the prompt string for `select` and create a menu for picking a file or folder from the current directory

```bash
PS3="Select a file: "; select file in *; do echo $file; done
```

### Create a menu from a Bash array

```bash
fruits=(apple orange pear banana); select word in ${fruits[@]}; do echo $word; done
```
