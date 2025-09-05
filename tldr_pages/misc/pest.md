# pest

> A PHP testing framework with a focus on simplicity. More information: <https://pestphp.com>.

## Examples

### Initialize a standard Pest configuration in the current directory

```bash
pest --init
```

### Run tests in the current directory

```bash
pest
```

### Run tests annotated with the given group

```bash
pest --group name
```

### Run tests and print the coverage report to `stdout`

```bash
pest --coverage
```

### Run tests with coverage and fail if the coverage is less than the minimum percentage

```bash
pest --coverage --min=80
```

### Run tests in parallel

```bash
pest --parallel
```

### Run tests with mutations

```bash
pest --mutate
```
