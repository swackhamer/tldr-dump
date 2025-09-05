# cvs

> Concurrent Versions System, a revision control system. More information: <https://manned.org/cvs>.

## Examples

### Create a new repository (requires the `CVSROOT` environment variable to be set externally)

```bash
cvs -d path/to/repository init
```

### Add a project to the repository

```bash
cvs import -m "message" project_name version vendor
```

### Checkout a project

```bash
cvs checkout project_name
```

### Show changes made to files

```bash
cvs diff path/to/file
```

### Add a file

```bash
cvs add path/to/file
```

### Commit a file

```bash
cvs commit -m "message" path/to/file
```

### Update the working directory from the remote repository

```bash
cvs update
```
