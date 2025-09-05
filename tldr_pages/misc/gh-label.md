# gh-label

> Work with GitHub labels. More information: <https://cli.github.com/manual/gh_label>.

## Examples

### List labels for the repository in the current directory

```bash
gh label list
```

### View labels for the repository in the current directory in the default web browser

```bash
gh label list [-w|--web]
```

### Create a label with a specific name, description and color in hexadecimal format for the repository in the current directory

```bash
gh label create name [-d|--description] "description" [-c|--color] color_hex
```

### Delete a label for the repository in the current directory, prompting for confirmation

```bash
gh label delete name
```

### Update the name and description for a specific label for the repository in the current directory

```bash
gh label edit name [-n|--name] new_name [-d|--description] "description"
```

### Clone labels from a specific repository into the repository in the current directory

```bash
gh label clone owner/repository
```

### Display help for a subcommand

```bash
gh label subcommand --help
```
