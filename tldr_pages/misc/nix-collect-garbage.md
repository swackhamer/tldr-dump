# nix-collect-garbage

> Delete unused and unreachable nix store paths. Generations can be listed using `nix-env --list-generations`. More information: <https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>.

## Examples

### Delete all store paths unused by current generations of each profile

```bash
sudo nix-collect-garbage [-d|--delete-old]
```

### Simulate the deletion of old store paths

```bash
sudo nix-collect-garbage [-d|--delete-old] --dry-run
```

### Delete all store paths older than 30 days

```bash
sudo nix-collect-garbage --delete-older-than 30d
```
