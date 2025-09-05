# elm

> Compile and run Elm source files. More information: <https://elm-lang.org>.

## Examples

### Initialize an Elm project, generates an elm.json file

```bash
elm init
```

### Start interactive Elm shell

```bash
elm repl
```

### Compile an Elm file, output the result to an `index.html` file

```bash
elm make source
```

### Compile an Elm file, output the result to a JavaScript file

```bash
elm make source --output=destination.js
```

### Start local web server that compiles Elm files on page load

```bash
elm reactor
```

### Install Elm package from <https://package.elm-lang.org>

```bash
elm install author/package
```
