# evil-winrm

> Windows Remote Management (WinRM) shell for pentesting. Once connected, we get a PowerShell prompt on the target host. More information: <https://github.com/Hackplayers/evil-winrm>.

## Examples

### Connect to a host

```bash
evil-winrm [-i|--ip] ip [-u|--user] user [-p|--password] password
```

### Connect to a host using pass-the-hash authentication instead of a password

```bash
evil-winrm [-i|--ip] ip [-u|--user] user [-H|--hash] nt_hash
```

### Connect to a host, specifying directories for PowerShell scripts and executables

```bash
evil-winrm [-i|--ip] ip [-u|--user] user [-p|--password] password [-s|--scripts] path/to/scripts [-e|--executables] path/to/executables
```

### Connect to a host, using SSL

```bash
evil-winrm [-i|--ip] ip [-u|--user] user [-p|--password] password [-S|--ssl] [-c|--pub-key] path/to/pubkey [-k|--priv-key] path/to/privkey
```

### Upload a file to the host

```bash
PS > upload path/to/local/file path/to/remote/file
```

### List all loaded PowerShell functions

```bash
PS > menu
```

### Load a PowerShell script from the `--scripts` directory

```bash
PS > script.ps1
```

### Invoke a binary on the host from the `--executables` directory

```bash
PS > Invoke-Binary binary.exe
```
