# git-stash

> Stash local Git changes in a temporary area. More information: <https://git-scm.com/docs/git-stash>.

## Examples

### Stash current changes with a message, except new (untracked) files

```bash
git stash push [-m|--message] optional_stash_message
```

### Stash current changes, including new untracked files

```bash
git stash [-u|--include-untracked]
```

### Interactively select parts of changed files for stashing

```bash
git stash [-p|--patch]
```

### List all stashes (shows stash name, related branch and message)

```bash
git stash list
```

### Show the changes as a patch between the stash (default is `stash@{0}`) and the commit back when stash entry was first created

```bash
git stash show [-p|--patch] stash@{0}
```

### Apply a stash (default is the latest, named stash@{0})

```bash
git stash apply optional_stash_name_or_commit
```

### Drop or apply a stash (default is stash@{0}) and remove it from the stash list if applying doesn't cause conflicts

```bash
git stash pop optional_stash_name
```

### Drop all stashes

```bash
git stash clear
```
