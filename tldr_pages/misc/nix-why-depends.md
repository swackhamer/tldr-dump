# nix-why-depends

> Show why a package depends on another package. More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>.

## Examples

### Show why the currently running NixOS system requires a certain store path

```bash
nix why-depends /run/current-system /nix/store/checksum-package-version.ext
```

### Show why a package from nixpkgs requires another package as a _build-time_ dependency

```bash
nix why-depends --derivation nixpkgs#dependent nixpkgs#dependency
```
