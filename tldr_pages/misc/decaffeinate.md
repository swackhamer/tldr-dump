# decaffeinate

> Move your CoffeeScript source to modern JavaScript. More information: <https://decaffeinate-project.org>.

## Examples

### Convert a CoffeeScript file to JavaScript

```bash
decaffeinate path/to/file.coffee
```

### Convert a CoffeeScript v2 file to JavaScript

```bash
decaffeinate --use-cs2 path/to/file.coffee
```

### Convert require and `module.exports` to import and export

```bash
decaffeinate --use-js-modules path/to/file.coffee
```

### Convert a CoffeeScript, allowing named exports

```bash
decaffeinate --loose-js-modules path/to/file.coffee
```
