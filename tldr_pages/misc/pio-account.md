# pio-account

> Manage your PlatformIO account. More information: <https://docs.platformio.org/en/latest/core/userguide/account/>.

## Examples

### Register a new PlatformIO account

```bash
pio account register [-u|--username] username [-e|--email] email [-p|--password] password --firstname firstname --lastname lastname
```

### Permanently delete your PlatformIO account and related data

```bash
pio account destroy
```

### Log in to your PlatformIO account

```bash
pio account login [-u|--username] username [-p|--password] password
```

### Log out of your PlatformIO account

```bash
pio account logout
```

### Update your PlatformIO profile

```bash
pio account update [-u|--username] username [-e|--email] email --firstname firstname --lastname lastname --current-password password
```

### Show detailed information about your PlatformIO account

```bash
pio account show
```

### Reset your password using your username or email

```bash
pio account forgot [-u|--username] username_or_email
```
