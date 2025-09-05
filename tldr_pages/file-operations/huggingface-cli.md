# huggingface-cli

> Interact with Hugging Face Hub. Login, manage local cache, download or upload files. More information: <https://huggingface.co/docs/huggingface_hub/guides/cli>.

## Examples

### Login to Hugging Face Hub

```bash
huggingface-cli login
```

### Display the name of the logged in user

```bash
huggingface-cli whoami
```

### Log out

```bash
huggingface-cli logout
```

### Print information about the environment

```bash
huggingface-cli env
```

### Download files from an repository and print out the path (omit filenames to download entire repository)

```bash
huggingface-cli download --repo-type repo_type repo_id filename1 filename2 ...
```

### Upload an entire folder or a file to Hugging Face

```bash
huggingface-cli upload --repo-type repo_type repo_id path/to/local_file_or_directory path/to/repo_file_or_directory
```

### Scan cache to see downloaded repositories and their disk usage

```bash
huggingface-cli scan-cache
```

### Delete the cache interactively

```bash
huggingface-cli delete-cache
```
