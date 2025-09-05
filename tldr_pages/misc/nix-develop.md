# nix-develop

> Run a Bash shell that provides the build environment of a derivation. More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>.

## Examples

### Start a shell with all dependencies of a package from nixpkgs available

```bash
nix develop nixpkgs#pkg
```

### Start a development shell for the default package in a flake in the current directory

```bash
nix develop
```

### In that shell, configure and build the sources

```bash
configurePhase; buildPhase
```
