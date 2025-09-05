# sqlx

> Utility for SQLx, the Rust SQL toolkit. More information: <https://github.com/launchbadge/sqlx/blob/main/sqlx-cli/README.md>.

## Examples

### Create the database specified in the DATABASE_URL environment variable

```bash
sqlx database create
```

### Drop the specified database

```bash
sqlx database drop [-D|--database-url] database_url
```

### Create a new pair of up and down migration files with the given description in the "migrations" directory

```bash
sqlx migrate add -r migration_description
```

### Run all pending migrations for the specified database

```bash
sqlx migrate run [-D|--database-url] database_url
```

### Revert the latest migration for the specified database

```bash
sqlx migrate revert [-D|--database-url] database_url
```
