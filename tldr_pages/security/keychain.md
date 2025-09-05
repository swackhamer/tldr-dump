# keychain

> Re-use ssh-agent and/or gpg-agent between logins. More information: <https://funtoo.org/Keychain>.

## Examples

### Check for a running ssh-agent, and start one if needed

```bash
keychain
```

### Also check for gpg-agent

```bash
keychain --agents "gpg,ssh"
```

### List signatures of all active keys

```bash
keychain --list
```

### List fingerprints of all active keys

```bash
keychain --list-fp
```

### Add a timeout for identities added to the agent, in minutes

```bash
keychain --timeout minutes
```
