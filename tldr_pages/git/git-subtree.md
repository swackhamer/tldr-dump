# git-subtree

> Manage project dependencies as subprojects. More information: <https://manned.org/git-subtree>.

## Examples

### Add a Git repository as a subtree

```bash
git subtree add [-P|--prefix] path/to/directory/ --squash repository_url branch_name
```

### Update subtree repository to its latest commit

```bash
git subtree pull [-P|--prefix] path/to/directory/ repository_url branch_name
```

### Merge recent changes up to the latest subtree commit into the subtree

```bash
git subtree merge [-P|--prefix] path/to/directory/ --squash repository_url branch_name
```

### Push commits to a subtree repository

```bash
git subtree push [-P|--prefix] path/to/directory/ repository_url branch_name
```

### Extract a new project history from the history of a subtree

```bash
git subtree split [-P|--prefix] path/to/directory/ repository_url [-b|--branch] branch_name
```
