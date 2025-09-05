# psalm

> A static analysis tool for finding errors in PHP applications. More information: <https://psalm.dev>.

## Examples

### Generate a Psalm configuration

```bash
psalm --init
```

### Analyze the current working directory

```bash
psalm
```

### Analyze a specific directory or file

```bash
psalm path/to/file_or_directory
```

### Analyze a project with a specific configuration file

```bash
psalm --config path/to/psalm.xml
```

### Include informational findings in the output

```bash
psalm --show-info
```

### Analyze a project and display statistics

```bash
psalm --stats
```

### Analyze a project in parallel with 4 threads

```bash
psalm --threads 4
```
