# gh-repo

> Work with GitHub repositories. More information: <https://cli.github.com/manual/gh_repo>.

## Examples

### Create a new repository (if the repository name is not set, the default name will be the name of the current directory)

```bash
gh repo create name
```

### Clone a repository

```bash
gh repo clone owner/repository
```

### Fork and clone a repository

```bash
gh repo fork owner/repository --clone
```

### View a repository in the default web browser

```bash
gh repo view repository [-w|--web]
```

### List repositories owned by a specific user or organization (if the owner is not set, the default owner will be the currently logged in user)

```bash
gh repo list owner
```

### List only non-forks repositories and limit the number of repositories to list (default: 30)

```bash
gh repo list owner --source [-L|--limit] limit
```

### List repositories with a specific primary coding language

```bash
gh repo list owner [-l|--language] language_name
```
