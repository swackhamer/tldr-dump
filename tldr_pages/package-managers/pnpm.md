# pnpm

> Fast, disk space efficient package manager for Node.js. Manage Node.js projects and their module dependencies. More information: <https://pnpm.io/pnpm-cli>.

## Examples

### Create a `package.json` file

```bash
pnpm init
```

### Download all the packages listed as dependencies in `package.json`

```bash
pnpm install
```

### Download a specific version of a package and add it to the list of dependencies in `package.json`

```bash
pnpm add module_name@version
```

### Download a package and add it to the list of dev dependencies in `package.json`

```bash
pnpm add [-D|--save-dev] module_name
```

### Download a package and install it globally

```bash
pnpm add [-g|--global] module_name
```

### Uninstall a package and remove it from the list of dependencies in `package.json`

```bash
pnpm remove module_name
```

### Print a tree of locally installed modules

```bash
pnpm list
```

### List top-level globally installed modules

```bash
pnpm list [-g|--global] --depth 0
```
