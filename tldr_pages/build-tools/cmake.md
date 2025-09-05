# cmake

> Cross-platform build automation system, that generates recipes for native build systems. More information: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

## Examples

### Generate a build recipe in the current directory with `CMakeLists.txt` from a project directory

```bash
cmake path/to/project_directory
```

### Use a generated recipe in a given directory to build artifacts

```bash
cmake --build path/to/build_directory
```

### Install the build artifacts into `/usr/local/` and strip debugging symbols

```bash
cmake --install path/to/build_directory --strip
```

### Generate a build recipe, with build type set to `Release` with CMake variable

```bash
cmake path/to/project_directory -D CMAKE_BUILD_TYPE=Release
```

### Generate a build recipe using `generator_name` as the underlying build system

```bash
cmake -G generator_name path/to/project_directory
```

### Install the build artifacts using a custom prefix for paths

```bash
cmake --install path/to/build_directory --strip --prefix path/to/directory
```

### Run a custom build target

```bash
cmake --build path/to/build_directory [-t|--target] target_name
```

### Display help

```bash
cmake [-h|--help]
```
