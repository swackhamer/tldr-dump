# gh-release

> Manage GitHub releases. More information: <https://cli.github.com/manual/gh_release>.

## Examples

### List releases in a GitHub repository, limited to 30 items

```bash
gh release list
```

### Display information about a specific release

```bash
gh release view tag
```

### Create a new release

```bash
gh release create tag
```

### Delete a specific release

```bash
gh release delete tag
```

### Download assets from a specific release

```bash
gh release download tag
```

### Upload assets to a specific release

```bash
gh release upload tag path/to/file1 path/to/file2 ...
```
