# git-replace

> Create, list, and delete refs to replace objects. More information: <https://git-scm.com/docs/git-replace>.

## Examples

### Replace any commit with a different one, leaving other commits unchanged

```bash
git replace object replacement
```

### Delete existing replace refs for the given objects

```bash
git replace [-d|--delete] object
```

### Edit an object's content interactively

```bash
git replace --edit object
```
