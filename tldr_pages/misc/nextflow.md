# nextflow

> Run computational pipelines. Mostly used for bioinformatics workflows. More information: <https://www.nextflow.io>.

## Examples

### Run a pipeline, use cached results from previous runs

```bash
nextflow run main.nf -resume
```

### Run a specific release of a remote workflow from GitHub

```bash
nextflow run user/repo -revision release_tag
```

### Run with a given work directory for intermediate files, save execution report

```bash
nextflow run workflow -work-dir path/to/directory -with-report report.html
```

### Show details of previous runs in current directory

```bash
nextflow log
```

### Remove cache and intermediate files for a specific run

```bash
nextflow clean -force run_name
```

### List all downloaded projects

```bash
nextflow list
```

### Pull the latest version of a remote workflow from Bitbucket

```bash
nextflow pull user/repo -hub bitbucket
```

### Update Nextflow

```bash
nextflow self-update
```
