# crane-registry

> This command serves a registry implementation on an automatically chosen port (:0), $PORT or --address. The command blocks while the server accepts pushes and pulls and contents are can be stored in memory, and disk. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_registry_serve.md>.

## Examples

### Serve a registry implementation

```bash
crane registry serve
```

### Address to listen on

```bash
crane registry serve --address address_name
```

### Path to a directory where blobs will be stored

```bash
crane registry serve --disk path/to/store_dir
```

### Display help for `crane registry`

```bash
crane registry [-h|--help]
```

### Display help for `crane registry serve`

```bash
crane registry serve [-h|--help]
```
