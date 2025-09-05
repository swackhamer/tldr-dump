# sui-move

> Work with Move source code. More information: <https://docs.sui.io/references/cli/move>.

## Examples

### Create a new Move project in the given folder

```bash
sui move new project_name
```

### Test the Move project in the current directory

```bash
sui move test
```

### Test with coverage and get a summary

```bash
sui move test --coverage; sui move coverage summary
```

### Find which parts of your code are covered from tests (i.e. explain coverage results)

```bash
sui move coverage source --module module_name
```

### Build the Move project in the current directory

```bash
sui move build
```

### Build the Move project from the given path

```bash
sui move build --path path
```

### Migrate to Move 2024 for the package at the provided path

```bash
sui move migrate path
```
