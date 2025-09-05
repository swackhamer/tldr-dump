# set-nodeversion

> Set the default Node.js version for `ps-nvm`. Part of `ps-nvm` and can only be run under PowerShell. More information: <https://github.com/aaronpowell/ps-nvm>.

## Examples

### Use a specific version of Node.js in the current PowerShell session

```bash
Set-NodeVersion node_version
```

### Use the latest installed Node.js version 20.x

```bash
Set-NodeVersion ^20
```

### Set the default Node.js version for the current user (only applies to future PowerShell sessions)

```bash
Set-NodeVersion node_version -Persist User
```

### Set the default Node.js version for all users (must be run as Administrator/root and only applies to future PowerShell sessions)

```bash
Set-NodeVersion node_version -Persist Machine
```
