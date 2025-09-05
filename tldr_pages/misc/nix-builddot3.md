# nix-build.3

> Build a Nix expression (downloading from the cache when possible). See also: `nix-build` for information about traditional Nix builds from expressions, `nix flake` for information about flakes. More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-build.html>.

## Examples

### Build a package from nixpkgs, symlinking the result to `./result`

```bash
nix build nixpkgs#pkg
```

### Build a package from a flake in the current directory, showing the build logs in the process

```bash
nix build -L .#pkg
```

### Build the default package from a flake in some directory

```bash
nix build ./path/to/directory
```

### Build a package without making the `result` symlink, instead printing the store path to the `stdout`

```bash
nix build --no-link --print-out-paths
```
