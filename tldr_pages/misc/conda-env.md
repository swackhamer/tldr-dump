# conda-env

> Manage conda environments. More information: <https://docs.conda.io/projects/conda/en/latest/commands/env/index.html>.

## Examples

### Create an environment from an environment file (YAML, TXT, etc.)

```bash
conda env create [-f|--file] path/to/file
```

### Delete an environment and everything in it

```bash
conda env remove [-n|--name] environment_name
```

### Update an environment based on an environment file

```bash
conda env update [-f|--file] path/to/file --prune
```

### List all environments

```bash
conda env list
```

### View environment details

```bash
conda env export
```

### List environment variables

```bash
conda env config vars list
```

### Set environment variables

```bash
conda env config vars set my_var=value
```
