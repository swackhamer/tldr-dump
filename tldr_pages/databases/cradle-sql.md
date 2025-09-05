# cradle-sql

> Manage Cradle SQL databases. More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

## Examples

### Rebuild the database schema

```bash
cradle sql build
```

### Rebuild the database schema for a specific package

```bash
cradle sql build package
```

### Empty the entire database

```bash
cradle sql flush
```

### Empty the database tables for a specific package

```bash
cradle sql flush package
```

### Populate the tables for all packages

```bash
cradle sql populate
```

### Populate the tables for a specific package

```bash
cradle sql populate package
```
