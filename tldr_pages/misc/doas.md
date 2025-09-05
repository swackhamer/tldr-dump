# doas

> Execute a command as another user. More information: <https://man.openbsd.org/doas>.

## Examples

### Run a command as root

```bash
doas command
```

### Run a command as another user

```bash
doas -u user command
```

### Launch the default shell as root

```bash
doas -s
```

### Parse a configuration file and check if the execution of a command as another user is allowed

```bash
doas -C path/to/config_file command
```

### Make `doas` request a password even after it was supplied earlier

```bash
doas -L
```
