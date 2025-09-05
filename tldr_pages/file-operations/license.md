# license

> Create license files for open-source projects. More information: <https://nishanths.github.io/license>.

## Examples

### Print a license to `stdout`, using the defaults (auto-detected author name, and current year)

```bash
license license_name
```

### Generate a license and save it to a file

```bash
license -o path/to/file license_name
```

### List all available licenses

```bash
license ls
```

### Generate a license with custom author name and year

```bash
license --name author --year release_year license_name
```
