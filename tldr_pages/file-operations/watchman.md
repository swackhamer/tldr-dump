# watchman

> A service that watches files, and triggers actions when changes occur. More information: <https://facebook.github.io/watchman/docs/cli-options>.

## Examples

### Infer the root directory of the project containing the specified directory, and watch its files and sub-folders for changes

```bash
watchman watch-project path/to/directory
```

### Add a trigger to run a command when files with a specified filename pattern in a watched directory change

```bash
watchman -- trigger path/to/watched_directory trigger_name 'pattern' -- command
```

### List all watched directories

```bash
watchman watch-list
```

### Delete a watch on a directory and its associated triggers

```bash
watchman watch-del path/to/watched_directory
```

### Delete all watched directories and triggers

```bash
watchman watch-del-all
```

### List all triggers on a watched directory

```bash
watchman trigger-list path/to/watched_directory
```

### Delete a trigger from a watched directory

```bash
watchman trigger-del path/to/watched_directory trigger_name
```

### Temporarily stop `watchman`, until the next time you call a `watchman` command

```bash
watchman shutdown-server
```
