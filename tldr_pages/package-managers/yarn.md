# yarn

> JavaScript and Node.js package manager alternative. More information: <https://yarnpkg.com/cli>.

## Examples

### Install a module globally

```bash
yarn global add module_name
```

### Install all dependencies referenced in the `package.json` file (the `install` is optional)

```bash
yarn install
```

### Install a module and save it as a dependency to the `package.json` file (add `--dev` to save as a dev dependency)

```bash
yarn add module_name@version
```

### Uninstall a module and remove it from the `package.json` file

```bash
yarn remove module_name
```

### Interactively create a `package.json` file

```bash
yarn init
```

### Identify whether a module is a dependency and list other modules that depend upon it

```bash
yarn why module_name
```
