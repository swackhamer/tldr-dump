# cabal

> Interface to the Haskell package infrastructure (Cabal). Manage Haskell projects and Cabal packages from the Hackage package repository. More information: <https://cabal.readthedocs.io/en/latest/getting-started.html>.

## Examples

### Search and list packages from Hackage

```bash
cabal list search_string
```

### Show information about a package

```bash
cabal info package
```

### Download and install a package

```bash
cabal install package
```

### Create a new Haskell project in the current directory

```bash
cabal init
```

### Build the project in the current directory

```bash
cabal build
```

### Run tests of the project in the current directory

```bash
cabal test
```
