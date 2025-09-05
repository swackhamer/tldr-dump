# m4b-tool

> Merge, split, and manipulate audiobook files with chapters. More information: <https://github.com/sandreas/m4b-tool>.

## Examples

### Create an audiobook with the audio files in the input directory

```bash
m4b-tool merge path/to/input_directory --output-file=path/to/merged.m4b
```

### Make chapters using the input files' names

```bash
m4b-tool merge path/to/input_directory --output-file=path/to/merged.m4b --use-filenames-as-chapters
```
