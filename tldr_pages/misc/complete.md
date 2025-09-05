# complete

> Get and set argument autocompletion rules of shell commands in Bash. The specified completions will be invoked when `<Tab>` is pressed in Bash. See also: `compgen`, `compopt`. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-complete>.

## Examples

### Set arguments of a command to autocomplete through a function (completion response is sent in `COMPREPLY` variable)

```bash
complete -F function command
```

### Set arguments of a command to autocomplete through another command (`$1` is the command, `$2` is the argument the cursor is on, and `$3` is the argument preceding the cursor)

```bash
complete -C autocomplete_command command
```

### Set arguments of a command to autocomplete to shell builtins

```bash
complete -b command
```

### Apply autocompletion without appending a space to the completed word

```bash
complete -o nospace -F function command
```

### List all loaded complete specifications

```bash
complete -p
```

### List loaded complete specifications for a command

```bash
complete -p command
```
