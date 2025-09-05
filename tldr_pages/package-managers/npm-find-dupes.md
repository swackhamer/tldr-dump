# npm-find-dupes

> Identify duplicate dependencies in `node_modules`. More information: <https://docs.npmjs.com/cli/npm-find-dupes>.

## Examples

### List all duplicate packages within `node_modules`

```bash
npm find-dupes
```

### Include `devDependencies` in duplicate detection

```bash
npm find-dupes --include dev
```

### List all duplicate instances of a specific package in `node-modules`

```bash
npm find-dupes package_name
```

### Exclude optional dependencies from duplicate detection

```bash
npm find-dupes --omit optional
```

### Set the logging level for output

```bash
npm find-dupes --loglevel silent|error|warn|info|verbose
```

### Output duplicate information in JSON format

```bash
npm find-dupes --json
```

### Limit duplicate search to specific scopes

```bash
npm find-dupes --scope @scope1,@scope2
```

### Exclude specific scopes from duplicate detection

```bash
npm find-dupes --omit-scope @scope1,@scope2
```
