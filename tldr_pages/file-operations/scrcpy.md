# scrcpy

> Display and control your Android device on a desktop. More information: <https://github.com/Genymobile/scrcpy>.

## Examples

### Display a mirror of a connected device

```bash
scrcpy
```

### Turn the device screen off and prevent it from sleeping while mirroring

```bash
scrcpy [-S|--turn-screen-off] [-w|--stay-awake]
```

### Display a mirror of a specific device based on its ID or IP address (find it under the `adb devices` command)

```bash
scrcpy [-s|--serial] 0123456789abcdef|192.168.0.1:5555
```

### Start display in fullscreen mode

```bash
scrcpy [-f|--fullscreen]
```

### Show touches on physical device

```bash
scrcpy [-t|--show-touches]
```

### Record display screen

```bash
scrcpy [-r|--record] path/to/file.mp4
```

### Specify the target directory for pushing files to device by drag and drop (non-APK)

```bash
scrcpy --push-target path/to/directory
```
