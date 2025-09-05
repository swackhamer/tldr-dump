# git

> Distributed version control system. Some subcommands such as `commit`, `add`, `branch`, `switch`, `push`, etc. have their own usage documentation. More information: <https://git-scm.com/docs/git>.

## Examples

### Create an empty Git repository

```bash
git init
```

### Clone a remote Git repository from the internet

```bash
git clone https://example.com/repo.git
```

### View the status of the local repository

```bash
git status
```

### Stage all changes for a commit

```bash
git add [-A|--all]
```

### Commit changes to version history

```bash
git commit [-m|--message] message_text
```

### Push local commits to a remote repository

```bash
git push
```

### Pull any changes made to a remote

```bash
git pull
```

### Reset everything the way it was in the latest commit

```bash
git reset --hard; git clean [-f|--force]
```
