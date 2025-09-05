# mongo

> The legacy MongoDB shell. See `mongosh` for the new shell. Note: All connection options can be replaced with one string: `mongodb://user@host:port/db_name?authSource=authdb_name`. More information: <https://docs.mongodb.com/manual/reference/program/mongo>.

## Examples

### Connect to a local database on the default port (`mongodb://localhost:27017`)

```bash
mongo
```

### Connect to a database

```bash
mongo --host host --port port db_name
```

### Authenticate using the specified username on the specified database (you will be prompted for a password)

```bash
mongo --host host --port port --username username --authenticationDatabase authdb_name db_name
```

### Evaluate a JavaScript expression on a database

```bash
mongo --eval 'JSON.stringify(db.foo.findOne())' db_name
```
