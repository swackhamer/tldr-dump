# aws-lambda

> Use AWS Lambda, a compute service for running code without provisioning or managing servers. More information: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

## Examples

### Run a function

```bash
aws lambda invoke --function-name name path/to/response.json
```

### Run a function with an input payload in JSON format

```bash
aws lambda invoke --function-name name --payload json path/to/response.json
```

### List functions

```bash
aws lambda list-functions
```

### Display the configuration of a function

```bash
aws lambda get-function-configuration --function-name name
```

### List function aliases

```bash
aws lambda list-aliases --function-name name
```

### Display the reserved concurrency configuration for a function

```bash
aws lambda get-function-concurrency --function-name name
```

### List which AWS services can invoke the function

```bash
aws lambda get-policy --function-name name
```
