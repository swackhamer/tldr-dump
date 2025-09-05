# gh-skyline

> Generate a 3D model of your GitHub contribution history. By default, it will create a `{username}-{year}-github-skyline.stl` file in the current directory. More information: <https://github.com/github/gh-skyline>.

## Examples

### Generate a skyline STL file for the current year and authenticated user

```bash
gh skyline
```

### Generate a skyline for a specific user and year

```bash
gh skyline [-u|--user] username [-y|--year] year
```

### Generate a skyline for a range of years

```bash
gh skyline [-u|--user] username [-y|--year] first_year-last_year
```

### Generate a full skyline (from the user's join year to the current year)

```bash
gh skyline [-u|--user] username [-f|--full]
```

### Enable debug logging

```bash
gh skyline [-d|--debug]
```

### Generate a skyline and specify the output file path

```bash
gh skyline [-o|--output] path/to/output_file.stl
```

### Open the GitHub profile for a specific user

```bash
gh skyline [-u|--user] username [-w|--web]
```

### Display help

```bash
gh skyline [-h|--help]
```
