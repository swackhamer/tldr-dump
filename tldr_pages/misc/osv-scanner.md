# osv-scanner

> Scan various mediums for dependencies and matches them against the OSV database. More information: <https://osv.dev/about>.

## Examples

### Scan a Docker image

```bash
osv-scanner -D docker_image_name
```

### Scan a package lockfile

```bash
osv-scanner -L path/to/lockfile
```

### Scan an SBOM file

```bash
osv-scanner -S path/to/sbom_file
```

### Scan multiple directories recursively

```bash
osv-scanner -r directory1 directory2 ...
```

### Skip scanning Git repositories

```bash
osv-scanner --skip-git -r|-D target
```

### Output result in JSON format

```bash
osv-scanner --json -D|-L|-S|-r target
```
