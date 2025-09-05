# nodemon

> Watch files and automatically restart a node application when changes are detected. More information: <https://nodemon.io>.

## Examples

### Execute the specified file and watch a specific file for changes

```bash
nodemon path/to/file.js
```

### Manually restart nodemon (note nodemon must already be active for this to work)

```bash
rs
```

### Ignore specific files

```bash
nodemon --ignore path/to/file_or_directory
```

### Pass arguments to the node application

```bash
nodemon path/to/file.js arguments
```

### Pass arguments to node itself if they're not nodemon arguments already (e.g. `--inspect`)

```bash
nodemon arguments path/to/file.js
```

### Run an arbitrary non-node script

```bash
nodemon --exec "command_to_run_script options" path/to/script
```

### Run a Python script

```bash
nodemon --exec "python options" path/to/file.py
```
