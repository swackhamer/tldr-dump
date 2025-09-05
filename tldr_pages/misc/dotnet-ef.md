# dotnet-ef

> Perform design-time development tasks for Entity Framework Core. More information: <https://learn.microsoft.com/ef/core/cli/dotnet>.

## Examples

### Update the database to a specified migration

```bash
dotnet ef database update migration
```

### Drop the database

```bash
dotnet ef database drop
```

### List available `DbContext` types

```bash
dotnet ef dbcontext list
```

### Generate code for a `DbContext` and entity types for a database

```bash
dotnet ef dbcontext scaffold connection_string provider
```

### Add a new migration

```bash
dotnet ef migrations add name
```

### Remove the last migration, rolling back the code changes that were done for the latest migration

```bash
dotnet ef migrations remove
```

### List available migrations

```bash
dotnet ef migrations list
```

### Generate an SQL script from migrations range

```bash
dotnet ef migrations script from_migration to_migration
```
