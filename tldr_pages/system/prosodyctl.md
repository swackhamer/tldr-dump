# prosodyctl

> The control tool for the Prosody XMPP server. Note: Process management through `prosodyctl` is discouraged. Instead, use the tools provided by your system (e.g. `systemctl`). More information: <https://prosody.im/doc/prosodyctl>.

## Examples

### Show the status of the Prosody server

```bash
sudo prosodyctl status
```

### Reload the server's configuration files

```bash
sudo prosodyctl reload
```

### Add a user to the Prosody XMPP server

```bash
sudo prosodyctl adduser user@example.com
```

### Set a user's password

```bash
sudo prosodyctl passwd user@example.com
```

### Permanently delete a user

```bash
sudo prosodyctl deluser user@example.com
```
