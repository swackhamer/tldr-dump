# pipenv

> Simple and unified Python development workflow. Manage packages and the virtual environment for a project. More information: <https://pypi.org/project/pipenv>.

## Examples

### Create a new project

```bash
pipenv
```

### Create a new project using Python 3

```bash
pipenv --three
```

### Install a package

```bash
pipenv install package
```

### Install all the dependencies for a project

```bash
pipenv install
```

### Install all the dependencies for a project (including dev packages)

```bash
pipenv install --dev
```

### Uninstall a package

```bash
pipenv uninstall package
```

### Start a shell within the created virtual environment

```bash
pipenv shell
```

### Generate a `requirements.txt` (list of dependencies) for a project

```bash
pipenv lock --requirements
```
