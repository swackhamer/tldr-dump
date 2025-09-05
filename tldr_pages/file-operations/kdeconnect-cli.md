# kdeconnect-cli

> Use KDE Connect for sharing files or text to a device, ringing it, unlocking it, and much more. More information: <https://kdeconnect.kde.org>.

## Examples

### List all devices

```bash
kdeconnect-cli --list-devices
```

### List available (paired and reachable) devices

```bash
kdeconnect-cli --list-available
```

### Request pairing with a specific device, specifying its ID

```bash
kdeconnect-cli --pair --device device_id
```

### Ring a device, specifying its name

```bash
kdeconnect-cli --ring --name "device_name"
```

### Share an URL or file with a paired device, specifying its ID

```bash
kdeconnect-cli --share url|path/to/file --device device_id
```

### Send an SMS with an optional attachment to a specific number

```bash
kdeconnect-cli --name "device_name" --send-sms "message" --destination phone_number --attachment path/to/file
```

### Unlock a specific device

```bash
kdeconnect-cli --name "device_name" --unlock
```

### Simulate a key press on a specific device

```bash
kdeconnect-cli --name "device_name" --send-keys key
```
