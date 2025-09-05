# xctool

> Build Xcode projects. More information: <https://github.com/facebookarchive/xctool>.

## Examples

### Build a single project without any workspace

```bash
xctool -project YourProject.xcodeproj -scheme YourScheme build
```

### Build a project that is part of a workspace

```bash
xctool -workspace YourWorkspace.xcworkspace -scheme YourScheme build
```

### Clean, build and execute all the tests

```bash
xctool -workspace YourWorkspace.xcworkspace -scheme YourScheme clean build test
```
