# gitea

> Administer Gitea, a lightweight Git hosting server. Requires a configured `app.ini` file or environment variables. More information: <https://docs.gitea.com/administration/command-line>.

## Examples

### Run the Gitea web server using the default configuration

```bash
gitea web
```

### Create the necessary database schema and tables

```bash
gitea migrate
```

### Run administrative subcommands for user management or authentication management

```bash
gitea admin user list
```

### Display help for a specific subcommand

```bash
gitea admin --help
```

### Display help

```bash
gitea help
```

### Display version

```bash
gitea --version
```
