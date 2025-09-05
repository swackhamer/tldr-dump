# jhsdb

> Attach to a Java process or launch a postmortem debugger to analyze the core dump from a crashed Java Virtual Machine. More information: <https://manned.org/jhsdb>.

## Examples

### Print stack and locks information of a Java process

```bash
jhsdb jstack --pid pid
```

### Open a core dump in interactive debug mode

```bash
jhsdb clhsdb --core path/to/core_dump --exe path/to/jdk/bin/java
```

### Start a remote debug server

```bash
jhsdb debugd --pid pid --serverid optional_unique_id
```

### Connect to a process in interactive debug mode

```bash
jhsdb clhsdb --pid pid
```
