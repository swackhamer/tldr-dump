# hive

> CLI tool for Apache Hive. More information: <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>.

## Examples

### Start a Hive interactive shell

```bash
hive
```

### Run HiveQL

```bash
hive -e "hiveql_query"
```

### Run a HiveQL file with a variable substitution

```bash
hive [-d|--define] key=value -f path/to/file.sql
```

### Run a HiveQL with HiveConfig (e.g. `mapred.reduce.tasks=32`)

```bash
hive --hiveconf conf_name=conf_value
```
