# az-storage-blob

> Manage blob storage containers and objects in Azure. Part of `azure-cli` (also known as `az`). More information: <https://learn.microsoft.com/cli/azure/storage/blob>.

## Examples

### Download a blob to a file path specifying a source container

```bash
az storage blob download --account-name storage_account_name --account-key storage_account_key [-c|--container-name] container_name [-n|--name] path/to/blob [-f|--file] path/to/local_file
```

### Download blobs from a blob container recursively

```bash
az storage blob download-batch --account-name storage_account_name --account-key storage_account_key [-s|--source] container_name [-d|--destination] path/to/remote --pattern filename_regex [-d|--destination] path/to/destination
```

### Upload a local file to blob storage

```bash
az storage blob upload --account-name storage_account_name --account-key storage_account_key [-c|--container-name] container_name [-n|--name] path/to/blob [-f|--file] path/to/local_file
```

### Delete a blob object

```bash
az storage blob delete --account-name storage_account_name --account-key storage_account_key [-c|--container-name] container_name [-n|--name] path/to/blob
```

### Generate a shared access signature for a blob

```bash
az storage blob generate-sas --account-name storage_account_name --account-key storage_account_key [-c|--container-name] container_name [-n|--name] path/to/blob --permissions permission_set --expiry Y-m-d'T'H:M'Z' --https-only
```
