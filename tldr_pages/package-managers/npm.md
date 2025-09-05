# npm

> JavaScript and Node.js package manager. Manage Node.js projects and their module dependencies. More information: <https://docs.npmjs.com/cli/npm>.

## Examples

### Create a `package.json` file with default values (omit `--yes` to do it interactively)

```bash
npm init [-y|--yes]
```

### Download all the packages listed as dependencies in `package.json`

```bash
npm [i|install]
```

### Download a specific version of a package and add it to the list of dependencies in `package.json`

```bash
npm [i|install] package_name@version
```

### Download the latest version of a package and add it to the list of dev dependencies in `package.json`

```bash
npm [i|install] package_name [-D|--save-dev]
```

### Download the latest version of a package and install it globally

```bash
npm [i|install] [-g|--global] package_name
```

### Uninstall a package and remove it from the list of dependencies in `package.json`

```bash
npm [r|uninstall] package_name
```

### List all locally installed dependencies

```bash
npm [ls|list]
```

### List all top-level globally installed packages

```bash
npm [ls|list] [-g|--global] --depth 0
```
