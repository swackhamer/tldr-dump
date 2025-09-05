# lerna

> Manage JavaScript projects with multiple packages. More information: <https://lerna.js.org>.

## Examples

### Initialize project files (`lerna.json`, `package.json`, `.git`, etc.)

```bash
lerna init
```

### Install all external dependencies of each package and symlink together local dependencies

```bash
lerna bootstrap
```

### Run a specific script for every package that contains it in its `package.json`

```bash
lerna run script
```

### Execute an arbitrary shell command in every package

```bash
lerna exec -- ls
```

### Publish all packages that have changed since the last release

```bash
lerna publish
```
