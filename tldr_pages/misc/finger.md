# finger

> User information lookup program. More information: <https://manned.org/finger>.

## Examples

### Display information about currently logged in users

```bash
finger
```

### Display information about a specific user

```bash
finger username
```

### Display the user's login name, real name, terminal name, and other information

```bash
finger -s
```

### Produce multiline output format displaying same information as `-s` as well as user's home directory, home phone number, login shell, mail status, etc.

```bash
finger -l
```

### Prevent matching against user's names and only use login names

```bash
finger -m
```
