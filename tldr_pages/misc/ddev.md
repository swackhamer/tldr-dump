# ddev

> Container based local development tool for PHP environments. More information: <https://ddev.readthedocs.io/en/stable/users/usage/cli/>.

## Examples

### Start up a project

```bash
ddev start
```

### Configure a project's type and docroot

```bash
ddev config
```

### Follow the log trail

```bash
ddev logs [-f|--follow]
```

### Run composer within the container

```bash
ddev composer
```

### Install a specific Node.js version

```bash
ddev nvm install version
```

### Export a database

```bash
ddev export-db [-f|--file] /tmp/db.sql.gz
```

### Run a specific command within a container

```bash
ddev exec echo 1
```
