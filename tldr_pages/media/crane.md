# crane

> Container images managing tool. Some subcommands such as `pull`, `push`, `copy`, etc. have their own usage documentation. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

## Examples

### Execute a `crane` subcommand

```bash
crane subcommand
```

### Allow pushing non-distributable (foreign) layers

```bash
crane --allow-nondistributable-artifacts subcommand
```

### Allow image references to be fetched without TLS

```bash
crane --insecure subcommand
```

### Specify the platform in the form `os/arch/variant:osversion` (e.g. `linux/amd64`). (default all)

```bash
crane --platform platform subcommand
```

### Enable debug logs for a subcommand

```bash
crane [-v|--verbose] subcommand
```

### Display help for a subcommand

```bash
crane [-h|--help] subcommand
```
