# tailscale

> A private WireGuard network service. Some subcommands such as `up` have their own usage documentation. More information: <https://tailscale.com/kb/1080/cli>.

## Examples

### Allow the current user to operate on the Tailscale daemon

```bash
sudo tailscale set --operator $USER
```

### Connect to Tailscale

```bash
tailscale up
```

### Disconnect from Tailscale

```bash
tailscale down
```

### Display all devices connected to Tailscale (with their IP addresses)

```bash
tailscale status
```

### Ping a peer node at the Tailscale layer and display which route it took for each response

```bash
tailscale ping ip|hostname
```

### Analyze the local network conditions and display the result

```bash
tailscale netcheck
```

### Start a web server for controlling the Tailscale daemon

```bash
tailscale web
```

### Display a shareable identifier to help diagnose issues

```bash
tailscale bugreport
```
