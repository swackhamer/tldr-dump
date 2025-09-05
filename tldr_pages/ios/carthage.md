# carthage

> A dependency management tool for Cocoa applications. More information: <https://github.com/Carthage/Carthage>.

## Examples

### Download the latest version of all dependencies mentioned in Cartfile, and build them

```bash
carthage update
```

### Update dependencies, but only build for iOS

```bash
carthage update --platform ios
```

### Update dependencies, but don't build any of them

```bash
carthage update --no-build
```

### Download and rebuild the current version of dependencies (without updating them)

```bash
carthage bootstrap
```

### Rebuild a specific dependency

```bash
carthage build dependency
```
