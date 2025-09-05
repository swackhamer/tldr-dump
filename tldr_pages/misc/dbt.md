# dbt

> A tool to model transformations in data warehouses. More information: <https://github.com/dbt-labs/dbt-core>.

## Examples

### Debug the dbt project and the connection to the database

```bash
dbt debug
```

### Run all models of the project

```bash
dbt run
```

### Run all tests of `example_model`

```bash
dbt test --select example_model
```

### Build (load seeds, run models, snapshots, and tests associated with) `example_model` and its downstream dependents

```bash
dbt build --select example_model+
```

### Build all models, except the ones with the tag `not_now`

```bash
dbt build --exclude "tag:not_now"
```

### Build all models with tags `one` and `two`

```bash
dbt build --select "tag:one,tag:two"
```

### Build all models with tags `one` or `two`

```bash
dbt build --select "tag:one tag:two"
```
