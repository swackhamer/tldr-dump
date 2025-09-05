# stack

> Manage Haskell projects. More information: <https://github.com/commercialhaskell/stack>.

## Examples

### Create a new package

```bash
stack new package template
```

### Compile a package

```bash
stack build
```

### Run tests inside a package

```bash
stack test
```

### Compile a project and re-compile every time a file changes

```bash
stack build --file-watch
```

### Compile a project and execute a command after compilation

```bash
stack build --exec "command"
```

### Run a program and pass an argument to it

```bash
stack exec program -- argument
```
