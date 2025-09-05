# kismet

> A wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework. More information: <https://www.kismetwireless.net/docs/readme/starting/commandline/>.

## Examples

### Capture packets from a specific wireless interface

```bash
sudo kismet -c wlan0
```

### Monitor multiple channels on a wireless interface

```bash
sudo kismet -c wlan0,wlan1 -m
```

### Capture packets and save them to a specific directory

```bash
sudo kismet -c wlan0 -d path/to/output
```

### Start Kismet with a specific configuration file

```bash
sudo kismet -c wlan0 [-f|--config-file] path/to/config.conf
```

### Monitor and log data to an SQLite database

```bash
sudo kismet -c wlan0 --log-to-db
```

### Monitor using a specific data source

```bash
sudo kismet -c wlan0 --data-source=rtl433
```

### Enable alerts for specific events

```bash
sudo kismet -c wlan0 --enable-alert=new_ap
```

### Display detailed information about a specific AP's packets

```bash
sudo kismet -c wlan0 --info BSSID
```
