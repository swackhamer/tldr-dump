# delta

> A viewer for Git and diff output. More information: <https://dandavison.github.io/delta/full---help-output.html>.

## Examples

### Compare files or directories

```bash
delta path/to/old_file_or_directory path/to/new_file_or_directory
```

### Compare files or directories, showing the line numbers

```bash
delta [-n|--line-numbers] path/to/old_file_or_directory path/to/new_file_or_directory
```

### Compare files or directories, showing the differences side by side

```bash
delta [-s|--side-by-side] path/to/old_file_or_directory path/to/new_file_or_directory
```

### Compare files or directories, ignoring any Git configuration settings

```bash
delta --no-gitconfig path/to/old_file_or_directory path/to/new_file_or_directory
```

### Compare, rendering commit hashes, file names, and line numbers as hyperlinks, according to the hyperlink spec for terminal emulators

```bash
delta --hyperlinks path/to/old_file_or_directory path/to/new_file_or_directory
```

### Display the current settings

```bash
delta --show-config
```

### Display supported languages and associated file extensions

```bash
delta --list-languages
```
