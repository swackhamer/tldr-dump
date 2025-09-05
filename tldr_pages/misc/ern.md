# ern

> Electrode Native platform client. More information: <https://native.electrode.io/reference/index-6>.

## Examples

### Create a new `ern` application (`MiniApp`)

```bash
ern create-miniapp application_name
```

### Run one or more `MiniApps` in the iOS/Android Runner application

```bash
ern run-ios|android
```

### Create an Electrode Native container

```bash
ern create-container --miniapps /path/to/miniapp_directory --platform ios|android
```

### Publish an Electrode Native container to a local Maven repository

```bash
ern publish-container --publisher maven --platform android --extra '{"groupId":"com.walmart.ern","artifactId":"quickstart"}'
```

### Transform an iOS container into a pre-compiled binary framework

```bash
ern transform-container --platform ios --transformer xcframework
```

### List all installed versions of Electrode Native

```bash
ern platform versions
```

### Set a logging level

```bash
ern platform config set logLevel trace|debug
```
