# jj-git-init

> Create a new Git backed Jujutsu repo. Note: Unless `--colocate` is used, it is not a valid Git repository and `git` commands can't be used on it. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-init>.

## Examples

### Create a new Git backed repo in the current directory

```bash
jj git init
```

### Create a new Git backed repo in the given directory

```bash
jj git init path/to/directory
```

### Initialize the Jujutsu repository as a valid Git repository (allowing the use of both `jj` and `git` commands in the same directory)

```bash
jj git init --colocate
```

### Initialize the Jujutsu repository backed by an existing Git repository

```bash
jj git init --git-repo git_repo
```
