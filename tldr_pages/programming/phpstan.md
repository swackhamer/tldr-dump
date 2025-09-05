# phpstan

> A PHP static analysis tool to discover bugs in code. More information: <https://phpstan.org/user-guide/command-line-usage>.

## Examples

### Analyze one or more directories

```bash
phpstan analyse path/to/directory1 path/to/directory2 ...
```

### Analyze a directory using a configuration file

```bash
phpstan analyse path/to/directory [-c|--configuration] path/to/config
```

### Analyze using a specific rule level (0-10, higher is stricter)

```bash
phpstan analyse path/to/directory [-l|--level] level
```

### Specify an autoload file to load before analyzing

```bash
phpstan analyse path/to/directory [-a|--autoload-file] path/to/autoload_file
```

### Specify a memory limit during analysis

```bash
phpstan analyse path/to/directory --memory-limit memory_limit
```

### Display available options for analysis

```bash
phpstan analyse --help
```
