# jbang

> Easily create, edit and run self-contained source-only Java programs. See also: `java`. More information: <https://www.jbang.dev/documentation/jbang/latest/cli/jbang.html>.

## Examples

### Initialize a simple Java class

```bash
jbang init path/to/file.java
```

### Initialize a Java class (useful for scripting)

```bash
jbang init --template=cli path/to/file.java
```

### Use `jshell` to explore and use a script and any dependencies in a REPL editor

```bash
jbang run --interactive
```

### Setup a temporary project to edit a script in an IDE

```bash
jbang edit --open=codium|code|eclipse|idea|netbeans|gitpod path/to/script.java
```

### Run a Java code snippet (Java 9 and later)

```bash
echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);' | jbang -
```

### Run command-line application

```bash
jbang path/to/file.java command arg1 arg2 ...
```

### Install a script on the user's `$PATH`

```bash
jbang app install --name command_name path/to/script.java
```

### Install a specific version of JDK to be used with `jbang`

```bash
jbang jdk install version
```
