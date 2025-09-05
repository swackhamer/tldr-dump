# ssh-copy-id

> Install your public key in a remote machine's authorized_keys. More information: <https://manned.org/ssh-copy-id>.

## Examples

### Copy your keys to the remote machine

```bash
ssh-copy-id username@remote_host
```

### Copy the given public key to the remote

```bash
ssh-copy-id -i path/to/certificate username@remote_host
```

### Copy the given public key to the remote with specific port

```bash
ssh-copy-id -i path/to/certificate -p port username@remote_host
```
