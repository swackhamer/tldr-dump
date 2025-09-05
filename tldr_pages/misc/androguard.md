# androguard

> Reverse engineer Android applications. Written in Python. More information: <https://github.com/androguard/androguard>.

## Examples

### Display Android app manifest

```bash
androguard axml path/to/app.apk
```

### Display app metadata (version and app ID)

```bash
androguard apkid path/to/app.apk
```

### Decompile Java code from an app

```bash
androguard decompile path/to/app.apk --output path/to/directory
```
