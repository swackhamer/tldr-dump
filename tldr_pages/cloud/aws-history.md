# aws-history

> Print the command-line history for AWS CLI commands (the record of history of AWS CLI commands must be enabled). More information: <https://docs.aws.amazon.com/cli/latest/reference/history/>.

## Examples

### List commands history with command IDs

```bash
aws history list
```

### Display events related to a specific command given a command ID

```bash
aws history show command_id
```
