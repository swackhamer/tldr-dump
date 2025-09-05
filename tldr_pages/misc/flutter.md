# flutter

> Google's free, open source, and cross-platform mobile app SDK. Some subcommands such as `pub` have their own usage documentation. More information: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

## Examples

### Initialize a new Flutter project in a directory of the same name

```bash
flutter create project_name
```

### Check if all external tools are correctly installed

```bash
flutter doctor
```

### List or change Flutter channel

```bash
flutter channel stable|beta|dev|master
```

### Run Flutter on all started emulators and connected devices

```bash
flutter run -d all
```

### Run tests in a terminal from the root of the project

```bash
flutter test test/example_test.dart
```

### Build a release APK targeting most modern smartphones

```bash
flutter build apk --target-platform android-arm,android-arm64
```

### Delete the `build` and `.dart_tool` directories

```bash
flutter clean
```

### Display help about a specific command

```bash
flutter help command
```
