# phpspec

> A Behaviour Driven Development tool for PHP. More information: <https://phpspec.net>.

## Examples

### Create a specification for a class

```bash
phpspec describe class_name
```

### Run all specifications in the "spec" directory

```bash
phpspec run
```

### Run a single specification

```bash
phpspec run path/to/class_specification_file
```

### Run specifications using a specific configuration file

```bash
phpspec run [-c|--config] path/to/configuration_file
```

### Run specifications using a specific bootstrap file

```bash
phpspec run [-b|--bootstrap] path/to/bootstrap_file
```

### Disable code generation prompts

```bash
phpspec run --no-code-generation
```

### Enable fake return values

```bash
phpspec run --fake
```
