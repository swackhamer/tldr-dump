# systemsetup

> Configure System Preferences machine settings. More information: <https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>.

## Examples

### Enable remote login (SSH)

```bash
systemsetup -setremotelogin on
```

### Specify timezone, NTP Server and enable network time

```bash
systemsetup -settimezone "US/Pacific" -setnetworktimeserver us.pool.ntp.org -setusingnetworktime on
```

### Make the machine never sleep and automatically restart on power failure or kernel panic

```bash
systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on
```

### List valid startup disks

```bash
systemsetup -liststartupdisks
```

### Specify a new startup disk

```bash
systemsetup -setstartupdisk path/to/directory
```
