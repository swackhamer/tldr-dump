# php-coveralls

> A PHP client for Coveralls. More information: <https://php-coveralls.github.io/php-coveralls/#cli-options>.

## Examples

### Send coverage information to Coveralls

```bash
php-coveralls
```

### Send coverage information to Coveralls for a specific directory

```bash
php-coveralls [-r|--root_dir] path/to/directory
```

### Send coverage information to Coveralls with a specific config

```bash
php-coveralls [-c|--config] path/to/.coveralls.yml
```

### Send coverage information to Coveralls with verbose output

```bash
php-coveralls [-v|--verbose]
```

### Send coverage information to Coveralls excluding source files with no executable statements

```bash
php-coveralls --exclude-no-stmt
```

### Send coverage information to Coveralls with a specific environment name

```bash
php-coveralls [-e|--env] test|dev|prod
```

### Specify multiple Coverage Clover XML files to upload

```bash
php-coveralls [-x|--coverage_clover] path/to/first_clover.xml --coverage_clover path/to/second_clover.xml
```

### Output the JSON that will be sent to Coveralls to a specific file

```bash
php-coveralls [-o|--json_path] path/to/coveralls-upload.json
```
