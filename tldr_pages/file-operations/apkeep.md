# apkeep

> Download APK files from various sources. More information: <https://github.com/EFForg/apkeep>.

## Examples

### Download an APK file to the specified directory

```bash
apkeep --app com.example.application path/to/directory
```

### List all available versions for download

```bash
apkeep --app com.example.application --list-versions path/to/directory
```

### Specify a store to download from

```bash
apkeep --app com.example.application --download-source apk-pure|google-play|f-droid|huawei-app-gallery path/to/directory
```
