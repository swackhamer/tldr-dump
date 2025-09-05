# mvn

> Apache Maven: build and manage Java-based projects. More information: <https://manned.org/mvn>.

## Examples

### Compile a project

```bash
mvn compile
```

### Compile and package the compiled code in its distributable format, such as a `jar`

```bash
mvn package
```

### Compile and package, skipping unit tests

```bash
mvn package [-D|--define] skipTests
```

### Install the built package in local maven repository. (This will invoke the compile and package commands too)

```bash
mvn install
```

### Delete build artifacts from the target directory

```bash
mvn clean
```

### Do a clean and then invoke the package phase

```bash
mvn clean package
```

### Clean and then package the code with a given build profile

```bash
mvn clean [-P|--activate-profiles] profile package
```

### Run a class with a main method

```bash
mvn exec:java [-D|--define] exec.mainClass="com.example.Main" [-D|--define] exec.args="argument1 argument2 ..."
```
