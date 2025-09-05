# phpunit

> PHPUnit test runner. More information: <https://phpunit.de>.

## Examples

### Run tests in the current directory. Note: Expects you to have a 'phpunit.xml'

```bash
phpunit
```

### Run tests in a specific file

```bash
phpunit path/to/TestFile.php
```

### Run tests annotated with the given group

```bash
phpunit --group name
```

### Run tests and generate a coverage report in HTML

```bash
phpunit --coverage-html path/to/directory
```
