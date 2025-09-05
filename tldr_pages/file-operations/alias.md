# alias

> Create aliases - words that are replaced by a command string. Aliases expire with the current shell session unless defined in the shell's configuration file, e.g. `~/.bashrc` for Bash or `~/.zshrc` for Zsh. See also: `unalias`. More information: <https://www.gnu.org/software/bash/manual/bash.html#index-alias>.

## Examples

### List all aliases

```bash
alias
```

### Create a generic alias

```bash
alias word="command"
```

### View the command associated to a given alias

```bash
alias word
```

### Remove an aliased command

```bash
unalias word
```

### Turn `rm` into an interactive command

```bash
alias rm="rm --interactive"
```

### Create `la` as a shortcut for `ls --all`

```bash
alias la="ls --all"
```
