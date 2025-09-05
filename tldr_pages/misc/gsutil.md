# gsutil

> Access Google Cloud Storage. You can use `gsutil` to do a wide range of bucket and object management tasks. More information: <https://cloud.google.com/storage/docs/gsutil>.

## Examples

### List all buckets in a project you are logged into

```bash
gsutil ls
```

### List the objects in a bucket

```bash
gsutil ls -r 'gs://bucket_name/prefix**'
```

### Download an object from a bucket

```bash
gsutil cp gs://bucket_name/object_name path/to/save_location
```

### Upload an object to a bucket

```bash
gsutil cp object_location gs://destination_bucket_name/
```

### Rename or move objects in a bucket

```bash
gsutil mv gs://bucket_name/old_object_name gs://bucket_name/new_object_name
```

### Create a new bucket in the project you are logged into

```bash
gsutil mb gs://bucket_name
```

### Delete a bucket and remove all the objects in it

```bash
gsutil rm -r gs://bucket_name
```
