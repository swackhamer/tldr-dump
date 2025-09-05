# ant

> Apache Ant: build and manage Java-based projects. More information: <https://ant.apache.org/manual/index.html>.

## Examples

### Build a project with default build file `build.xml`

```bash
ant
```

### Build a project using build file other than `build.xml`

```bash
ant [-f|-buildfile] buildfile.xml
```

### Print information on possible targets for this project

```bash
ant [-p|-projecthelp]
```

### Print debugging information

```bash
ant [-d|-debug]
```

### Execute all targets that do not depend on fail target(s)

```bash
ant [-k|-keep-going]
```
