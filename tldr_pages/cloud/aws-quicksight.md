# aws-quicksight

> Create, delete, list, search and update AWS QuickSight entities. More information: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

## Examples

### List datasets

```bash
aws quicksight list-data-sets --aws-account-id aws_account_id
```

### List users

```bash
aws quicksight list-users --aws-account-id aws_account_id --namespace default
```

### List groups

```bash
aws quicksight list-groups --aws-account-id aws_account_id --namespace default
```

### List dashboards

```bash
aws quicksight list-dashboards --aws-account-id aws_account_id
```

### Display detailed information about a dataset

```bash
aws quicksight describe-data-set --aws-account-id aws_account_id --data-set-id data_set_id
```

### Display who has access to the dataset and what kind of actions they can perform on the dataset

```bash
aws quicksight describe-data-set-permissions --aws-account-id aws_account_id --data-set-id data_set_id
```
