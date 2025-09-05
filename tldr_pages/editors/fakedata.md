# fakedata

> Generate fake data using a large variety of generators. More information: <https://github.com/lucapette/fakedata>.

## Examples

### List all valid generators

```bash
fakedata --generators
```

### Generate data using one or more generators

```bash
fakedata generator1 generator2
```

### Generate data with a specific output format

```bash
fakedata [-f|--format] csv|tab|sql generator
```

### Generate a given number of data items (defaults to 10)

```bash
fakedata [-l|--limit] n generator
```

### Generate data using a custom output template (the first letter of generator names must be capitalized)

```bash
echo "\{\{Generator\}\}" | fakedata
```
