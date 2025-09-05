# jstack

> Java stack trace tool. More information: <https://manned.org/jstack>.

## Examples

### Print Java stack traces for all threads in a Java process

```bash
jstack java_pid
```

### Print mixed mode (Java/C++) stack traces for all threads in a Java process

```bash
jstack -m java_pid
```

### Print stack traces from Java core dump

```bash
jstack /usr/bin/java file.core
```
