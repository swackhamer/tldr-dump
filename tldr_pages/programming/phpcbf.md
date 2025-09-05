# phpcbf

> Fix violations detected by phpcs. More information: <https://github.com/squizlabs/PHP_CodeSniffer>.

## Examples

### Fix issues in the specified directory (defaults to the PEAR standard)

```bash
phpcbf path/to/directory
```

### Display a list of installed coding standards

```bash
phpcbf -i
```

### Specify a coding standard to validate against

```bash
phpcbf path/to/directory --standard standard
```

### Specify comma-separated file extensions to include when sniffing

```bash
phpcbf path/to/directory --extensions file_extension1,file_extension2,...
```

### A comma-separated list of files to load before processing

```bash
phpcbf path/to/directory --bootstrap path/to/file1,path/to/file2,...
```

### Don't recurse into subdirectories

```bash
phpcbf path/to/directory -l
```
