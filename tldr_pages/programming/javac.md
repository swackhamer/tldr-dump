# javac

> Java application compiler. More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

## Examples

### Compile a `.java` file

```bash
javac path/to/file.java
```

### Compile several `.java` files

```bash
javac path/to/file1.java path/to/file2.java ...
```

### Compile all `.java` files in current directory

```bash
javac *.java
```

### Compile a `.java` file and place the resulting class file in a specific directory

```bash
javac -d path/to/directory path/to/file.java
```
