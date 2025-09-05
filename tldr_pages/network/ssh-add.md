# ssh-add

> Manage loaded SSH keys in the `ssh-agent`. Ensure that `ssh-agent` is up and running for the keys to be loaded in it. More information: <https://man.openbsd.org/ssh-add>.

## Examples

### Add the default SSH keys in `~/.ssh` to the ssh-agent

```bash
ssh-add
```

### Add a specific key to the ssh-agent

```bash
ssh-add path/to/private_key
```

### List fingerprints of currently loaded keys

```bash
ssh-add -l
```

### Delete a key from the ssh-agent

```bash
ssh-add -d path/to/private_key
```

### Delete all currently loaded keys from the ssh-agent

```bash
ssh-add -D
```

### Add a key to the ssh-agent and the keychain

```bash
ssh-add -K path/to/private_key
```
