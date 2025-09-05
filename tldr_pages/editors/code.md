# code

> Cross platform and extensible code editor. More information: <https://code.visualstudio.com/docs/configure/command-line>.

## Examples

### Start Visual Studio Code

```bash
code
```

### Open specific files/directories

```bash
code path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Compare two specific files

```bash
code [-d|--diff] path/to/file1 path/to/file2
```

### Open specific files/directories in a new window

```bash
code [-n|--new-window] path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Install/uninstall a specific extension

```bash
code --install|uninstall-extension publisher.extension
```

### Display diagnostic and process information about the running code window

```bash
code [-s|--status]
```

### Print installed extensions with their versions

```bash
code --list-extensions --show-versions
```

### Start the editor as a superuser (root) while storing user data in a specific directory

```bash
sudo code --user-data-dir path/to/directory
```
