# dvc-dag

> Visualize the pipeline(s) defined in `dvc.yaml`. More information: <https://dvc.org/doc/command-reference/dag>.

## Examples

### Visualize the entire pipeline

```bash
dvc dag
```

### Visualize the pipeline stages up to a specified target stage

```bash
dvc dag target
```

### Export the pipeline in the dot format

```bash
dvc dag --dot > path/to/pipeline.dot
```
