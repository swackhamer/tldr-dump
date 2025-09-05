# mongod

> The MongoDB database server. More information: <https://docs.mongodb.com/manual/reference/program/mongod>.

## Examples

### Specify the storage directory (default: `/data/db` on Linux and macOS, `C:\data\db` on Windows)

```bash
mongod --dbpath path/to/directory
```

### Specify a configuration file

```bash
mongod --config path/to/file
```

### Specify the port to listen on (default: 27017)

```bash
mongod --port port
```

### Specify the database profiling level. 0 is off, 1 is only slow operations, 2 is all (default: 0)

```bash
mongod --profile 0|1|2
```
