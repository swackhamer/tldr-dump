# pnpm-outdated

> Check for outdated packages. The check can be limited to a subset of the installed packages by providing arguments (patterns are supported). More information: <https://pnpm.io/cli/outdated>.

## Examples

### Check for outdated packages

```bash
pnpm outdated
```

### Check for outdated dependencies found in every workspace package

```bash
pnpm outdated [-r|--recursive]
```

### Filter outdated packages using a package selector

```bash
pnpm outdated --filter package_selector
```

### List outdated packages globally

```bash
pnpm outdated [-g|--global]
```

### Print details of outdated packages

```bash
pnpm outdated --long
```

### Print outdated dependencies in a specific format

```bash
pnpm outdated --format format
```

### Print only versions that satisfy specifications in `package.json`

```bash
pnpm outdated --compatible
```

### Check only outdated dev dependencies

```bash
pnpm outdated [-D|--dev]
```
