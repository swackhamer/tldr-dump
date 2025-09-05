# dart

> Manage Dart projects. More information: <https://dart.dev/tools/dart-tool>.

## Examples

### Initialize a new Dart project in a directory of the same name

```bash
dart create project_name
```

### Run a Dart file

```bash
dart run path/to/file.dart
```

### Download dependencies for the current project

```bash
dart pub get
```

### Run unit tests for the current project

```bash
dart test
```

### Update an outdated project's dependencies to support null-safety

```bash
dart pub upgrade --null-safety
```

### Compile a Dart file to a native binary

```bash
dart compile exe path/to/file.dart
```

### Apply automated fixes to the current project

```bash
dart fix --apply
```
