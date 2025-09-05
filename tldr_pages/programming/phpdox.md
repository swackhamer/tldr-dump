# phpdox

> A PHP documentation generator. More information: <https://phpdox.net>.

## Examples

### Display an annotated skeleton configuration XML file

```bash
phpdox --skel
```

### Generate documentation for the current working directory

```bash
phpdox
```

### Generate documentation using a specific configuration file

```bash
phpdox [-f|--file] path/to/phpdox.xml
```

### Only run the metadata collection process

```bash
phpdox [-c|--collector]
```

### Only run the documentation generator process

```bash
phpdox [-g|--generator]
```
