# slocate

> Secure variant of GNU Locate. See also: `locate`. More information: <https://manned.org/slocate>.

## Examples

### Enable quiet mode to suppress error messages

```bash
slocate -q
```

### Limit the number of results shown

```bash
slocate -n number
```

### Build an `slocate` database starting at path `/`

```bash
slocate -u
```

### Build an `slocate` database starting at a given directory

```bash
slocate -U path/to/directory
```

### Update an `slocate` database using the default `/etc/updatedb.conf` configuration

```bash
slocate -c
```

### Set the security level of `slocate`, with `0` being disabled, and `1` being secure

```bash
slocate -l 0|1
```

### Specify the database that `slocate` should search in

```bash
slocate [-d|--database] path/to/directory
```

### Search the `slocate` database using a specific `regex` string

```bash
slocate [-r|--regexp] regex
```
