# git-show-branch

> Show branches and their commits. More information: <https://git-scm.com/docs/git-show-branch>.

## Examples

### Show a summary of the latest commit on a branch

```bash
git show-branch branch_name|ref|commit
```

### Compare commits in the history of multiple commits or branches

```bash
git show-branch branch_name1|ref1|commit1 branch_name2|ref2|commit2 ...
```

### Compare all remote tracking branches

```bash
git show-branch [-r|--remotes]
```

### Compare both local and remote tracking branches

```bash
git show-branch [-a|--all]
```

### List the latest commits in all branches

```bash
git show-branch [-a|--all] --list
```

### Compare a given branch with the current branch

```bash
git show-branch --current commit|branch_name|ref
```

### Display the commit name instead of the relative name

```bash
git show-branch --sha1-name --current current|branch_name|ref
```

### Keep going a given number of commits past the common ancestor

```bash
git show-branch --more 5 branch_name1|ref1|commit1 branch_name2|ref2|commit2 ...
```
