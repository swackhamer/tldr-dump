# jar

> Java applications/libraries packager. More information: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

## Examples

### Recursively archive all files in the current directory into a .jar file

```bash
jar cf file.jar *
```

### Unzip .jar/.war file to the current directory

```bash
jar -xvf file.jar
```

### List a .jar/.war file content

```bash
jar tf path/to/file.jar
```

### List a .jar/.war file content with verbose output

```bash
jar tvf path/to/file.jar
```
