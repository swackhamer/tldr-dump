# nix-search

> Search for packages in a Nix flake. See also: `nix flake` for information about flakes. More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-search.html>.

## Examples

### Search `nixpkgs` for a package based on its name or description

```bash
nix search nixpkgs search_term
```

### Show description of a package from nixpkgs

```bash
nix search nixpkgs#pkg
```

### Show all packages available from a flake on github

```bash
nix search github:owner/repo
```
