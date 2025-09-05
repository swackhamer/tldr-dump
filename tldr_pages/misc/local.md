# local

> Declare local variables and give them attributes. See also: `declare`, `export`. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-local>.

## Examples

### Declare a string variable with the specified value

```bash
local variable="value"
```

### Declare an integer variable with the specified value

```bash
local -i variable="value"
```

### Declare an array variable with the specified value

```bash
local variable=(item_a item_b item_c)
```

### Declare an associative array variable with the specified value

```bash
local -A variable=([key_a]=item_a [key_b]=item_b [key_c]=item_c)
```

### Declare a readonly variable with the specified value

```bash
local -r variable="value"
```

### Display help

```bash
local --help
```
