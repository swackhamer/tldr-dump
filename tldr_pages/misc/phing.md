# phing

> A PHP build tool based on Apache Ant. More information: <https://www.phing.info/guide/chunkhtml/ch03s03.html>.

## Examples

### Perform the default task in the `build.xml` file

```bash
phing
```

### Initialize a new build file

```bash
phing [-i|--init] path/to/build.xml
```

### Perform a specific task

```bash
phing task_name
```

### Use the given build file path

```bash
phing [-f|-buildfile] path/to/build.xml task_name
```

### Log to the given file

```bash
phing -logfile path/to/log_file task_name
```

### Use custom properties in the build

```bash
phing -Dproperty=value task_name
```

### Specify a custom listener class

```bash
phing -listener class_name task_name
```

### Build using verbose output

```bash
phing -verbose task_name
```
