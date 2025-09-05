# l2ping

> Send an L2CAP echo request and receive an answer. More information: <https://manned.org/l2ping>.

## Examples

### Ping a Bluetooth device

```bash
sudo l2ping mac_address
```

### Reverse ping a Bluetooth device

```bash
sudo l2ping -r mac_address
```

### Ping a Bluetooth device from a specified interface

```bash
sudo l2ping -i hci0 mac_address
```

### Ping Bluetooth device with a specified sized data package

```bash
sudo l2ping -s byte_count mac_address
```

### Ping flood a Bluetooth device

```bash
sudo l2ping -f mac_address
```

### Ping a Bluetooth device a specified amount of times

```bash
sudo l2ping -c amount mac_address
```

### Ping a Bluetooth device with a specified delay between requests

```bash
sudo l2ping -d seconds mac_address
```
