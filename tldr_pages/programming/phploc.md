# phploc

> Quickly measure the size and analyzing the structure of a PHP project. More information: <https://github.com/sebastianbergmann/phploc>.

## Examples

### Analyze a directory and print the result

```bash
phploc path/to/directory
```

### Include only specific files from a comma-separated list (globs are allowed)

```bash
phploc path/to/directory --names 'path/to/file1,path/to/file2,...'
```

### Exclude specific files from a comma-separated list (globs are allowed)

```bash
phploc path/to/directory --names-exclude 'path/to/file1,path/to/file2,...'
```

### Exclude a specific directory from analysis

```bash
phploc path/to/directory --exclude path/to/exclude_directory
```

### Log the results to a specific CSV file

```bash
phploc path/to/directory --log-csv path/to/file
```

### Log the results to a specific XML file

```bash
phploc path/to/directory --log-xml path/to/file
```

### Count PHPUnit test case classes and test methods

```bash
phploc path/to/directory --count-tests
```
