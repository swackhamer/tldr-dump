# mongorestore

> Utility to import a collection or database from a binary dump into a MongoDB instance. More information: <https://docs.mongodb.com/database-tools/mongorestore/>.

## Examples

### Import a BSON data dump from a directory to a MongoDB database

```bash
mongorestore --db database_name path/to/directory
```

### Import a BSON data dump from a directory to a given database in a MongoDB server host, running at a given port, with user authentication (user will be prompted for password)

```bash
mongorestore --host database_host:port --db database_name --username username path/to/directory --password
```

### Import a collection from a BSON file to a MongoDB database

```bash
mongorestore --db database_name path/to/file
```

### Import a collection from a BSON file to a given database in a MongoDB server host, running at a given port, with user authentication (user will be prompted for password)

```bash
mongorestore --host database_host:port --db database_name --username username path/to/file --password
```
