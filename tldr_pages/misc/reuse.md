# reuse

> Tool for compliance with the REUSE recommendations. More information: <https://reuse.readthedocs.io/en/stable/man/index.html>.

## Examples

### Lint for REUSE compliance for the current project (version control aware)

```bash
reuse lint
```

### Lint for REUSE compliance from the specified directory

```bash
reuse --root path/to/directory lint
```

### Add copyright statement to file

```bash
reuse annotate [-c|--copyright] "your_name <your_email>" --fallback-dot-license path/to/file
```

### Add licence information to file

```bash
reuse annotate [-l|--license] spdx_identifier --fallback-dot-license path/to/file
```

### Download a license by its SPDX identifier and place it in the LICENSES directory

```bash
reuse download spdx-identifier
```

### Download all missing licenses detected in the project

```bash
reuse download --all
```
