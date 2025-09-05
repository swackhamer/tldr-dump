# nix-shell.2

> Start an interactive shell based on a Nix expression. See also: `nix shell.3`. More information: <https://nixos.org/manual/nix/stable/command-ref/nix-shell.html>.

## Examples

### Start with nix expression in `shell.nix` or `default.nix` in the current directory

```bash
nix-shell
```

### Run shell command in non-interactive shell and exit

```bash
nix-shell --run "command argument1 argument2 ..."
```

### Start with expression in `default.nix` in the current directory

```bash
nix-shell default.nix
```

### Start with packages loaded from nixpkgs

```bash
nix-shell [-p|--packages] package1 package2 ...
```

### Start with packages loaded from specific nixpkgs revision

```bash
nix-shell [-p|--packages] package1 package2 ... [-I|--include] nixpkgs=https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz
```

### Evaluate rest of file in specific interpreter, for use in `#!-scripts` (see <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>)

```bash
nix-shell -i interpreter [-p|--packages] package1 package2 ...
```
