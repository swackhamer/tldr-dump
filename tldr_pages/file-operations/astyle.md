# astyle

> Source code indenter, formatter, and beautifier for the C, C++, C# and Java programming languages. Upon running, a copy of the original file is created with an ".orig" appended to the original file name. More information: <https://astyle.sourceforge.net>.

## Examples

### Apply the default style of 4 spaces per indent and no formatting changes

```bash
astyle source_file
```

### Apply the Java style with attached braces

```bash
astyle --style=java path/to/file
```

### Apply the allman style with broken braces

```bash
astyle --style=allman path/to/file
```

### Apply a custom indent using spaces. Choose between 2 and 20 spaces

```bash
astyle --indent=spaces=number_of_spaces path/to/file
```

### Apply a custom indent using tabs. Choose between 2 and 20 tabs

```bash
astyle --indent=tab=number_of_tabs path/to/file
```
