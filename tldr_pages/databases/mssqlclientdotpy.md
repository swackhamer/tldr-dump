# mssqlclient.py

> Connect to Microsoft SQL Server instances and execute queries. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Connect to an MSSQL server using Windows authentication

```bash
mssqlclient.py -windows-auth domain/username:password@target
```

### Connect using SQL server authentication

```bash
mssqlclient.py username:password@target
```

### Connect using pass-the-hash authentication

```bash
mssqlclient.py domain/username@target -hashes LM_Hash:NT_Hash
```

### Connect using Kerberos authentication (requires valid tickets)

```bash
mssqlclient.py -k domain/username@target
```

### Execute a specific SQL command upon connection

```bash
mssqlclient.py username:password@target -query "SELECT user_name();"
```

### Execute multiple SQL commands from a file

```bash
mssqlclient.py username:password@target -file path/to/sql_file.sql
```

### Connect to a specific database instance (default is `None`)

```bash
mssqlclient.py username:password@target -db database_name
```

### Display SQL queries before execution

```bash
mssqlclient.py username:password@target -show
```
