# fastd

> VPN daemon. Works on Layer 2 or Layer 3, supports different encryption methods, used by Freifunk. See also: `ivpn`, `mozillavpn`, `mullvad`, `warp-cli`. More information: <https://fastd.readthedocs.io/en/stable/>.

## Examples

### Start `fastd` with a specific configuration file

```bash
fastd [-c|--config] path/to/fastd.conf
```

### Start a Layer 3 VPN with an MTU of 1400, loading the rest of the configuration parameters from a file

```bash
fastd [-m|--mode] tap [-M|--mtu] 1400 [-c|--config] path/to/fastd.conf
```

### Validate a configuration file

```bash
fastd --verify-config [-c|--config] path/to/fastd.conf
```

### Generate a new keypair

```bash
fastd --generate-key
```

### Show the public key to a private key in a configuration file

```bash
fastd --show-key [-c|--config] path/to/fastd.conf
```

### Show the current version

```bash
fastd [-v|--version]
```
