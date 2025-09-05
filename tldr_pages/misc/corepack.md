# corepack

> Zero-runtime-dependency package acting as bridge between Node projects and their package managers. More information: <https://github.com/nodejs/corepack>.

## Examples

### Add the Corepack shims to the Node.js installation directory to make them available as global commands

```bash
corepack enable
```

### Add the Corepack shims to a specific directory

```bash
corepack enable --install-directory path/to/directory
```

### Remove the Corepack shims from the Node.js installation directory

```bash
corepack disable
```

### Prepare a specific package manager

```bash
corepack prepare package_manager@version --activate
```

### Prepare the package manager configured for the project in the current path

```bash
corepack prepare
```

### Use a package manager without installing it as a global command

```bash
corepack npm|pnpm|yarn package_manager_arguments
```

### Install a package manager from the specified archive

```bash
corepack hydrate path/to/corepack.tgz
```

### Display help for a subcommand

```bash
corepack subcommand --help
```
