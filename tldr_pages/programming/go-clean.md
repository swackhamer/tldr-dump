# go-clean

> Remove object files and cached files. More information: <https://pkg.go.dev/cmd/go#hdr-Remove_object_files_and_cached_files>.

## Examples

### Print the remove commands instead of actually removing anything

```bash
go clean -n
```

### Delete the build cache

```bash
go clean -cache
```

### Delete all cached test results

```bash
go clean -testcache
```

### Delete the module cache

```bash
go clean -modcache
```
