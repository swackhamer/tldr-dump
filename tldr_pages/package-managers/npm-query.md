# npm-query

> Print an array of dependency objects using CSS-like selectors. More information: <https://docs.npmjs.com/cli/npm-query>.

## Examples

### Print direct dependencies

```bash
npm query ':root > *'
```

### Print all direct production/development dependencies

```bash
npm query ':root > .prod|dev'
```

### Print dependencies with a specific name

```bash
npm query '#package'
```

### Print dependencies with a specific name and within a semantic versioning range

```bash
npm query '#package@semantic_version'
```

### Print dependencies which have no dependencies

```bash
npm query ':empty'
```

### Find all dependencies with postinstall scripts and uninstall them

```bash
npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' [-r|--raw-output] | xargs -I _ npm uninstall _
```

### Find all Git dependencies and print which application requires them

```bash
npm query ":type(git)" | jq 'map(.name)' | xargs -I _ npm why _
```
