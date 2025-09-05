# kahlan

> A unit and Behaviour Driven Development test framework for PHP. More information: <https://kahlan.github.io/docs/cli-options.html>.

## Examples

### Run all specifications in the "spec" directory

```bash
kahlan
```

### Run specifications using a specific configuration file

```bash
kahlan --config=path/to/configuration_file
```

### Run specifications and output using a reporter

```bash
kahlan --reporter=dot|bar|json|tap|verbose
```

### Run specifications with code coverage (detail can be between 0 and 4)

```bash
kahlan --coverage=detail_level
```
