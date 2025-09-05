# rails-db

> Various database-related subcommands for Ruby on Rails. More information: <https://guides.rubyonrails.org/active_record_migrations.html>.

## Examples

### Create databases, load the schema, and initialize with seed data

```bash
rails db:setup
```

### Access the database console

```bash
rails db
```

### Create the databases defined in the current environment

```bash
rails db:create
```

### Destroy the databases defined in the current environment

```bash
rails db:drop
```

### Run pending migrations

```bash
rails db:migrate
```

### View the status of each migration file

```bash
rails db:migrate:status
```

### Rollback the last migration

```bash
rails db:rollback
```

### Fill the current database with data defined in `db/seeds.rb`

```bash
rails db:seed
```
