# warp-cli

> Connect, disconnect and switch modes of a connection to Cloudflare's WARP service. WARP is a VPN that encrypts traffic for privacy, security, and speed. See also: `fastd`, `ivpn`, `mozillavpn`, `mullvad`. More information: <https://developers.cloudflare.com/warp-client/>.

## Examples

### Register the current device to WARP (must be run before first connection)

```bash
warp-cli registration new
```

### Connect to WARP

```bash
warp-cli connect
```

### Disconnect from WARP

```bash
warp-cli disconnect
```

### Display the WARP connection status

```bash
warp-cli status
```

### Switch to a specific mode

```bash
warp-cli set-mode mode
```

### Display help

```bash
warp-cli help
```

### Display help for a subcommand

```bash
warp-cli help subcommand
```
