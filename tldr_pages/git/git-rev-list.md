# git-rev-list

> List revisions (commits) in reverse chronological order. More information: <https://git-scm.com/docs/git-rev-list>.

## Examples

### List all commits on the current branch

```bash
git rev-list HEAD
```

### Print the latest commit that changed (add/edit/remove) a specific file on the current branch

```bash
git rev-list [-n|--max-count] 1 HEAD -- path/to/file
```

### List commits more recent than a specific date, on a specific branch

```bash
git rev-list --since "2019-12-01 00:00:00" branch_name
```

### List all merge commits on a specific commit

```bash
git rev-list --merges commit
```

### Print the number of commits since a specific tag

```bash
git rev-list tag_name..HEAD --count
```
