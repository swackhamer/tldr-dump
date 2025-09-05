# wapm

> The WebAssembly package manager. More information: <https://wapm.io/help/reference>.

## Examples

### Interactively create a new `wapm.toml` file

```bash
wapm init
```

### Download all the packages listed as dependencies in `wapm.toml`

```bash
wapm install
```

### Download a specific version of a package and add it to the list of dependencies in `wapm.toml`

```bash
wapm install package@version
```

### Download a package and install it globally

```bash
wapm install --global package
```

### Uninstall a package and remove it from the list of dependencies in `wapm.toml`

```bash
wapm uninstall package
```

### Print a tree of locally installed dependencies

```bash
wapm list
```

### List top-level globally installed packages

```bash
wapm list --global
```

### Execute a package command using the Wasmer runtime

```bash
wapm run command_name arguments
```
