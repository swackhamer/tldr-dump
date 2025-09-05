# fclones

> Efficient duplicate file finder and remover. More information: <https://github.com/pkolaczk/fclones>.

## Examples

### Search for duplicate files in the current directory

```bash
fclones group .
```

### Search multiple directories for duplicate files and cache the results

```bash
fclones group --cache path/to/directory1 path/to/directory2
```

### Search only the specified directory for duplicate files, skipping subdirectories and save the results into a file

```bash
fclones group path/to/directory --depth 1 > path/to/file.txt
```

### Move the duplicate files in a TXT file to a different directory

```bash
fclones move path/to/target_directory < path/to/file.txt
```

### Perform a dry run for soft links in a TXT file without actually linking

```bash
fclones link --soft < path/to/file.txt --dry-run 2 > /dev/null
```

### Delete the newest duplicates from the current directory without storing them in a file

```bash
fclones group . | fclones remove --priority newest
```

### Preprocess JPEG files in the current directory by using an external command to strip their EXIF data before matching for duplicates

```bash
fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place
```
