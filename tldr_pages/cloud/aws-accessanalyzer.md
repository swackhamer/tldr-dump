# aws-accessanalyzer

> Analyze and review resource policies to identify potential security risks. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

## Examples

### Create a new Access Analyzer

```bash
aws accessanalyzer create-analyzer --analyzer-name analyzer_name --type type --tags tags
```

### Delete an existing Access Analyzer

```bash
aws accessanalyzer delete-analyzer --analyzer-arn analyzer_arn
```

### Get details of a specific Access Analyzer

```bash
aws accessanalyzer get-analyzer --analyzer-arn analyzer_arn
```

### List all Access Analyzers

```bash
aws accessanalyzer list-analyzers
```

### Update settings of an Access Analyzer

```bash
aws accessanalyzer update-analyzer --analyzer-arn analyzer_arn --tags new_tags
```

### Create a new Access Analyzer archive rule

```bash
aws accessanalyzer create-archive-rule --analyzer-arn analyzer_arn --rule-name rule_name --filter filter
```

### Delete an Access Analyzer archive rule

```bash
aws accessanalyzer delete-archive-rule --analyzer-arn analyzer_arn --rule-name rule_name
```

### List all Access Analyzer archive rules

```bash
aws accessanalyzer list-archive-rules --analyzer-arn analyzer_arn
```
