# boot

> Build tooling for the Clojure programming language. More information: <https://github.com/boot-clj/boot>.

## Examples

### Start a REPL session either with the project or standalone

```bash
boot repl
```

### Build a single `uberjar`

```bash
boot jar
```

### Generate scaffolding for a new project based on a template

```bash
boot --dependencies boot/new new --template template_name --name project_name
```

### Build for development (if using the boot/new template)

```bash
boot dev
```

### Build for production (if using the boot/new template)

```bash
boot prod
```

### Display help for a specific task

```bash
boot task --help
```
