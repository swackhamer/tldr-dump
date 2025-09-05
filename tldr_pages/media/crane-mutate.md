# crane-mutate

> Modify image labels and annotations. The container must be pushed to a registry, and the manifest is updated there. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>.

## Examples

### New annotations to set (default [])

```bash
crane mutate [-a|--annotation]/[-l|--label] annotation/label
```

### Path to tarball/command/entrypoint/environment variable/exposed-ports to append to image

```bash
crane mutate --append/--cmd/--entrypoint/[-e|--env]/--exposed-ports var1 var2 ...
```

### Path to new tarball of resulting image

```bash
crane mutate [-o|--output] path/to/tarball
```

### Repository in the form `os/arch/variant:osversion,platform` to push mutated image

```bash
crane mutate --set-platform platform_name
```

### New tag reference to apply to mutated image

```bash
crane mutate [-t|--tag] tag_name
```

### New user to set

```bash
crane mutate [-u|--user] username
```

### New working dir to set

```bash
crane mutate [-w|--workdir] path/to/workdir
```

### Display help

```bash
crane mutate [-h|--help]
```
