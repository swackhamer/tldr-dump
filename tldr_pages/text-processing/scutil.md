# scutil

> Manage system configuration parameters. Require root privileges when setting configuration. More information: <https://keith.github.io/xcode-man-pages/scutil.8.html>.

## Examples

### Display DNS Configuration

```bash
scutil --dns
```

### Display proxy configuration

```bash
scutil --proxy
```

### Get computer name

```bash
scutil --get ComputerName
```

### Set computer name

```bash
sudo scutil --set ComputerName computer_name
```

### Get hostname

```bash
scutil --get HostName
```

### Set hostname

```bash
scutil --set HostName hostname
```
