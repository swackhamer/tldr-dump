# typeorm

> A JavaScript ORM that can run on Node.js, browser, Cordova, Ionic, React Native, NativeScript, and Electron platforms. More information: <https://typeorm.io/docs/advanced-topics/using-cli/#initialize-a-new-typeorm-project>.

## Examples

### Generate a new initial TypeORM project structure

```bash
typeorm init
```

### Create an empty migration file

```bash
typeorm migration:create --name migration_name
```

### Create a migration file with the SQL statements to update the schema

```bash
typeorm migration:generate --name migration_name
```

### Run all pending migrations

```bash
typeorm migration:run
```

### Create a new entity file in a specific directory

```bash
typeorm entity:create --name entity --dir path/to/directory
```

### Display the SQL statements to be executed by `typeorm schema:sync` on the default connection

```bash
typeorm schema:log
```

### Execute a specific SQL statement on the default connection

```bash
typeorm query sql_sentence
```

### Display help for a subcommand

```bash
typeorm subcommand --help
```
