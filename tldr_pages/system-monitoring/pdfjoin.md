# pdfjoin

> PDF merging utility based on pdfjam. More information: <https://github.com/rrthomas/pdfjam-extras>.

## Examples

### Merge two PDFs into one with the default suffix "joined"

```bash
pdfjoin path/to/file1.pdf path/to/file2.pdf
```

### Merge the first page of each given file together

```bash
pdfjoin path/to/file1.pdf path/to/file2.pdf ... 1 --outfile output_file
```

### Save pages 3 to 5 followed by page 1 to a new PDF with custom suffix

```bash
pdfjoin path/to/file.pdf 3-5,1 --suffix rearranged
```

### Merge page subranges from two PDFs

```bash
pdfjoin /path/to/file1.pdf 2- file2 last-3 --outfile output_file
```
