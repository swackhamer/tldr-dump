# git-check-attr

> For every pathname, list if each attribute is unspecified, set, or unset as a gitattribute on that pathname. More information: <https://git-scm.com/docs/git-check-attr>.

## Examples

### Check the values of all attributes on a file

```bash
git check-attr [-a|--all] path/to/file
```

### Check the value of a specific attribute on a file

```bash
git check-attr attribute path/to/file
```

### Check the values of all attributes on specific files

```bash
git check-attr [-a|--all] path/to/file1 path/to/file2 ...
```

### Check the value of a specific attribute on one or more files

```bash
git check-attr attribute path/to/file1 path/to/file2 ...
```
