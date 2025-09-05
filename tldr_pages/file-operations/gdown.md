# gdown

> Download files from Google Drive and other URLs. More information: <https://github.com/wkentaro/gdown>.

## Examples

### Download a file from a URL

```bash
gdown url
```

### Download using a file ID

```bash
gdown file_id
```

### Download with fuzzy file ID extraction (also works with <https://docs.google.com> links)

```bash
gdown --fuzzy url
```

### Download a folder using its ID or the full URL

```bash
gdown folder_id|url [-O|--output] path/to/output_directory --folder
```

### Download a tar archive, write it to `stdout` and extract it

```bash
gdown tar_url [-O|--output] - [-q|--quiet] | tar xvf -
```
