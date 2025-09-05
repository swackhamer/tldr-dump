# glib-compile-resources

> Compiles resource files (e.g. images) into a binary resource bundle. These may be linked into GTK applications using the GResource API. More information: <https://manned.org/glib-compile-resources>.

## Examples

### Compile resources referenced in `file.gresource.xml` to a .gresource binary

```bash
glib-compile-resources file.gresource.xml
```

### Compile resources referenced in `file.gresource.xml` to a C source file

```bash
glib-compile-resources --generate-source file.gresource.xml
```

### Compile resources in `file.gresource.xml` to a chosen target file, with `.c`, `.h` or `.gresource` extension

```bash
glib-compile-resources --generate --target=file.ext file.gresource.xml
```

### Print a list of resource files referenced in `file.gresource.xml`

```bash
glib-compile-resources --generate-dependencies file.gresource.xml
```
