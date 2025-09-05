# yadm

> A dotfiles manager that works by using `git`. Some subcommands such as `init`, `clone`, `push`, and `pull` have their own usage documentation. More information: <https://yadm.io/docs/overview>.

## Examples

### Override the `yadm` directory. `yadm` stores its configurations relative to this directory

```bash
yadm --yadm-dir
```

### Override the `yadm` data directory: `yadm` stores its data relative to this directory

```bash
yadm --yadm-data
```

### Override the location of the `yadm` repository

```bash
yadm --yadm-repo
```

### Override the location of the `yadm` configuration file

```bash
yadm --yadm-config
```

### Override the location of the `yadm` encryption configuration

```bash
yadm --yadm-encrypt
```

### Override the location of the `yadm` encrypted files archive

```bash
yadm --yadm-archive
```

### Override the location of the `yadm` bootstrap program

```bash
yadm --yadm-bootstrap
```
