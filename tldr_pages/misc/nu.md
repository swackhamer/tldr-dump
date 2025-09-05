# nu

> Nushell ("a new type of shell") takes a modern, structured approach to your command-line. See also: `elvish`. More information: <https://www.nushell.sh>.

## Examples

### Start an interactive shell session

```bash
nu
```

### Execute specific commands

```bash
nu --commands "echo 'nu is executed'"
```

### Execute a specific script

```bash
nu path/to/script.nu
```

### Execute a specific script with logging

```bash
nu --log-level error|warn|info|debug|trace path/to/script.nu
```
