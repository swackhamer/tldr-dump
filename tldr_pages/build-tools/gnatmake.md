# gnatmake

> A low-level build tool for Ada programs (part of the GNAT toolchain). More information: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Switches-for-gnatmake.html>.

## Examples

### Compile an executable

```bash
gnatmake source_file1.adb source_file2.adb ...
```

### Set a custom executable name

```bash
gnatmake -o executable_name source_file.adb
```

### [f]orce recompilation

```bash
gnatmake -f source_file.adb
```
