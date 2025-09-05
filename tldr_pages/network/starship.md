# starship

> The minimal, blazing-fast, and infinitely customizable prompt for any shell. Some subcommands such as `init` have their own usage documentation. More information: <https://starship.rs>.

## Examples

### Print the starship integration code for the specified shell

```bash
starship init bash|elvish|fish|ion|powershell|tcsh|zsh|nu|xonsh|cmd
```

### Explain each part of the current prompt and show the time taken to render them

```bash
starship explain
```

### Print the computed starship configuration (use `--default` to print default configuration instead)

```bash
starship print-config
```

### List supported modules

```bash
starship module --list
```

### Edit the starship configuration in the default editor

```bash
starship config
```

### Create a bug report GitHub issue pre-populated with information about the system and starship configuration

```bash
starship bug-report
```

### Print the completion script for the specified shell

```bash
starship completions bash|elvish|fish|powershell|zsh
```

### Display help for a subcommand

```bash
starship subcommand --help
```
