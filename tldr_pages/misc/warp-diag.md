# warp-diag

> Diagnostic and feedback tool for Cloudflare's WARP service. See also: `warp-cli`. More information: <https://developers.cloudflare.com/warp-client/>.

## Examples

### Generate a Zip file with information about the system configuration and the WARP connection

```bash
warp-diag
```

### Generate a Zip file with debug information including a timestamp to the output filename

```bash
warp-diag --add-ts
```

### Save the output file under a specific directory

```bash
warp-diag --output path/to/directory
```

### Submit a new feedback to Cloudflare's WARP interactively

```bash
warp-diag feedback
```
