# tailscale-file

> Send files across connected devices on a Tailscale network. It currently does not support sending files to devices owned by other users even on the same Tailscale network. More information: <https://tailscale.com/kb/1106/taildrop/>.

## Examples

### Store files that were sent to the current node into a specific directory

```bash
tailscale file get path/to/directory
```
