# sfdk-cmake

> Executes cmake build step. More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.cmake.adoc>.

## Examples

### Run cmake

```bash
sfdk cmake
```

### Run cmake in specified project directory

```bash
sfdk cmake project
```

### Run cmake with extra arguments

```bash
sfdk cmake -- arguments
```

### Run cmake build in current directory

```bash
sfdk cmake --build .
```

### Run cmake build in current directory with extra cmake arguments

```bash
sfdk cmake --build . cmake-arguments
```

### Run cmake build in current directory with extra build tool arguments

```bash
sfdk cmake --build . -- build-tool-arguments
```
