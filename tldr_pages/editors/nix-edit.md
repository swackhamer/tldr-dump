# nix-edit

> Open the Nix expression of a Nix package in $EDITOR. More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-edit.html>.

## Examples

### Open the source of the Nix expression of a package from nixpkgs in your `$EDITOR`

```bash
nix edit nixpkgs#pkg
```

### Dump the source of a package to `stdout`

```bash
EDITOR=cat nix edit nixpkgs#pkg
```
