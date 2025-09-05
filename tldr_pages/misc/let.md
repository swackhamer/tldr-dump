# let

> Evaluate arithmetic expressions in shell. Supports variables, operators, and conditional expressions. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-let>.

## Examples

### Evaluate a simple arithmetic expression

```bash
let "result = a + b"
```

### Use post-increment and assignment in an expression

```bash
let "x++"
```

### Use conditional operator in an expression

```bash
let "result = (x > 10) ? x : 0"
```

### Display help

```bash
let --help
```
