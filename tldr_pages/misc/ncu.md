# ncu

> Find newer versions of package dependencies and check outdated npm packages locally or globally. `ncu` only updates dependency versions in `package.json`. To install the new versions, run `npm install` afterwards. More information: <https://github.com/raineorshine/npm-check-updates>.

## Examples

### List outdated dependencies in the current directory

```bash
ncu
```

### List outdated global `npm` packages

```bash
ncu --global
```

### Upgrade all dependencies in the current directory

```bash
ncu --upgrade
```

### Interactively upgrade dependencies in the current directory

```bash
ncu --interactive
```

### List outdated dependencies up to the highest minor version

```bash
ncu --target minor
```

### List outdated dependencies that match a keyword or `regex`

```bash
ncu --filter keyword|/regex/
```

### List only a specific section of outdated dependencies

```bash
ncu --dep dev|optional|peer|prod|packageManager
```

### Display help

```bash
ncu --help
```
