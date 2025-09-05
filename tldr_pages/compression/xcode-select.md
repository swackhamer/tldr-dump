# xcode-select

> Switch between different versions of Xcode and the included developer tools. Also used to update the path to Xcode if it is moved after installation. More information: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

## Examples

### Install Xcode's command-line tools

```bash
xcode-select --install
```

### Select a given path as the active developer directory

```bash
xcode-select --switch path/to/Xcode.app/Contents/Developer
```

### Select a given Xcode instance and use its developer directory as the active one

```bash
xcode-select --switch path/to/Xcode_file.app
```

### Print the currently selected developer directory

```bash
xcode-select --print-path
```

### Discard any user-specified developer directory so that it will be found via the default search mechanism

```bash
sudo xcode-select --reset
```
