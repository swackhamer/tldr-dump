# sbt

> Build tool for Scala and Java projects. More information: <https://www.scala-sbt.org/1.x/docs/>.

## Examples

### Start a REPL (interactive shell)

```bash
sbt
```

### Create a new Scala project from an existing Giter8 template hosted on GitHub

```bash
sbt new scala/hello-world.g8
```

### Compile and run all tests

```bash
sbt test
```

### Delete all generated files in the `target` directory

```bash
sbt clean
```

### Compile the main sources in `src/main/scala` and `src/main/java` directories

```bash
sbt compile
```

### Use the specified version of sbt

```bash
sbt -sbt-version version
```

### Use a specific jar file as the sbt launcher

```bash
sbt -sbt-jar path
```

### List all sbt options

```bash
sbt -h
```
