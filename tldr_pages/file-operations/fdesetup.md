# fdesetup

> Set and retrieve FileVault related information. More information: <https://keith.github.io/xcode-man-pages/fdesetup.8.html>.

## Examples

### List current FileVault enabled users

```bash
sudo fdesetup list
```

### Get current FileVault status

```bash
fdesetup status
```

### Add FileVault enabled user

```bash
sudo fdesetup add -usertoadd user1
```

### Enable FileVault

```bash
sudo fdesetup enable
```

### Disable FileVault

```bash
sudo fdesetup disable
```
