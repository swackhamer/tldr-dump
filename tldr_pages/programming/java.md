# java

> Java application launcher. More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

## Examples

### Execute a Java `.class` file that contains a main method by using just the class name

```bash
java classname
```

### Execute a Java program and use additional third-party or user-defined classes

```bash
java -classpath path/to/classes1:path/to/classes2:. classname
```

### Execute a `.jar` program

```bash
java -jar filename.jar
```

### Execute a `.jar` program with debug waiting to connect on port 5005

```bash
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar filename.jar
```

### Display JDK, JRE and HotSpot versions

```bash
java -version
```

### Display help

```bash
java -help
```
