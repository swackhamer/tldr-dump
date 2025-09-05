# flips

> Create and apply patches for IPS and BPS files. More information: <https://github.com/Alcaro/Flips>.

## Examples

### Start Flips to create and apply patches interactively

```bash
flips
```

### Apply a patch and create a new ROM file

```bash
flips --apply patch.bps rom.smc hack.smc
```

### Create a patch from two ROMs

```bash
flips --create rom.smc hack.smc patch.bps
```
