# eol

> Show end-of-life dates (EoLs) for a number of products. More information: <https://github.com/hugovk/norwegianblue>.

## Examples

### List all available products

```bash
eol
```

### Get EoLs of one or more products

```bash
eol product1 product2 ...
```

### Open the product webpage

```bash
eol product --web
```

### Get EoLs of a one or more products in a specific format

```bash
eol product1 product2 ... --format html|json|md|markdown|pretty|rst|csv|tsv|yaml
```

### Get EoLs of one or more products as a single markdown file

```bash
eol product1 product2 ... --format markdown > eol_report.md
```

### Display help

```bash
eol --help
```
