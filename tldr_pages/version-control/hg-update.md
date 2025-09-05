# hg-update

> Update the working directory to a specified changeset. More information: <https://www.mercurial-scm.org/help/commands/update>.

## Examples

### Update to the tip of the current branch

```bash
hg update
```

### Update to the specified revision

```bash
hg update [-r|--rev] revision
```

### Update and discard uncommitted changes

```bash
hg update [-C|--clean]
```

### Update to the last commit matching a specified date

```bash
hg update [-d|--date] dd-mm-yyyy
```
