# gendesk

> Specifies the command to generate a `.desktop` file and a download icon with minimal information. More information: <https://manned.org/gendesk>.

## Examples

### Create a `.desktop` file named `app`

```bash
gendesk -n --name "app" --exec "/path/to/app" --icon "/path/to/icon.png" --comment "This is application"
```

### Create a `.desktop` file named `app`, do not display any output, and overwrite it if it exists

```bash
gendesk -q -f -n --name "app" --exec "/path/to/app" --icon "/path/to/icon.png" --comment "This is application"
```

### Display help

```bash
gendesk [-h|--help]
```
