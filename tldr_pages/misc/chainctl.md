# chainctl

> The official CLI for Chainguard. More information: <https://edu.chainguard.dev/chainguard/chainctl/chainctl-docs/chainctl/>.

## Examples

### Authenticate to the Chainguard Platform

```bash
chainctl auth login
```

### Logout from the Chainguard Platform

```bash
chainctl auth logout
```

### Check which version you have installed

```bash
chainctl version
```

### Update to the latest version

```bash
chainctl update
```

### List images available to your account

```bash
chainctl images list
```

### List image repositories available to your account

```bash
chainctl images repos list
```

### Examine the history of an image tag in chainctl (e.g., image=python tag=3)

```bash
chainctl images history image:tag
```

### List package version data from repositories available to your account (e.g., package_name=go)

```bash
chainctl packages versions list package_name
```
