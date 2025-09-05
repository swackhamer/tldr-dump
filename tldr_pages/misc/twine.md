# twine

> Utility for publishing Python packages on PyPI. More information: <https://twine.readthedocs.io/en/stable/#commands>.

## Examples

### Upload to PyPI

```bash
twine upload dist/*
```

### Upload to the Test PyPI repository to verify things look right

```bash
twine upload [-r|--repository] testpypi dist/*
```

### Upload to PyPI with a specified username and password

```bash
twine upload [-u|--username] username [-p|--password] password dist/*
```

### Upload to an alternative repository URL

```bash
twine upload --repository-url repository_url dist/*
```

### Check that your distribution's long description should render correctly on PyPI

```bash
twine check dist/*
```

### Upload using a specific pypirc configuration file

```bash
twine upload --config-file configuration_file dist/*
```

### Continue uploading files if one already exists (only valid when uploading to PyPI)

```bash
twine upload --skip-existing dist/*
```

### Upload to PyPI showing detailed information

```bash
twine upload --verbose dist/*
```
