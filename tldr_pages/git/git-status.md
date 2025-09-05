# git-status

> Show the changes to files in a Git repository. List changed, added and deleted files compared to the currently checked-out commit. More information: <https://git-scm.com/docs/git-status>.

## Examples

### Show changed files which are not yet added for commit

```bash
git status
```

### Give output in short format

```bash
git status [-s|--short]
```

### Show verbose information on changes in both the staging area and working directory

```bash
git status [-vv|--verbose --verbose]
```

### Show the branch and tracking info

```bash
git status [-b|--branch]
```

### Show output in short format along with branch info

```bash
git status [-sb|--short --branch]
```

### Show the number of entries currently stashed away

```bash
git status --show-stash
```

### Don't show untracked files in the output

```bash
git status [-uno|--untracked-files=no]
```
