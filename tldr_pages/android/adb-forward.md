# adb-forward

> Connect to an Android device wirelessly. More information: <https://developer.android.com/tools/adb>.

## Examples

### Forward a TCP port

```bash
adb forward tcp:local_port tcp:remote_port
```

### List all forwardings

```bash
adb forward --list
```

### Remove a forwarding rule

```bash
adb forward --remove tcp:local_port
```

### Remove all forwarding rules

```bash
adb forward --remove-all
```
