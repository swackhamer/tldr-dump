# piactl

> The tool for Private Internet Access, a commercial VPN provider. More information: <https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-part-1>.

## Examples

### Log in to Private Internet Access

```bash
piactl login path/to/login_file
```

### Connect to Private Internet Access

```bash
piactl connect
```

### Disconnect from Private Internet Access

```bash
piactl disconnect
```

### Enable or disable the Private Internet Access daemon in the background

```bash
piactl background enable|disable
```

### List all available VPN regions

```bash
piactl get regions
```

### Display the current VPN region

```bash
piactl get region
```

### Set your VPN region

```bash
piactl set region region
```

### Log out of Private Internet Access

```bash
piactl logout
```
