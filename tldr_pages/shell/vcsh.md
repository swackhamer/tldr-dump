# vcsh

> Version Control System for the home directory using Git repositories. See also: `chezmoi`, `stow`, `tuckr`, `homeshick`. More information: <https://github.com/RichiH/vcsh>.

## Examples

### Initialize an (empty) repository

```bash
vcsh init repository_name
```

### Clone a repository into a custom directory name

```bash
vcsh clone git_url repository_name
```

### List all managed repositories

```bash
vcsh list
```

### Execute a Git command on a managed repository

```bash
vcsh repository_name git_command
```

### Push/pull all managed repositories to/from remotes

```bash
vcsh push|pull
```

### Write a custom `.gitignore` file for a managed repository

```bash
vcsh write-gitignore repository_name
```
