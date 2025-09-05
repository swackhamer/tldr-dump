# conda-install

> Install packages into an existing conda environment. More information: <https://docs.conda.io/projects/conda/en/latest/commands/install.html>.

## Examples

### Install one or more package into the currently active conda environment

```bash
conda install package1 package2 ...
```

### Install a single package into the currently active conda environment using channel conda-forge

```bash
conda install [-c|--channel] conda-forge package
```

### Install a single package into the currently active conda environment using channel conda-forge and ignoring other channels

```bash
conda install [-c|--channel] conda-forge --override-channels package
```

### Install a specific version of a package

```bash
conda install package=version
```

### Install a package into a specific environment

```bash
conda install [-n|--name] environment package
```

### Update a package in the current environment

```bash
conda install --upgrade package
```

### Install a package and agree to the transactions without prompting

```bash
conda install [-y|--yes] package
```
