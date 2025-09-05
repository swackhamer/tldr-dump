# doppler-secrets

> Manage your Doppler project's secrets. More information: <https://docs.doppler.com/docs/accessing-secrets>.

## Examples

### Get all secrets

```bash
doppler secrets
```

### Get value(s) of one or more secrets

```bash
doppler secrets get secrets
```

### Upload a secrets file

```bash
doppler secrets upload path/to/file.env
```

### Delete value(s) of one or more secrets

```bash
doppler secrets delete secrets
```

### Download secrets as `.env`

```bash
doppler secrets download --format=env --no-file > path/to/.env
```
