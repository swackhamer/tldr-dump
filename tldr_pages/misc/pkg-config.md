# pkg-config

> Provide the details of installed libraries for compiling applications. More information: <https://www.freedesktop.org/wiki/Software/pkg-config/>.

## Examples

### Get the list of libraries and their dependencies

```bash
pkg-config --libs library1 library2 ...
```

### Get the list of libraries, their dependencies, and proper cflags for gcc

```bash
pkg-config --cflags --libs library1 library2 ...
```

### Compile your code with libgtk-3, libwebkit2gtk-4.0 and all their dependencies

```bash
c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example
```
