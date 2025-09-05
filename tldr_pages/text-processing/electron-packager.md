# electron-packager

> Build Electron app executables for Windows, Linux and macOS. Requires a valid package.json in the application directory. More information: <https://github.com/electron/electron-packager>.

## Examples

### Package an application for the current architecture and platform

```bash
electron-packager "path/to/app" "app_name"
```

### Package an application for all architectures and platforms

```bash
electron-packager "path/to/app" "app_name" --all
```

### Package an application for 64-bit Linux

```bash
electron-packager "path/to/app" "app_name" --platform="linux" --arch="x64"
```

### Package an application for ARM macOS

```bash
electron-packager "path/to/app" "app_name" --platform="darwin" --arch="arm64"
```
