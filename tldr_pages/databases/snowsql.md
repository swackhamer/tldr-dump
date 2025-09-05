# snowsql

> SnowSQL client for Snowflake's Data Cloud. More information: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

## Examples

### Connect to a specific instance at <https://account.snowflakecomputing.com> (password can be provided in prompt or configuration file)

```bash
snowsql --accountname account --username username --dbname database --schemaname schema
```

### Connect to an instance specified by a specific configuration file (defaults to `~/.snowsql/config`)

```bash
snowsql --config path/to/configuration_file
```

### Connect to the default instance using a token for multi-factor authentication

```bash
snowsql --mfa-passcode token
```

### Execute a single SQL query or SnowSQL command on the default connection (useful in shell scripts)

```bash
snowsql --query 'query'
```

### Execute commands from a specific file on the default connection

```bash
snowsql --filename path/to/file.sql
```
