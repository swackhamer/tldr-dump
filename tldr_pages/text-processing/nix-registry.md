# nix-registry

> Manage a Nix flake registry. See also: `nix flake` for information about flakes. More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-registry.html>.

## Examples

### Pin the `nixpkgs` revision to the current version of the upstream repository

```bash
nix registry pin nixpkgs
```

### Pin an entry to the latest version of the branch, or a particular reivision of a GitHub repository

```bash
nix registry pin entry github:owner/repo/branch_or_revision
```

### Add a new entry that always points to the latest version of a GitHub repository, updating automatically

```bash
nix registry add entry github:owner/repo
```

### Remove a registry entry

```bash
nix registry remove entry
```

### See documentation about what Nix flake registries are

```bash
nix registry --help
```
