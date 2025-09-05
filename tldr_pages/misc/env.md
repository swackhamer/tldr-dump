# env

> Show the environment or run a program in a modified environment. More information: <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

## Examples

### Show the environment

```bash
env
```

### Run a program. Often used in scripts after the shebang (#!) for looking up the path to the program

```bash
env program
```

### Clear the environment and run a program

```bash
env [-i|--ignore-environment] program
```

### Remove variable from the environment and run a program

```bash
env [-u|--unset] variable program
```

### Set a variable and run a program

```bash
env variable=value program
```

### Set one or more variables and run a program

```bash
env variable1=value variable2=value variable3=value ... program
```

### Run a program under a different name

```bash
env [-a|--argv0] custom_name program
```
