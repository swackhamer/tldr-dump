# mosh

> Mobile Shell (`mosh`) is a robust and responsive replacement for SSH. `mosh` persists connections to remote servers while roaming between networks. More information: <https://manned.org/mosh>.

## Examples

### Connect to a remote server

```bash
mosh username@remote_host
```

### Connect to a remote server with a specific identity (private key)

```bash
mosh --ssh="ssh -i path/to/key_file" username@remote_host
```

### Connect to a remote server using a specific port

```bash
mosh --ssh="ssh -p 2222" username@remote_host
```

### Run a command on a remote server

```bash
mosh remote_host -- command -with -flags
```

### Select Mosh UDP port (useful when `remote_host` is behind a NAT)

```bash
mosh -p 124 username@remote_host
```

### Usage when `mosh-server` binary is outside standard path

```bash
mosh --server=path/to/mosh-server remote_host
```
