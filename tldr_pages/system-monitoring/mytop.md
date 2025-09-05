# mytop

> Display MySQL server performance info like `top`. More information: <https://jeremy.zawodny.com/mysql/mytop/mytop.html>.

## Examples

### Start `mytop`

```bash
mytop
```

### Connect with a specified username and password

```bash
mytop [-u|-user] user [-p|-password] password
```

### Connect with a specified username (the user will be prompted for a password)

```bash
mytop [-u|-user] user -prompt
```

### Do not show any idle (sleeping) threads

```bash
mytop [-u|-user] user [-p|-password] password --noidle
```
