# nix-store.2

> Manipulate or query the Nix store. See also: `nix store.3`. More information: <https://nixos.org/manual/nix/stable/command-ref/nix-store.html>.

## Examples

### Collect garbage, such as removing unused paths

```bash
nix-store --gc
```

### Hard-link identical files together to reduce space usage

```bash
nix-store --optimise
```

### Delete a specific store path (must be unused)

```bash
nix-store --delete /nix/store/checksum-package-version.ext
```

### Show all dependencies of a store path (package), in a tree format

```bash
nix-store [-q|--query] --tree /nix/store/checksum-package-version.ext
```

### Calculate the total size of a certain store path with all the dependencies

```bash
du [-cLsh|--total --dereference --summarize --human-readable] $(nix-store [-q|--query] --references /nix/store/checksum-package-version.ext)
```

### Show all dependents of a particular store path

```bash
nix-store [-q|--query] --referrers /nix/store/checksum-package-version.ext
```
