# propelauth

> Set up PropelAuth authentication as quickly and easily as possible. More information: <https://docs.propelauth.com/reference/api/cli>.

## Examples

### Login to PropelAuth using an API Key generated from <https://auth.propelauth.com/api_keys/personal>

```bash
propelauth login
```

### Set the default PropelAuth Project for the CLI. If no default project is set, the system will prompt for selecting a Project each time certain commands are run

```bash
propelauth set-default-project
```

### Install PropelAuth authentication in an application. If no directory is provided, the current directory is used

```bash
propelauth setup [-f|--framework] path/to/directory
```

### Log the CLI out of PropelAuth

```bash
propelauth logout
```
