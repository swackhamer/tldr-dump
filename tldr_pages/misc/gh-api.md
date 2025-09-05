# gh-api

> Make authenticated HTTP requests to the GitHub API and print the response. More information: <https://cli.github.com/manual/gh_api>.

## Examples

### Display the releases for the current repository in JSON format

```bash
gh api repos/:owner/:repo/releases
```

### Create a reaction for a specific issue

```bash
gh api [-H|--header] Accept:application/vnd.github.squirrel-girl-preview+json [-f|--raw-field] 'content=+1' repos/:owner/:repo/issues/123/reactions
```

### Display the result of a GraphQL query in JSON format

```bash
gh api graphql [-f|--field] name=':repo' [-f|--raw-field] 'query'
```

### Send a request using a custom HTTP method

```bash
gh api [-X|--method] POST endpoint
```

### Include the HTTP response headers in the output

```bash
gh api [-i|--include] endpoint
```

### Do not print the response body

```bash
gh api --silent endpoint
```

### Send a request to a specific GitHub Enterprise Server

```bash
gh api --hostname github.example.com endpoint
```

### Display the subcommand help

```bash
gh api --help
```
