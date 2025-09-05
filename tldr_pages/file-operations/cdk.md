# cdk

> A CLI for AWS Cloud Development Kit (CDK). More information: <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>.

## Examples

### List the stacks in the app

```bash
cdk ls
```

### Synthesize and print the CloudFormation template for the specified stack(s)

```bash
cdk synth stack_name
```

### Deploy one or more stacks

```bash
cdk deploy stack_name1 stack_name2 ...
```

### Destroy one or more stacks

```bash
cdk destroy stack_name1 stack_name2 ...
```

### Compare the specified stack with the deployed stack or a local CloudFormation template

```bash
cdk diff stack_name
```

### Create a new CDK project in the current directory for a specified language

```bash
cdk init [-l|--language] language
```

### Open the CDK API reference in your browser

```bash
cdk docs
```
