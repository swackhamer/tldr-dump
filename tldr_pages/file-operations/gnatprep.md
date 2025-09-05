# gnatprep

> Preprocessor for Ada source code files (part of the GNAT toolchain). More information: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Preprocessing-with-gnatprep.html>.

## Examples

### Use symbol definitions from a file

```bash
gnatprep source_file target_file definitions_file
```

### Specify symbol values in the command-line

```bash
gnatprep -Dname=value source_file target_file
```
