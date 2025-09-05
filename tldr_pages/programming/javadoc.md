# javadoc

> Generate Java API documentation in HTML format from source code. More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javadoc.html>.

## Examples

### Generate documentation for Java source code and save the result in a directory

```bash
javadoc -d path/to/directory/ path/to/java_source_code
```

### Generate documentation with a specific encoding

```bash
javadoc -docencoding UTF-8 path/to/java_source_code
```

### Generate documentation excluding some packages

```bash
javadoc -exclude package_list path/to/java_source_code
```
