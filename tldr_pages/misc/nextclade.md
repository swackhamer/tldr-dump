# nextclade

> Bioinformatics tool for virus genome alignment, clade assignment and qc checks. More information: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/reference.html>.

## Examples

### Align sequences to user provided reference, outputting the alignment to a file

```bash
nextclade run path/to/sequences.fa [-r|--input-ref] path/to/reference.fa [-o|--output-fasta] path/to/alignment.fa
```

### Create a TSV report, auto-downloading the latest dataset

```bash
nextclade run path/to/fasta [-d|--dataset-name] dataset_name [-t|--output-tsv] path/to/report.tsv
```

### List all available datasets

```bash
nextclade dataset list
```

### Download the latest SARS-CoV-2 dataset

```bash
nextclade dataset get [-n|--name] sars-cov-2 [-o|--output-dir] path/to/directory
```

### Use a downloaded dataset, producing all outputs

```bash
nextclade run [-D|--input-dataset] path/to/dataset_dir [-O|--output-all] path/to/output_dir path/to/sequences.fasta
```

### Run on multiple files

```bash
nextclade run [-d|--dataset-name] dataset_name [-t|--output-tsv] path/to/output_tsv -- path/to/input_fasta_1 path/to/input_fasta_2 ...
```

### Try reverse complement if sequence does not align

```bash
nextclade run --retry-reverse-complement [-d|--dataset-name] dataset_name [-t|--output-tsv] path/to/output_tsv path/to/input_fasta
```
