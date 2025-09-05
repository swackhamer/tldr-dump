# nix-shell.3

> Start a shell in which the specified packages are available. See also: `nix-shell` for setting up development environments, `nix flake` for information about flakes. More information: <https://manned.org/nix3-shell>.

## Examples

### Start an interactive shell with some packages from `nixpkgs`

```bash
nix shell nixpkgs#pkg1 nixpkgs#packageSet.pkg2 ...
```

### Start a shell providing a package from an older version of `nixpkgs` (21.05)

```bash
nix shell nixpkgs/nixos-21.05#pkg
```

### Start a shell with the "default package" from a flake in the current directory, printing build logs if any builds happen

```bash
nix shell -L
```

### Start a shell with a package from a flake on GitHub

```bash
nix shell github:owner/repo#pkg
```

### Run a command in a shell with a package

```bash
nix shell nixpkgs#pkg -c some-cmd --someflag 'Some other arguments'
```
