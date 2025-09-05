# github-label-sync

> Synchronize GitHub labels. More information: <https://github.com/Financial-Times/github-label-sync>.

## Examples

### Synchronize labels using a local `labels.json` file

```bash
github-label-sync --access-token token repository_name
```

### Synchronize labels using a specific labels JSON file

```bash
github-label-sync --access-token token --labels url|path/to/json_file repository_name
```

### Perform a dry run instead of actually synchronizing labels

```bash
github-label-sync --access-token token --dry-run repository_name
```

### Keep labels that aren't in `labels.json`

```bash
github-label-sync --access-token token --allow-added-labels repository_name
```

### Synchronize using the `GITHUB_ACCESS_TOKEN` environment variable

```bash
github-label-sync repository_name
```
