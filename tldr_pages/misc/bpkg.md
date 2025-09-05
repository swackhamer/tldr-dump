# bpkg

> A package manager for Bash scripts. More information: <https://github.com/bpkg/bpkg>.

## Examples

### Update the local index

```bash
bpkg update
```

### Install a package globally

```bash
bpkg install --global package
```

### Install a package in a subdirectory of the current directory

```bash
bpkg install package
```

### Install a specific version of a package globally

```bash
bpkg install package@version -g
```

### Show details about a specific package

```bash
bpkg show package
```

### Run a command, optionally specifying its arguments

```bash
bpkg run command argument1 argument2 ...
```
