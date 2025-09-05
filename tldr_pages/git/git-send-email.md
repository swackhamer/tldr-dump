# git-send-email

> Send a collection of patches as emails. Patches can be specified as files, directions, or a revision list. More information: <https://git-scm.com/docs/git-send-email>.

## Examples

### Send the last commit in the current branch interactively

```bash
git send-email -1
```

### Send a given commit

```bash
git send-email -1 commit
```

### Send multiple (e.g. 10) commits in the current branch

```bash
git send-email -10
```

### Send an introductory email message for the patch series

```bash
git send-email -number_of_commits --compose
```

### Review and edit the email message for each patch you're about to send

```bash
git send-email -number_of_commits --annotate
```
