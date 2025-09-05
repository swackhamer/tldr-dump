# snakefmt

> Format Snakemake files. More information: <https://github.com/snakemake/snakefmt>.

## Examples

### Format a specific Snakefile

```bash
snakefmt path/to/snakefile
```

### Format all Snakefiles recursively in a specific directory

```bash
snakefmt path/to/directory
```

### Format a file using a specific configuration file

```bash
snakefmt --config path/to/config.toml path/to/snakefile
```

### Format a file using a specific maximum line length

```bash
snakefmt --line-length 100 path/to/snakefile
```

### Display the changes that would be performed without performing them (dry-run)

```bash
snakefmt --diff path/to/snakefile
```
