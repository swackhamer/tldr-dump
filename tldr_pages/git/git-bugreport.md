# git-bugreport

> Captures debug information from the system and user, generating a text file to aid in the reporting of a bug in Git. More information: <https://git-scm.com/docs/git-bugreport>.

## Examples

### Create a new bug report file in the current directory

```bash
git bugreport
```

### Create a new bug report file in the specified directory, creating it if it does not exist

```bash
git bugreport [-o|--output-directory] path/to/directory
```

### Create a new bug report file with the specified filename suffix in `strftime` format

```bash
git bugreport [-s|--suffix] %m%d%y
```
