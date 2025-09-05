# jenv

> Manage the "JAVA_HOME" environment variable. More information: <https://github.com/jenv/jenv/>.

## Examples

### Add a Java version to jEnv

```bash
jenv add path/to/jdk_home
```

### Display the current JDK version used

```bash
jenv version
```

### Display all managed JDKs

```bash
jenv versions
```

### Set the global JDK version

```bash
jenv global java_version
```

### Set the JDK version for the current shell session

```bash
jenv shell java_version
```

### Enable a jEnv plugin

```bash
jenv enable-plugin plugin_name
```
