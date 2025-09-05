# lastcomm

> Show last commands executed. More information: <https://manpages.debian.org/latest/acct/lastcomm.1.en.html>.

## Examples

### Print information about all the commands in the acct (record file)

```bash
lastcomm
```

### Display commands executed by a given user

```bash
lastcomm --user user
```

### Display information about a given command executed on the system

```bash
lastcomm --command command
```

### Display information about commands executed on a given terminal

```bash
lastcomm --tty terminal_name
```
