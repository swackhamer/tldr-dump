# declare

> Declare variables and give them attributes. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-declare>.

## Examples

### Declare a string variable with the specified value

```bash
declare variable="value"
```

### Declare an integer variable with the specified value

```bash
declare -i variable="value"
```

### Declare an array variable with the specified value

```bash
declare -a variable=(item_a item_b item_c)
```

### Declare an associative array variable with the specified value

```bash
declare -A variable=([key_a]=item_a [key_b]=item_b [key_c]=item_c)
```

### Declare a readonly string variable with the specified value

```bash
declare -r variable="value"
```

### Declare a global variable within a function with the specified value

```bash
declare -g variable="value"
```

### Print a function definition

```bash
declare -f function_name
```

### Print a variable definition

```bash
declare -p variable_name
```
