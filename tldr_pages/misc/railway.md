# railway

> Connect code to a Railway project. More information: <https://docs.railway.com/reference/cli-api>.

## Examples

### Login to a Railway account

```bash
railway login
```

### Link to an existing Project under a Railway account or team

```bash
railway link projectId
```

### Create a new project

```bash
railway init
```

### Run a local command using variables from the active environment

```bash
railway run cmd
```

### Deploy the linked project directory (if running from a subdirectory, the project root is still deployed)

```bash
railway up
```

### Open an interactive shell to a database

```bash
railway connect
```
