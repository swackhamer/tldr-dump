# direnv

> Shell extension to load and unload environment variables depending on the current directory. More information: <https://github.com/direnv/direnv>.

## Examples

### Grant direnv permission to load the `.envrc` present in the current directory

```bash
direnv allow .
```

### Revoke the authorization to load the `.envrc` present in the current directory

```bash
direnv deny .
```

### Edit the `.envrc` file in the default text editor and reload the environment on exit

```bash
direnv edit .
```

### Trigger a reload of the environment

```bash
direnv reload
```

### Print some debug status information

```bash
direnv status
```
