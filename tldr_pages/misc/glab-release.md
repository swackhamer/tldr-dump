# glab-release

> Manage GitLab releases. More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/release/index.md>.

## Examples

### List releases in a Gitlab repository, limited to 30 items

```bash
glab release list
```

### Display information about a specific release

```bash
glab release view tag
```

### Create a new release

```bash
glab release create tag
```

### Delete a specific release

```bash
glab release delete tag
```

### Download assets from a specific release

```bash
glab release download tag
```

### Upload assets to a specific release

```bash
glab release upload tag path/to/file1 path/to/file2 ...
```
