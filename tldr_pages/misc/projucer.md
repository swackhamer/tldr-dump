# projucer

> A project manager for JUCE framework applications. More information: <https://docs.juce.com/master/projucer_manual.html#projucer_manual_tools_command_line_tools>.

## Examples

### Display information about a project

```bash
Projucer --status path/to/project_file
```

### Resave all files and resources in a project

```bash
Projucer --resave path/to/project_file
```

### Update the version number in a project

```bash
Projucer --set-version version_number path/to/project_file
```

### Generate a JUCE project from a PIP file

```bash
Projucer --create-project-from-pip path/to/PIP path/to/output
```

### Remove all JUCE-style comments (`//=====`, `//-----` or `///////`)

```bash
Projucer --tidy-divider-comments path/to/target_folder
```

### Display help

```bash
Projucer --help
```
