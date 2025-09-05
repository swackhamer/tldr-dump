# ssh-keyscan

> Get the public SSH keys of remote hosts. More information: <https://man.openbsd.org/ssh-keyscan>.

## Examples

### Retrieve all public SSH keys of a remote host

```bash
ssh-keyscan hostname
```

### Retrieve all public SSH keys of a remote host listening on a specific port

```bash
ssh-keyscan -p port hostname
```

### Retrieve certain types of public SSH keys of a remote host

```bash
ssh-keyscan -t rsa,dsa,ecdsa,ed25519 hostname
```

### Manually update the SSH known_hosts file with the fingerprint of a given host

```bash
ssh-keyscan -H hostname >> ~/.ssh/known_hosts
```
