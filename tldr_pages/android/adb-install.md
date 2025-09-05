# adb-install

> Push packages to a connected Android device or emulator. More information: <https://developer.android.com/tools/adb>.

## Examples

### Push an Android application to an emulator/device

```bash
adb install path/to/file.apk
```

### Push an Android application to a specific emulator/device (overrides `$ANDROID_SERIAL`)

```bash
adb -s serial_number install path/to/file.apk
```

### [r]einstall an existing app, keeping its data

```bash
adb install -r path/to/file.apk
```

### Push an Android application allowing version code [d]owngrade (debuggable packages only)

```bash
adb install -d path/to/file.apk
```

### [g]rant all permissions listed in the app manifest

```bash
adb install -g path/to/file.apk
```

### Quickly update an installed package by only updating the parts of the APK that changed

```bash
adb install --fastdeploy path/to/file.apk
```
