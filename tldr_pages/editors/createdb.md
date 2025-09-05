# createdb

> Create a PostgreSQL database. More information: <https://www.postgresql.org/docs/current/app-createdb.html>.

## Examples

### Create a database owned by the current user

```bash
createdb database_name
```

### Create a database owned by a specific user with a description

```bash
createdb --owner username database_name 'description'
```

### Create a database from a template

```bash
createdb --template template_name database_name
```
