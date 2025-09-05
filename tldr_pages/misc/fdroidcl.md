# fdroidcl

> Manage F-Droid apps of devices connected via ADB. More information: <https://github.com/mvdan/fdroidcl>.

## Examples

### Fetch the F-Droid index

```bash
fdroidcl update
```

### Display information about an app

```bash
fdroidcl show app_id
```

### Download the APK file of an app

```bash
fdroidcl download app_id
```

### Search for an app in the index

```bash
fdroidcl search search_pattern
```

### Install an app on a connected device

```bash
fdroidcl install app_id
```

### Add a repository

```bash
fdroidcl repo add repo_name url
```

### Remove, enable or disable a repository

```bash
fdroidcl repo remove|enable|disable repo_name
```
