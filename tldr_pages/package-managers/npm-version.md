# npm-version

> Bump a node package version. More information: <https://docs.npmjs.com/cli/npm-version>.

## Examples

### Check current version

```bash
npm version
```

### Bump the minor version

```bash
npm version minor
```

### Set a specific version

```bash
npm version version
```

### Bump the patch version without creating a Git tag

```bash
npm version patch --no-git-tag-version
```

### Bump the major version with a custom commit message

```bash
npm version major [-m|--message] "Upgrade to %s for reasons"
```
