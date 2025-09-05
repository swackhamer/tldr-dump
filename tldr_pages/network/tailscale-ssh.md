# tailscale-ssh

> SSH to a Tailscale machine (Linux Only). More information: <https://tailscale.com/kb/1193/tailscale-ssh>.

## Examples

### Advertise/Disable SSH on the host

```bash
tailscale up --ssh=true|false
```

### SSH to a specific host which has Tailscale-SSH enabled

```bash
tailscale ssh username@host
```
