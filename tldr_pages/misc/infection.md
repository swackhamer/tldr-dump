# infection

> A mutation testing framework for PHP. More information: <https://infection.github.io>.

## Examples

### Analyze code using the configuration file (or create one if it does not exist)

```bash
infection
```

### Use a specific number of threads

```bash
infection --threads number_of_threads
```

### Specify a minimum Mutation Score Indicator (MSI)

```bash
infection --min-msi percentage
```

### Specify a minimum covered code MSI

```bash
infection --min-covered-msi percentage
```

### Use a specific test framework (defaults to PHPUnit)

```bash
infection --test-framework phpunit|phpspec
```

### Only mutate lines of code that are covered by tests

```bash
infection --only-covered
```

### Display the mutation code that has been applied

```bash
infection --show-mutations
```

### Specify the log verbosity

```bash
infection --log-verbosity default|all|none
```
