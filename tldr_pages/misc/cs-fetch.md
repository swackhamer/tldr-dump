# cs-fetch

> Fetch fetches the JARs of dependencies. More information: <https://get-coursier.io/docs/cli-fetch>.

## Examples

### Fetch a specific version of a jar

```bash
cs fetch group_id:artifact_id:artifact_version
```

### Fetch a package and evaluate the classpath corresponding to the selected package in an env var

```bash
CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"
```

### Fetch a source of a specific jar

```bash
cs fetch --sources group_id:artifact_id:artifact_version
```

### Fetch the javadoc jars

```bash
cs fetch --javadoc group_id:artifact_id:artifact_version
```

### Fetch dependency with javadoc jars and source jars

```bash
cs fetch --default=true --sources --javadoc group_id:artifact_id:artifact_version
```

### Fetch jars coming from dependency files

```bash
cs fetch --dependency-file path/to/file1 --dependency-file path/to/file2 ...
```
