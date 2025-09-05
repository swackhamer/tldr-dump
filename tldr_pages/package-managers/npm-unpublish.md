# npm-unpublish

> Remove a package from the npm registry. More information: <https://docs.npmjs.com/cli/npm-unpublish>.

## Examples

### Unpublish a specific package version

```bash
npm unpublish package_name@version
```

### Unpublish the entire package

```bash
npm unpublish package_name [-f|--force]
```

### Unpublish a package that is scoped

```bash
npm unpublish @scope/package_name
```

### Specify a timeout period before unpublishing

```bash
npm unpublish package_name --timeout time_in_milliseconds
```

### To prevent accidental unpublishing, use the `--dry-run` flag to see what would be unpublished

```bash
npm unpublish package_name --dry-run
```
