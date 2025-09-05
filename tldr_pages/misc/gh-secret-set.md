# gh-secret-set

> Create or update GitHub secrets. More information: <https://cli.github.com/manual/gh_secret_set>.

## Examples

### Set a secret for the current repository (user will be prompted for the value)

```bash
gh secret set name
```

### Set a secret from a file for the current repository

```bash
gh secret set name < path/to/file
```

### Set a secret for a specific repository

```bash
gh secret set name [-b|--body] value [-R|--repo] owner/repository
```

### Set an organization secret for specific repositories

```bash
gh secret set name [-o|--org] organization [-r|--repos] "repository1,repository2,..."
```

### Set an organization secret with a specific visibility

```bash
gh secret set name [-o|--org] organization [-v|--visibility] all|private|selected
```
