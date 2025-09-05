# box

> A PHP application for building and managing Phars. More information: <https://github.com/box-project/box>.

## Examples

### Compile a new Phar file

```bash
box compile
```

### Compile a new Phar file using a specific configuration file

```bash
box compile [-c|--config] path/to/config
```

### Display information about the PHAR PHP extension

```bash
box info
```

### Display information about a specific Phar file

```bash
box info path/to/phar_file
```

### Validate the first found configuration file in the working directory

```bash
box validate
```

### Verify the signature of a specific Phar file

```bash
box verify path/to/phar_file
```

### Display help

```bash
box help
```
