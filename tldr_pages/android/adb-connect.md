# adb-connect

> Connect to an Android device wirelessly. More information: <https://developer.android.com/tools/adb>.

## Examples

### Pair with an Android device (address and pairing code can be found in developer options)

```bash
adb pair ip_address:port
```

### Connect to an Android device (port will be different from pairing)

```bash
adb connect ip_address:port
```

### Disconnect a device

```bash
adb disconnect ip_address:port
```
