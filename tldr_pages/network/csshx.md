# csshx

> Cluster SSH tool for macOS. More information: <https://github.com/brockgr/csshx>.

## Examples

### Connect to multiple hosts

```bash
csshX hostname1 hostname2
```

### Connect to multiple hosts with a given SSH key

```bash
csshX user@hostname1 user@hostname2 --ssh_args "-i path/to/key_file.pem"
```

### Connect to a pre-defined cluster from `/etc/clusters`

```bash
csshX cluster1
```
