# git-cherry

> Find commits that have yet to be applied upstream. More information: <https://git-scm.com/docs/git-cherry>.

## Examples

### Show commits (and their messages) with equivalent commits upstream

```bash
git cherry [-v|--verbose]
```

### Specify a different upstream and topic branch

```bash
git cherry origin topic
```

### Limit commits to those within a given limit

```bash
git cherry origin topic base
```
