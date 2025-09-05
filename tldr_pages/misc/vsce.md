# vsce

> Extension manager for Visual Studio Code. More information: <https://github.com/microsoft/vscode-vsce>.

## Examples

### List all the extensions created by a publisher

```bash
vsce list publisher
```

### Publish an extension as major, minor or patch version

```bash
vsce publish major|minor|patch
```

### Unpublish an extension

```bash
vsce unpublish extension_id
```

### Package the current working directory as a `.vsix` file

```bash
vsce package
```

### Show the metadata associated with an extension

```bash
vsce show extension_id
```
