# nix-build.2

> Build a Nix expression. See also: `nix build.3`. More information: <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

## Examples

### Build a Nix expression

```bash
nix-build '<nixpkgs>' [-A|--attr] firefox
```

### Build a sandboxed Nix expression (on non-NixOS)

```bash
nix-build '<nixpkgs>' [-A|--attr] firefox --option sandbox true
```
