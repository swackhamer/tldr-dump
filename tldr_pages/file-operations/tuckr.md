# tuckr

> Dotfile manager written in Rust. See also: `chezmoi`, `vcsh`, `homeshick`, `stow`. More information: <https://github.com/RaphGL/Tuckr>.

## Examples

### Check dotfile status

```bash
tuckr status
```

### Add all dotfiles to system

```bash
tuckr add \*
```

### Add all dotfiles except specified programs

```bash
tuckr add \* -e program1,program2
```

### Remove all dotfiles from the system

```bash
tuckr rm \*
```

### Add a program dotfile and run its setup script

```bash
tuckr set program
```
