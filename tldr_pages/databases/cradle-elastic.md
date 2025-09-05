# cradle-elastic

> Manage the Elasticsearch instances for a Cradle instance. More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

## Examples

### Truncate the Elasticsearch index

```bash
cradle elastic flush
```

### Truncate the Elasticsearch index for a specific package

```bash
cradle elastic flush package
```

### Submit the Elasticsearch schema

```bash
cradle elastic map
```

### Submit the Elasticsearch schema for a specific package

```bash
cradle elastic map package
```

### Populate the Elasticsearch indices for all packages

```bash
cradle elastic populate
```

### Populate the Elasticsearch indices for a specific package

```bash
cradle elastic populate package
```
