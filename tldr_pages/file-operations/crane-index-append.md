# crane-index-append

> Append manifest to a remote index. This sub-command pushes an index based on an (optional) base index, with appended manifests. The platform for appended manifests is inferred from the configuration file or omitted if that is infeasible. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>.

## Examples

### Append manifest to a remote index

```bash
crane index append
```

### Reference to manifests to append to the base index

```bash
crane index append [-m|--manifest] manifest_name1 manifest_name2 ...
```

### Tag to apply to resulting image

```bash
crane index append [-t|--tag] tag_name
```

### Empty base index will have Docker media types instead of OCI

```bash
crane index append --docker-empty-base
```

### Append each of its children rather than the index itself (defaults true)

```bash
crane index append --flatten
```

### Display help

```bash
crane index append [-h|--help]
```
