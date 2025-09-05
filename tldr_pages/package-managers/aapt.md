# aapt

> Android Asset Packaging Tool: compile and package an Android app's resources. More information: <https://manned.org/aapt>.

## Examples

### List files contained in an APK archive

```bash
aapt list path/to/app.apk
```

### Display an app's metadata (version, permissions, etc.)

```bash
aapt dump badging path/to/app.apk
```

### Create a new APK archive with files from the specified directory

```bash
aapt package -F path/to/app.apk path/to/directory
```
