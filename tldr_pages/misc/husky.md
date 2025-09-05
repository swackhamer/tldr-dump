# husky

> Native Git hooks made easy. More information: <https://typicode.github.io/husky>.

## Examples

### Install Husky in the current directory

```bash
husky install
```

### Install Husky into a specific directory

```bash
husky install path/to/directory
```

### Set a specific command as a `pre-push` hook for Git

```bash
husky set .husky/pre-push "command command_arguments"
```

### Add a specific command to the current `pre-commit` hook

```bash
husky add .husky/pre-commit "command command_arguments"
```

### Uninstall Husky hooks from the current directory

```bash
husky uninstall
```

### Display help

```bash
husky
```
