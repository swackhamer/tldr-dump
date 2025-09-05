# passwd

> Change a user's password. More information: <https://manned.org/passwd>.

## Examples

### Change the password of the current user interactively

```bash
passwd
```

### Change the password of a specific user

```bash
passwd username
```

### Get the current status of the user

```bash
passwd [-S|--status]
```

### Make the password of the account blank (it will set the named account passwordless)

```bash
passwd [-d|--delete]
```

### Set password programmatically (ideal for install scripts)

```bash
yes password | passwd
```
