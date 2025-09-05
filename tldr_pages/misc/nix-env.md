# nix-env

> Manipulate or query Nix user environments. More information: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

## Examples

### List all installed packages

```bash
nix-env [-q|--query]
```

### Query installed packages

```bash
nix-env [-q|--query] search_term
```

### Query available packages

```bash
nix-env [-qa|--query --available] search_term
```

### Install package

```bash
nix-env [-iA|--install --attr] nixpkgs.pkg_name
```

### Install a package from a URL

```bash
nix-env [-i|--install] pkg_name [-f|--file] example.com
```

### Uninstall package

```bash
nix-env [-e|--uninstall] pkg_name
```

### Upgrade one package

```bash
nix-env [-u|--upgrade] pkg_name
```

### Upgrade all packages

```bash
nix-env [-u|--upgrade]
```
