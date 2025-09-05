# aws-dynamodb

> Manipulate an AWS Dynamodb database, a fast NoSQL database with predictable performance and seamless scalability. More information: <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/>.

## Examples

### Create a table

```bash
aws dynamodb create-table --table-name table_name --attribute-definitions AttributeName=S,AttributeType=S --key-schema AttributeName=S,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

### List all tables in the DynamoDB

```bash
aws dynamodb list-tables
```

### Get details about a specific table

```bash
aws dynamodb describe-table --table-name table_name
```

### Add an item to a table

```bash
aws dynamodb put-item --table-name table_name --item '{"AttributeName": {"S": "value"'
```

### Retrieve an item from a table

```bash
aws dynamodb get-item --table-name table_name --key '{"ID": {"N": "1"'
```

### Update an item in the table

```bash
aws dynamodb update-item --table-name table_name --key '{"ID": {"N": "1"' --update-expression "SET Name = :n" --expression-attribute-values '{":n": {"S": "Jane"'
```

### Scan items in the table

```bash
aws dynamodb scan --table-name table_name
```

### Delete an item from the table

```bash
aws dynamodb delete-item --table-name table_name --key '{"ID": {"N": "1"'
```
