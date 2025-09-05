# jmap

> Java memory map tool. More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jmap.html>.

## Examples

### Print shared object mappings for a Java process (output like pmap)

```bash
jmap java_pid
```

### Print heap summary information

```bash
jmap -heap filename.jar java_pid
```

### Print histogram of heap usage by type

```bash
jmap -histo java_pid
```

### Dump contents of the heap into a binary file for analysis with jhat

```bash
jmap -dump:format=b,file=path/to/file java_pid
```

### Dump live objects of the heap into a binary file for analysis with jhat

```bash
jmap -dump:live,format=b,file=path/to/file java_pid
```
