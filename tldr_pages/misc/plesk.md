# plesk

> Plesk hosting control panel. More information: <https://docs.plesk.com>.

## Examples

### Generate an auto login link for the admin user and print it

```bash
plesk login
```

### Show product version information

```bash
plesk version
```

### List all hosted domains

```bash
plesk bin domain --list
```

### Start watching for changes in the `panel.log` file

```bash
plesk log panel.log
```

### Start the interactive MySQL console

```bash
plesk db
```

### Open the Plesk main configuration file in the default editor

```bash
plesk conf panel.ini
```
