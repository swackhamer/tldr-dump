# svgo

> SVG Optimizer: optimizing Scalable Vector Graphics files. Based in Node.js. It applies a series of transformation rules (plugins), which can be toggled individually. More information: <https://github.com/svg/svgo>.

## Examples

### Optimize a file using the default plugins (overwrites the original file)

```bash
svgo test.svg
```

### Optimize a file and save the result to another file

```bash
svgo test.svg [-o|--output] test.min.svg
```

### Optimize all SVG files within a directory (overwrites the original files)

```bash
svgo [-f|--folder] path/to/directory/with/svg/files
```

### Optimize all SVG files within a directory and save the resulting files to another directory

```bash
svgo [-f|--folder] path/to/input/directory [-o|--output] path/to/output/directory
```

### Optimize SVG content passed from another command, and save the result to a file

```bash
cat test.svg | svgo [-i|--input] - [-o|--output] test.min.svg
```

### Optimize a file and print out the result

```bash
svgo test.svg [-o|--output] -
```

### Show available plugins

```bash
svgo --show-plugins
```
