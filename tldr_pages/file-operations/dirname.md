# dirname

> Calculates the parent directory of a file or directory path. More information: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

## Examples

### Calculate the parent directory of a given path

```bash
dirname path/to/file_or_directory
```

### Calculate the parent directory of multiple paths

```bash
dirname path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Delimit output with a NUL character instead of a newline (useful when combining with `xargs`)

```bash
dirname [-z|--zero] path/to/file_or_directory1 path/to/file_or_directory2 ...
```
