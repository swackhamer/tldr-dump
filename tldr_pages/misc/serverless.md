# serverless

> Toolkit for deploying and operating serverless architectures on AWS, Google Cloud, Azure and IBM OpenWhisk. Commands can be run either using the `serverless` command or its alias, `sls`. More information: <https://www.serverless.com/framework/docs/providers/aws/cli-reference>.

## Examples

### Create a serverless project

```bash
serverless create
```

### Create a serverless project from a template

```bash
serverless create --template template_name
```

### Deploy to a cloud provider

```bash
serverless deploy
```

### Display information about a serverless project

```bash
serverless info
```

### Invoke a deployed function

```bash
serverless invoke -f function_name
```

### Follow the logs for a project

```bash
serverless logs [-t|--tail]
```
