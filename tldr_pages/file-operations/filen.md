# filen

> Interface with Filen, an end-to-end encrypted cloud storage service. More information: <https://github.com/FilenCloudDienste/filen-cli>.

## Examples

### Enter interactive mode

```bash
filen
```

### Upload a local file to a specific remote folder

```bash
filen upload path/to/local_file remote_folder_id
```

### Download a file or folder using its remote ID

```bash
filen download remote_id path/to/local_destination
```

### List files and folders inside a remote folder

```bash
filen ls remote_folder
```

### Delete a remote file or folder (move it to trash)

```bash
filen rm remote_id
```

### Restore a trashed item

```bash
filen trash restore remote_id
```

### Synchronize a local folder with a remote folder (two-way sync)

```bash
filen sync path/to/local_folder:/remote_folder --continuous
```

### Download changes from the cloud to a local folder (one-way sync)

```bash
filen sync path/to/local_folder:ctl:/remote_folder
```
