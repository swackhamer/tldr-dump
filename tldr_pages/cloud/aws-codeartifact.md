# aws-codeartifact

> Manage CodeArtifact repositories, domains, packages, package versions and assets. CodeArtifact is an artifact repository compatible with popular package managers and build tools like Maven, Gradle, npm, Yarn, Twine, pip, NuGet, and SwiftPM. More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

## Examples

### List available domains for your AWS account

```bash
aws codeartifact list-domains
```

### Generate credentials for a specific package manager

```bash
aws codeartifact login --tool npm|pip|twine --domain your_domain --repository repository_name
```

### Get the endpoint URL of a CodeArtifact repository

```bash
aws codeartifact get-repository-endpoint --domain your_domain --repository repository_name --format npm|pypi|maven|nuget|generic
```

### Display help

```bash
aws codeartifact help
```

### Display help for a specific subcommand

```bash
aws codeartifact subcommand help
```
