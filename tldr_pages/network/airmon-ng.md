# airmon-ng

> Activate monitor mode on wireless network devices. Part of `aircrack-ng`. More information: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

## Examples

### List wireless devices and their statuses

```bash
sudo airmon-ng
```

### Turn on monitor mode for a specific device

```bash
sudo airmon-ng start wlan0
```

### Kill disturbing processes that use wireless devices

```bash
sudo airmon-ng check kill
```

### Turn off monitor mode for a specific network interface

```bash
sudo airmon-ng stop wlan0mon
```
