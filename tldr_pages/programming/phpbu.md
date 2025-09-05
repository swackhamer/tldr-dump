# phpbu

> A backup utility framework for PHP. More information: <https://phpbu.de/manual/current/en/phpbu-manual.html#cli>.

## Examples

### Run backups using the default `phpbu.xml` configuration file

```bash
phpbu
```

### Run backups using a specific configuration file

```bash
phpbu --configuration=path/to/configuration_file.xml
```

### Only run the specified backups

```bash
phpbu --limit=backup_task_name
```

### Simulate the actions that would have been performed

```bash
phpbu --simulate
```
