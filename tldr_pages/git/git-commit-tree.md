# git-commit-tree

> Low level utility to create commit objects. See also: `git commit`. More information: <https://git-scm.com/docs/git-commit-tree>.

## Examples

### Create a commit object with the specified message

```bash
git commit-tree tree -m "message"
```

### Create a commit object reading the message from a file (use `-` for `stdin`)

```bash
git commit-tree tree -F path/to/file
```

### Create a GPG-signed commit object

```bash
git commit-tree tree -m "message" [-S|--gpg-sign]
```

### Create a commit object with the specified parent commit object

```bash
git commit-tree tree -m "message" -p parent_commit_sha
```
