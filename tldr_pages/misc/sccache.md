# sccache

> A fast C/C++/Rust compiler cache. Composed of a client and a server, both running on the machine. More information: <https://manned.org/sccache>.

## Examples

### Show compilation statistics

```bash
sccache [-s|--show-stats]
```

### Run `gcc` (or any compiler command) through `sccache`

```bash
sccache gcc path/to/file.c
```

### Start `sccache` server in the foreground and print logs

```bash
sccache --stop-server; SCCACHE_LOG=trace SCCACHE_START_SERVER=1 SCCACHE_NO_DAEMON=1 sccache
```

### Ask scheduler for distributed compilation status

```bash
sccache --dist-status
```
