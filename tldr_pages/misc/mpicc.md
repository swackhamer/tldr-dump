# mpicc

> Open MPI C wrapper compiler. More information: <https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

## Examples

### Compile a source code file into an object file

```bash
mpicc -c path/to/file.c
```

### Link an object file and make an executable

```bash
mpicc -o executable path/to/object_file.o
```

### Compile and link source code in a single command

```bash
mpicc -o executable path/to/file.c
```
