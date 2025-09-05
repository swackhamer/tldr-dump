# conda-doctor

> Display a health report for your environment. More information: <https://docs.conda.io/projects/conda/en/latest/commands/doctor.html>.

## Examples

### View report for the currently active environment

```bash
conda doctor
```

### Specify an environment by name

```bash
conda doctor [-n|--name] environment_name
```

### Specify an environment by its path

```bash
conda doctor [-p|--prefix] path/to/environment
```

### Enable verbose output (Note: the `-v` flag can be repeated to increase verbosity)

```bash
conda doctor [-v|--verbose]
```
