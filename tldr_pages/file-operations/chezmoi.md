# chezmoi

> A multi-machine dotfile manager, written in Go. See also: `stow`, `tuckr`, `vcsh`, `homeshick`. More information: <https://chezmoi.io>.

## Examples

### Setup up `chezmoi`, creating a Git repository in `~/.local/share/chezmoi`

```bash
chezmoi init
```

### Set up `chezmoi` from existing dotfiles of a Git repository

```bash
chezmoi init repository_url
```

### Start tracking one or more dotfiles

```bash
chezmoi add path/to/dotfile1 path/to/dotfile2 ...
```

### Update repository with local changes

```bash
chezmoi re-add path/to/dotfile1 path/to/dotfile2 ...
```

### Edit the source state of a tracked dotfile

```bash
chezmoi edit path/to/dotfile_or_symlink
```

### See pending changes

```bash
chezmoi diff
```

### Apply the changes

```bash
chezmoi -v apply
```

### Pull changes from a remote repository and apply them

```bash
chezmoi update
```
