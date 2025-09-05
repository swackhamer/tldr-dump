# mcfly

> A smart command history search and management tool. Replaces your default shell history search (`<Ctrl r>`) with an intelligent search engine providing context and relevance to the commands. More information: <https://github.com/cantino/mcfly>.

## Examples

### Print the mcfly integration code for the specified shell

```bash
mcfly init bash|fish|zsh
```

### Search the history for a command, with 20 results

```bash
mcfly search --results 20 "search_terms"
```

### Add a new command to the history

```bash
mcfly add "command"
```

### Record that a directory has moved and transfer the historical records from the old path to the new one

```bash
mcfly move "path/to/old_directory" "path/to/new_directory"
```

### Train the suggestion engine (developer tool)

```bash
mcfly train
```

### Display help for a specific subcommand

```bash
mcfly help subcommand
```
