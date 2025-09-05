# htpasswd

> Create and manage htpasswd files to protect web server directories using basic authentication. More information: <https://httpd.apache.org/docs/current/programs/htpasswd.html>.

## Examples

### Create/overwrite htpasswd file

```bash
htpasswd -c path/to/file username
```

### Add user to htpasswd file or update existing user

```bash
htpasswd path/to/file username
```

### Add user to htpasswd file in batch mode without an interactive password prompt (for script usage)

```bash
htpasswd -b path/to/file username password
```

### Delete user from htpasswd file

```bash
htpasswd -D path/to/file username
```

### Verify user password

```bash
htpasswd -v path/to/file username
```

### Display a string with username (plain text) and password (md5)

```bash
htpasswd -nbm username password
```
