# git-mktree

> Build a tree object using `ls-tree` formatted text. More information: <https://git-scm.com/docs/git-mktree>.

## Examples

### Build a tree object and verify that each tree entry's hash identifies an existing object

```bash
git mktree
```

### Allow missing objects

```bash
git mktree --missing
```

### Read the NUL ([z]ero character) terminated output of the tree object (`ls-tree -z`)

```bash
git mktree -z
```

### Allow the creation of multiple tree objects

```bash
git mktree --batch
```

### Sort and build a tree from `stdin` (non-recursive `git ls-tree` output format is required)

```bash
git mktree < path/to/tree.txt
```
