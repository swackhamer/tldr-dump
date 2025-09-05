# npm-ls

> Print installed packages to `stdout`. More information: <https://docs.npmjs.com/cli/npm-ls>.

## Examples

### Print all versions of direct dependencies to `stdout`

```bash
npm ls
```

### Print all installed packages including peer dependencies

```bash
npm ls [-a|--all]
```

### Print dependencies with extended information

```bash
npm ls [-l|--long]
```

### Print dependencies in parseable format

```bash
npm ls [-p|--parseable]
```

### Print dependencies in JSON format

```bash
npm ls --json
```
