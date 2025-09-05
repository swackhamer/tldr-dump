# mamba

> Fast, cross-platform package manager, intended as a drop-in replacement for conda. Some subcommands such as `repoquery` have their own usage documentation. More information: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

## Examples

### Create a new environment, installing the specified packages into it

```bash
mamba create [-n|--name] environment_name python=3.10 matplotlib
```

### Install packages into the current environment, specifying the package channel

```bash
mamba install [-c|--channel] conda-forge python=3.6 numpy
```

### Update all packages in the current environment

```bash
mamba update --all
```

### Search for a specific package across repositories

```bash
mamba repoquery search numpy
```

### List all environments

```bash
mamba info --envs
```

### Remove unused [p]ackages and [t]arballs from the cache

```bash
mamba clean -pt
```

### Activate an environment

```bash
mamba activate environment_name
```

### List all installed packages in the currently activated environment

```bash
mamba list
```
