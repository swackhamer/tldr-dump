# gcrane-completion

> Generate the autocompletion script for gcrane for the specified shell. The available shells are `bash`, `fish`, `powershell`, and `zsh`. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

## Examples

### Generate the autocompletion script for your shell

```bash
gcrane completion shell_name
```

### Disable completion descriptions

```bash
gcrane completion shell_name --no-descriptions
```

### Load completions in your current shell session (bash/zsh)

```bash
source <(gcrane completion bash/zsh)
```

### Load completions in your current shell session (fish)

```bash
gcrane completion fish | source
```

### Load completions for every new session (bash)

```bash
gcrane completion bash > $(brew --prefix)/etc/bash_completion.d/gcrane
```

### Load completions for every new session (zsh)

```bash
gcrane completion zsh > $(brew --prefix)/share/zsh/site-functions/_gcrane
```

### Load completions for every new session (fish)

```bash
gcrane completion fish > ~/.config/fish/completions/gcrane.fish
```

### Display help

```bash
gcrane completion shell_name [-h|--help]
```
