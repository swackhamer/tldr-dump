# distcc

> Distributed C/C++/ObjC compilation client that works with `distccd`. More information: <https://manned.org/distcc>.

## Examples

### Compile a source file using a compiler like `gcc`

```bash
distcc gcc -c path/to/source.c -o path/to/output.o
```

### Set remote hosts to distribute compilation

```bash
export DISTCC_HOSTS="localhost ip1 ip2 ..."
```

### Compile a project with `make` using `distcc`

```bash
make [-j|--jobs] parallel_jobs CC="distcc gcc"
```

### Show the list of current `distcc` hosts

```bash
distcc --show-hosts
```

### Display help

```bash
distcc --help
```

### Display version

```bash
distcc --version
```
