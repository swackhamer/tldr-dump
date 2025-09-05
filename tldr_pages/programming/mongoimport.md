# mongoimport

> Imports content from a JSON, CSV, or TSV file into a MongoDB database. More information: <https://docs.mongodb.com/database-tools/mongoimport/>.

## Examples

### Import a JSON file into a specific collection

```bash
mongoimport --file path/to/file.json --uri mongodb_uri [-c|--collection] collection_name
```

### Import a CSV file, using the first line of the file to determine field names

```bash
mongoimport --type csv --file path/to/file.csv [-d|--db] database_name [-c|--collection] collection_name
```

### Import a JSON array, using each element as a separate document

```bash
mongoimport --jsonArray --file path/to/file.json
```

### Import a JSON file using a specific mode and a query to match existing documents

```bash
mongoimport --file path/to/file.json --mode delete|merge|upsert --upsertFields "field1,field2,..."
```

### Import a CSV file, reading field names from a separate CSV file and ignoring fields with empty values

```bash
mongoimport --type csv --file path/to/file.csv --fieldFile path/to/field_file.csv --ignoreBlanks
```

### Display help

```bash
mongoimport --help
```
