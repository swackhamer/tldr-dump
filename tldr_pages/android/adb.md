# adb

> Android Debug Bridge: communicate with an Android emulator instance or connected Android devices. Some subcommands such as `shell` have their own usage documentation. More information: <https://developer.android.com/tools/adb>.

## Examples

### Check whether the adb server process is running and start it

```bash
adb start-server
```

### Terminate the adb server process

```bash
adb kill-server
```

### Start a remote shell in the target emulator/device instance

```bash
adb shell
```

### Push an Android application to an emulator/device

```bash
adb install -r path/to/file.apk
```

### Copy a file/directory from the target device

```bash
adb pull path/to/device_file_or_directory path/to/local_destination_directory
```

### Copy a file/directory to the target device

```bash
adb push path/to/local_file_or_directory path/to/device_destination_directory
```

### List all connected devices

```bash
adb devices
```

### Specify which device to send commands to if there are multiple devices

```bash
adb -s device_ID shell
```
