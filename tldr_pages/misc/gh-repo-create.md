# gh-repo-create

> Create a new GitHub repository. More information: <https://cli.github.com/manual/gh_repo_create>.

## Examples

### Create a new repository interactively

```bash
gh repo create
```

### Create a new repository with a specified name and description

```bash
gh repo create repo_name [-d|--description] "repo_description"
```

### Create a private repository from the current directory

```bash
gh repo create [-s|--source] . --private
```

### Clone the new repository locally after creation

```bash
gh repo create repo_name [-c|--clone]
```

### Push the current directory to a new GitHub repository

```bash
gh repo create [-s|--source] . --public
```
