# command

> Command forces the shell to execute the program and ignore any functions, builtins and aliases with the same name. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-command>.

## Examples

### Execute the `ls` program literally, even if an `ls` alias exists

```bash
command ls
```

### Find and execute a command using a default `$PATH` (`/bin:/usr/bin:/sbin:/usr/sbin:/etc:/usr/etc`) that guarantees to find all standard utilities

```bash
command -p command_name
```

### Display the path to the executable or the alias definition of a specific command

```bash
command -v command_name
```
