# bc

> An arbitrary precision calculator language. See also: `dc`. More information: <https://keith.github.io/xcode-man-pages/bc.1.html>.

## Examples

### Start an interactive session

```bash
bc
```

### Start an interactive session with the standard math library enabled

```bash
bc --mathlib
```

### Calculate an expression

```bash
bc --expression '5 / 3'
```

### Execute a script

```bash
bc path/to/script.bc
```

### Calculate an expression with the specified scale

```bash
bc --expression 'scale = 10; 5 / 3'
```

### Calculate a sine/cosine/arctangent/natural logarithm/exponential function using `mathlib`

```bash
bc --mathlib --expression 's|c|a|l|e(1)'
```
