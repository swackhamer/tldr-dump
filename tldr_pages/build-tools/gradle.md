# gradle

> An open source build automation system. More information: <https://gradle.org>.

## Examples

### Compile a package

```bash
gradle build
```

### Exclude test task

```bash
gradle build [-x|--exclude-task] test
```

### Run in offline mode to prevent Gradle from accessing the network during builds

```bash
gradle build --offline
```

### Clear the build directory

```bash
gradle clean
```

### Build an Android Package (APK) in release mode

```bash
gradle assembleRelease
```

### List the main tasks

```bash
gradle tasks
```

### List all the tasks

```bash
gradle tasks --all
```
