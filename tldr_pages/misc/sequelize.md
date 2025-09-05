# sequelize

> Promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server. More information: <https://sequelize.org/docs/v7/cli/>.

## Examples

### Create a model with 3 fields and a migration file

```bash
sequelize model:generate --name table_name --attributes field1:integer,field2:string,field3:boolean
```

### Run the migration file

```bash
sequelize db:migrate
```

### Revert all migrations

```bash
sequelize db:migrate:undo:all
```

### Create a seed file with the specified name to populate the database

```bash
sequelize seed:generate --name seed_filename
```

### Populate database using all seed files

```bash
sequelize db:seed:all
```
