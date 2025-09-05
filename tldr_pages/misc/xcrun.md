# xcrun

> Run or locate development tools and properties. More information: <https://keith.github.io/xcode-man-pages/xcrun.1.html>.

## Examples

### Find and run a tool from the active developer directory

```bash
xcrun tool arguments
```

### Show verbose output

```bash
xcrun tool arguments --verbose
```

### Find a tool for a given SDK

```bash
xcrun --sdk sdk_name
```

### Find a tool for a given toolchain

```bash
xcrun --toolchain name
```

### Display help

```bash
xcrun --help
```

### Display version

```bash
xcrun --version
```
