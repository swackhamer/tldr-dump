# java_home

> Return a value for $JAVA_HOME or execute command using this variable. More information: <https://www.unix.com/man-page/osx/1/java_home>.

## Examples

### List JVMs based on a specific version

```bash
java_home --version 1.5+
```

### List JVMs based on a specific [arch]itecture

```bash
java_home --arch i386
```

### List JVMs based on a specific tasks (defaults to `CommandLine`)

```bash
java_home --datamodel Applets|WebStart|BundledApp|JNI|CommandLine
```

### List JVMs in a XML format

```bash
java_home --xml
```

### Display help

```bash
java_home --help
```
