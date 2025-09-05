# zapier-scaffold

> Add a starting trigger, create, search, or resource to an integration. More information: <https://platform.zapier.com/reference/cli#scaffold>.

## Examples

### Scaffold a new trigger, create, search, or resource

```bash
zapier scaffold trigger|search|create|resource noun
```

### Specify a custom destination directory for the scaffolded files

```bash
zapier scaffold trigger|search|create|resource noun [-d|--dest]=path/to/directory
```

### Overwrite existing files when scaffolding

```bash
zapier scaffold trigger|search|create|resource noun [-f|--force]
```

### Exclude comments from the scaffolded files

```bash
zapier scaffold trigger|search|create|resource noun --no-help
```

### Show extra debugging output

```bash
zapier scaffold [-d|--debug]
```
