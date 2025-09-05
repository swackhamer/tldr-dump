# xlsclients

> List client applications running on an X11 display. More information: <https://manned.org/xlsclients>.

## Examples

### List clients on the default display

```bash
xlsclients
```

### List clients on all screens

```bash
xlsclients -a
```

### List clients with detailed information

```bash
xlsclients -l
```

### Limit the command output length per client to a specific number of characters

```bash
xlsclients -m max_command_length
```

### Specify a particular display to inspect

```bash
xlsclients -display :display_number
```

### List clients on remote host's display

```bash
xlsclients -display remote_host:0
```

### Display version

```bash
xlsclients -version
```
