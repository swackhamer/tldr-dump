# mpirun

> Execute serial and parallel jobs in Open MPI. See also: `mpic++`. More information: <https://docs.open-mpi.org/en/main/man-openmpi/man1/mpirun.1.html>.

## Examples

### Execute an Open MPI program

```bash
mpirun path/to/executable
```

### Execute an Open MPI program with `n` parallel processes

```bash
mpirun -n n path/to/executable
```

### Allow more processes than available physical cores

```bash
mpirun -oversubscribe path/to/executable
```
