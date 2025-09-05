# git-filter-repo

> A versatile tool for rewriting Git history. See also: `bfg`. More information: <https://github.com/newren/git-filter-repo>.

## Examples

### Replace a sensitive string in all files

```bash
git filter-repo --replace-text <(echo 'find==>replacement')
```

### Extract a single folder, keeping history

```bash
git filter-repo --path path/to/folder
```

### Remove a single folder, keeping history

```bash
git filter-repo --path path/to/folder --invert-paths
```
