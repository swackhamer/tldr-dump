# coffee

> Execute CoffeeScript scripts or compiles them into JavaScript. More information: <https://coffeescript.org#cli>.

## Examples

### Run a script

```bash
coffee path/to/file.coffee
```

### Compile to JavaScript and save to a file with the same name

```bash
coffee --compile path/to/file.coffee
```

### Compile to JavaScript and save to a given output file

```bash
coffee --compile path/to/file.coffee --output path/to/file.js
```

### Start a REPL (interactive shell)

```bash
coffee --interactive
```

### Watch script for changes and re-run script

```bash
coffee --watch path/to/file.coffee
```
