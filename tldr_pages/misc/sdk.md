# sdk

> Manage parallel versions of multiple Software Development Kits. Supports Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x and many others. More information: <https://sdkman.io/usage>.

## Examples

### Install an SDK version

```bash
sdk install sdk_name sdk_version
```

### Use a specific SDK version for the current terminal session

```bash
sdk use sdk_name sdk_version
```

### Show the stable version of any available SDK

```bash
sdk current sdk_name
```

### Show the stable versions of all installed SDKs

```bash
sdk current
```

### List all available SDKs

```bash
sdk list
```

### List all versions of an SDK

```bash
sdk list sdk_name
```

### Upgrade an SDK to the latest stable version

```bash
sdk upgrade sdk_name
```

### Uninstall a specific SDK version

```bash
sdk rm sdk_name sdk_version
```
