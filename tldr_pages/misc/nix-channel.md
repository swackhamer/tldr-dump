# nix-channel

> Manage `nix` update channels. More information: <https://nixos.wiki/wiki/Nix_channels>.

## Examples

### List current channels

```bash
nix-channel --list
```

### Add a channel

```bash
nix-channel --add https://nixos.org/channels/nixpkgs-unstable
```

### Update package list of all channels

```bash
nix-channel --update
```
