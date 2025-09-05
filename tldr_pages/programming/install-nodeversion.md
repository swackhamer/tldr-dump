# install-nodeversion

> Install Node.js runtime versions for `ps-nvm`. This command is part of `ps-nvm` and can only be run under PowerShell. More information: <https://github.com/aaronpowell/ps-nvm>.

## Examples

### Install a specific Node.js version

```bash
Install-NodeVersion node_version
```

### Install multiple Node.js versions

```bash
Install-NodeVersion node_version1 , node_version2 , ...
```

### Install latest available version of Node.js 20

```bash
Install-NodeVersion ^20
```

### Install the x86 (x86 32-bit) / x64 (x86 64-bit) / arm64 (ARM 64-bit) version of Node.js

```bash
Install-NodeVersion node_version -Architecture x86|x64|arm64
```

### Use a HTTP proxy to download Node.js

```bash
Install-NodeVersion node-version -Proxy http://example.com
```
