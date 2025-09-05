# cradle-install

> Install the Cradle PHP framework components. More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

## Examples

### Install Cradle's components (User will be prompted for further details)

```bash
cradle install
```

### Forcefully overwrite files

```bash
cradle install [-f|--force]
```

### Skip running SQL migrations

```bash
cradle install --skip-sql
```

### Skip running package updates

```bash
cradle install --skip-versioning
```

### Use specific database details

```bash
cradle install -h hostname -u username -p password
```
