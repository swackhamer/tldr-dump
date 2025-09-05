# pprof

> Visualize and analyze profiling data. More information: <https://github.com/google/pprof>.

## Examples

### Generate a text report from a specific profiling file, on fibbo binary

```bash
pprof -top ./fibbo ./fibbo-profile.pb.gz
```

### Generate a graph and open it on a web browser

```bash
pprof -svg ./fibbo ./fibbo-profile.pb.gz
```

### Run pprof in interactive mode to be able to manually launch `pprof` on a file

```bash
pprof ./fibbo ./fibbo-profile.pb.gz
```

### Run a web server that serves a web interface on top of `pprof`

```bash
pprof -http=localhost:8080 ./fibbo ./fibbo-profile.pb.gz
```

### Fetch a profile from an HTTP server and generate a report

```bash
pprof http://localhost:8080/debug/pprof
```
