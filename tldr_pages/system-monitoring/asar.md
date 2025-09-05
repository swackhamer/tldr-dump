# asar

> A file archiver for the Electron platform. More information: <https://github.com/electron/asar>.

## Examples

### Archive a file or directory

```bash
asar pack path/to/input_file_or_directory path/to/output_archive.asar
```

### Extract an archive

```bash
asar extract path/to/archive.asar
```

### Extract a specific file from an archive

```bash
asar extract-file path/to/archive.asar file
```

### List the contents of an archive file

```bash
asar list path/to/archive.asar
```
