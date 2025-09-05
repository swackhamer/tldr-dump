# drupal-check

> Check Drupal PHP code for deprecations. More information: <https://github.com/mglaman/drupal-check#usage>.

## Examples

### Check the code in a specific directory for deprecations

```bash
drupal-check path/to/directory
```

### Check the code excluding a comma-separated list of directories

```bash
drupal-check [-e|--exclude-dir] path/to/excluded_directory,path/to/excluded_files/*.php path/to/directory
```

### Don't show a progress bar

```bash
drupal-check --no-progress path/to/directory
```

### Perform static analysis to detect bad coding practices

```bash
drupal-check [-a|--analysis] path/to/directory
```
