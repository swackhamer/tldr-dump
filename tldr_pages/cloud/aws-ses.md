# aws-ses

> CLI for AWS Simple Email Service. High-scale inbound and outbound cloud email service. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>.

## Examples

### Create a new receipt rule set

```bash
aws ses create-receipt-rule-set --rule-set-name rule_set_name --generate-cli-skeleton
```

### Describe the active receipt rule set

```bash
aws ses describe-active-receipt-rule-set --generate-cli-skeletion
```

### Describe a specific receipt rule

```bash
aws ses describe-receipt-rule --rule-set-name rule_set_name --rule-name rule_name --generate-cli-skeleton
```

### List all receipt rule sets

```bash
aws ses list-receipt-rule-sets --starting-token token_string --max-items integer --generate-cli-skeleton
```

### Delete a specific receipt rule set (the currently active rule set cannot be deleted)

```bash
aws ses delete-receipt-rule-set --rule-set-name rule_set_name --generate-cli-skeleton
```

### Delete a specific receipt rule

```bash
aws ses delete-receipt-rule --rule-set-name rule_set_name --rule-name rule_name --generate-cli-skeleton
```

### Send an email

```bash
aws ses send-email --from from_address --destination "ToAddresses=addresses" --message "Subject={Data=subject_text,Charset=utf8},Body={Text={Data=body_text,Charset=utf8},Html={Data=message_body_containing_html,Charset=utf8"
```

### Display help for a specific SES subcommand

```bash
aws ses subcommand help
```
