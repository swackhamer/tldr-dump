# compgen

> Bash built-in command for generating possible completion matches in Bash. Usually used within custom completion functions. See also: `complete`, `compopt`. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

## Examples

### List all shell built-ins, aliases, functions and executables that you could run

```bash
compgen -c
```

### List all commands that you could run that start with a specified string and save results to `COMPREPLY`

```bash
compgen -V COMPREPLY -c str
```

### Match against a wordlist

```bash
compgen -W "apple orange banana" a
```

### List all aliases

```bash
compgen -a
```

### List all functions that you could run

```bash
compgen -A function
```

### Show shell reserved keywords

```bash
compgen -k
```

### See all available commands/aliases starting with 'ls'

```bash
compgen -ac ls
```

### List all users on the system

```bash
compgen -u
```
