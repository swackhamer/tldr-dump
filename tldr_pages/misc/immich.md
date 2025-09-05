# immich

> Immich command-line interface (CLI) that allows you to perform certain actions. See also: `immich-go`. More information: <https://immich.app/docs/features/command-line-interface/>.

## Examples

### Authenticate to Immich server

```bash
immich login server_url/api server_key
```

### Upload some image files

```bash
immich upload file1.jpg file2.jpg ...
```

### Upload a directory including subdirectories

```bash
immich upload --recursive path/to/directory
```

### Create an album based on a directory

```bash
immich upload --album-name "My summer holiday" --recursive path/to/directory
```

### Skip assets matching a glob pattern

```bash
immich upload --ignore **/Raw/** **/*.tif --recursive path/to/directory
```

### Include hidden files

```bash
immich upload --include-hidden --recursive path/to/directory
```
