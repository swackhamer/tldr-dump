# mullvad

> CLI client for Mullvad VPN. See also: `fastd`, `ivpn`, `mozillavpn`, `warp-cli`. More information: <https://mullvad.net/en/help/how-use-mullvad-cli>.

## Examples

### Link your Mullvad account with the specified account number

```bash
mullvad account set account_number
```

### Enable LAN access while VPN is on

```bash
mullvad lan set allow
```

### Select a server in a specific city

```bash
mullvad relay set location se mma
```

### Select a specific server

```bash
mullvad relay set location se-mma-wg-001
```

### Establish the VPN tunnel

```bash
mullvad connect
```

### Check status of VPN tunnel

```bash
mullvad status
```

### Check the account expiration date and obtain the device name

```bash
mullvad account get
```
