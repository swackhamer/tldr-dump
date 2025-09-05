# id

> Display current user and group identity. More information: <https://www.gnu.org/software/coreutils/manual/html_node/id-invocation.html>.

## Examples

### Display current user's ID (UID), group ID (GID) and groups to which they belong

```bash
id
```

### Display the current user identity

```bash
id [-un|--user --name]
```

### Display the current user identity as a number

```bash
id [-u|--user]
```

### Display the current primary group identity

```bash
id [-gn|--group --name]
```

### Display the current primary group identity as a number

```bash
id [-g|--group]
```

### Display an arbitrary user's ID (UID), group ID (GID) and groups to which they belong

```bash
id username
```
