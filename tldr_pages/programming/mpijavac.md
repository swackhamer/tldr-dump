# mpijavac

> Open MPI compiler wrapper for Java. See also: `mpirun`. More information: <https://docs.open-mpi.org/en/main/features/java.html#building-java-mpi-applications>.

## Examples

### Compile a Java source file

```bash
mpijavac path/to/source_file.java
```

### Pass application-specific classpaths to compiler

```bash
mpijavac -cp path/to/my/app.jar path/to/source_file.java
```

### Show the flags necessary to build MPI Java applications

```bash
mpijavac --showme
```

### Show the flags necessary to compile MPI Java applications

```bash
mpijavac --showme:compile
```

### Show full invoked Java compiler command line

```bash
mpijavac path/to/source_file.java --showme
```
