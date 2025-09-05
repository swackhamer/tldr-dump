# gprbuild

> A high-level build tool for projects written in Ada and other languages (C/C++/Fortran). More information: <https://docs.adacore.com/gprbuild-docs/html/gprbuild_ug.html>.

## Examples

### Build a project (assuming only one `*.gpr` file exists in the current directory)

```bash
gprbuild
```

### Build a specific [P]roject file

```bash
gprbuild -P project_name
```

### Clean up the build workspace

```bash
gprclean
```

### Install compiled binaries

```bash
gprinstall --prefix path/to/installation/dir
```
