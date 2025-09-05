# uv-publish

> Upload distributions to an index. More information: <https://docs.astral.sh/uv/reference/cli/#uv-publish>.

## Examples

### Publish packages from `dist/` directory (default behavior)

```bash
uv publish
```

### Publish to a specific repository URL

```bash
uv publish --publish-url https://upload.pypi.org/legacy/
```

### Publish using a specific username and password

```bash
uv publish [-u|--username] username [-p|--password] password
```

### Publish using an API token

```bash
uv publish [-t|--token] your_api_token
```

### Publish specific distribution files

```bash
uv publish path/to/dist/*.whl path/to/dist/*.tar.gz
```

### Publish to TestPyPI for testing

```bash
uv publish --publish-url https://test.pypi.org/legacy/
```
