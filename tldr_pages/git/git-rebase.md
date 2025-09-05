# git-rebase

> Reapply commits from one branch on top of another branch. Commonly used to "move" an entire branch to another base, creating copies of the commits in the new location. More information: <https://git-scm.com/docs/git-rebase>.

## Examples

### Rebase the current branch on top of another specified branch

```bash
git rebase new_base_branch
```

### Start an interactive rebase, which allows the commits to be reordered, omitted, combined or modified

```bash
git rebase [-i|--interactive] target_base_branch_or_commit_hash
```

### Continue a rebase that was interrupted by a merge failure, after editing conflicting files

```bash
git rebase --continue
```

### Continue a rebase that was paused due to merge conflicts, by skipping the conflicted commit

```bash
git rebase --skip
```

### Abort a rebase in progress (e.g. if it is interrupted by a merge conflict)

```bash
git rebase --abort
```

### Move part of the current branch onto a new base, providing the old base to start from

```bash
git rebase --onto new_base old_base
```

### Reapply the last 5 commits in-place, stopping to allow them to be reordered, omitted, combined or modified

```bash
git rebase [-i|--interactive] HEAD~5
```

### Auto-resolve any conflicts by favoring the working branch version (`theirs` keyword has reversed meaning in this case)

```bash
git rebase [-X|--strategy-option] theirs branch_name
```
