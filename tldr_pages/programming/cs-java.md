# cs-java

> The `java` and `java-home` commands fetch and install JVMs. The `java` command runs them too. More information: <https://get-coursier.io/docs/cli-java>.

## Examples

### Display Java version by using coursier

```bash
cs java -version
```

### Call a specific Java version with custom properties using coursier

```bash
cs java --jvm jvm_name:jvm_version -Xmx32m -Xanother_jvm_opt -jar path/to/jar_name.jar
```

### List all the available JVM in the coursier default index

```bash
cs java --available
```

### List all the installed JVM in the system with his own location

```bash
cs java --installed
```

### Set a specific JVM as one-off default for the shell instance

```bash
cs java --jvm jvm_name:jvm_version --env
```

### Revert the changes for the default JVM settings

```bash
eval "$(cs java --disable)"
```

### Set a specific JVM as default for the whole system

```bash
cs java --jvm jvm_name:jvm_version --setup
```
