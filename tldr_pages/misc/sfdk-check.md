# sfdk-check

> Performs quality checks. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.cmake.adoc>.

## Examples

### Display test suites

```bash
sfdk check --list-suites
```

### Run all or essential test suites

```bash
sfdk check
```

### Add testing level to the check

```bash
sfdk check [-l|--levels] +level
```

### Remove testing level from the check

```bash
sfdk check [-l|--levels] -level
```

### Add testing suite to the check

```bash
sfdk check [-s|--suites] +suite
```

### Remove testing suite from the check

```bash
sfdk check [-s|--suites] -suite
```
