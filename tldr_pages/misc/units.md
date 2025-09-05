# units

> Convert between two units of measure. More information: <https://www.gnu.org/software/units/manual/units.html>.

## Examples

### Run in interactive mode

```bash
units
```

### List all units containing a specific string in interactive mode

```bash
search string
```

### Show the conversion between two simple units

```bash
units quarts tablespoons
```

### Convert between units with quantities

```bash
units "15 pounds" kilograms
```

### Show the conversion between two compound units

```bash
units "meters / second" "inches / hour"
```

### Show the conversion between units with different dimensions

```bash
units "acres" "ft^2"
```

### Show the conversion of byte multipliers

```bash
units "15 megabytes" bytes
```
