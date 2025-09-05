# mongodump

> Utility to export the contents of a MongoDB instance. More information: <https://docs.mongodb.com/database-tools/mongodump/>.

## Examples

### Create a dump of all databases (this will place the files inside a directory called "dump")

```bash
mongodump
```

### Specify an output location for the dump

```bash
mongodump [-o|--out] path/to/directory
```

### Create a dump of a given database

```bash
mongodump [-d|--db] database_name
```

### Create a dump of a given collection within a given database

```bash
mongodump [-c|--collection] collection_name [-d|--db] database_name
```

### Connect to a given host running on a given port, and create a dump

```bash
mongodump [-h|--host] host --port port
```

### Create a dump of a given database with a given username; user will be prompted for password

```bash
mongodump [-u|--username] username database [-p|--password]
```

### Create a dump from a specific instance; host, user, password and database will be defined in the connection string

```bash
mongodump --uri connection_string
```
