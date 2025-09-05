# xcodes

> Download, install and manage multiple Xcode versions. See also: `xcodes runtimes`. More information: <https://github.com/xcodesorg/xcodes>.

## Examples

### List all installed Xcode versions

```bash
xcodes installed
```

### List all available Xcode versions

```bash
xcodes list
```

### Select an Xcode version by specifying a version number or a path

```bash
xcodes select xcode_version|path/to/Xcode.app
```

### Download and install a specific Xcode version

```bash
xcodes install xcode_version
```

### Install the latest Xcode release and select it

```bash
xcodes install --latest --select
```

### Download a specific Xcode version archive to a given directory without installing it

```bash
xcodes download xcode_version --directory path/to/directory
```
