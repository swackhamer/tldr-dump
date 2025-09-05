# aws-kendra

> CLI for AWS Kendra. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html>.

## Examples

### Create an index

```bash
aws kendra create-index --name name --role-arn role_arn
```

### List indexes

```bash
aws kendra list-indexes
```

### Describe an index

```bash
aws kendra describe-index --id index_id
```

### List data sources

```bash
aws kendra list-data-sources
```

### Describe a data source

```bash
aws kendra describe-data-source --id data_source_id
```

### List search queries

```bash
aws kendra list-query-suggestions --index-id index_id --query-text query_text
```
