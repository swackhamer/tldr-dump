# calc

> An interactive arbitrary-precision calculator in the terminal. More information: <https://manned.org/calc>.

## Examples

### Start `calc` in interactive mode

```bash
calc
```

### Perform a calculation in non-interactive mode

```bash
calc '85 * (36 / 4)'
```

### Don't format the output (for use with [p]ipes)

```bash
calc -p '4/3 * pi() * 5^3'
```

### Perform a calculation and then switch to [i]nteractive mode

```bash
calc -i 'sqrt(2)'
```

### Start `calc` in a specific permission [m]ode (0 to 7, defaults to 7)

```bash
calc -m mode
```

### View an introduction to `calc`

```bash
calc help intro
```

### View an overview of `calc`

```bash
calc help overview
```

### Open the `calc` manual

```bash
calc help
```
