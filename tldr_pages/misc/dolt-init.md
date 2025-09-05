# dolt-init

> Create an empty Dolt data repository. More information: <https://docs.dolthub.com/cli-reference/cli#dolt-init>.

## Examples

### Initialize a new Dolt data repository in the current directory

```bash
dolt init
```

### Initialize a new Dolt data repository creating a commit with the specified metadata

```bash
dolt init --name "name" --email "email" --date "2021-12-31T00:00:00" [-b|--initial-branch] "branch_name"
```
