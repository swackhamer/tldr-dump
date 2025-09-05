# tmutil

> Utility for managing Time Machine backups. Most verbs require root privileges. More information: <https://keith.github.io/xcode-man-pages/tmutil.8.html>.

## Examples

### Set an HFS+ drive as the backup destination

```bash
sudo tmutil setdestination path/to/disk_mount_point
```

### Set an APF share or SMB share as the backup destination

```bash
sudo tmutil setdestination "protocol://user[:password]@host/share"
```

### Append the given destination to the list of destinations

```bash
sudo tmutil setdestination -a destination
```

### Enable automatic backups

```bash
sudo tmutil enable
```

### Disable automatic backups

```bash
sudo tmutil disable
```

### Start a backup, if one is not running already, and release control of the shell

```bash
sudo tmutil startbackup
```

### Start a backup and block until the backup is finished

```bash
sudo tmutil startbackup -b
```

### Stop a backup

```bash
sudo tmutil stopbackup
```
