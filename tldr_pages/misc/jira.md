# jira

> Interface (third party) for interacting with Jira. More information: <https://github.com/ankitpokhrel/jira-cli>.

## Examples

### List recent issues

```bash
jira issue list
```

### List issues from the current sprint, assigned to me

```bash
jira sprint list --current -a$(jira me)
```

### Create a new issue, optionally set a parent issue

```bash
jira issue create --parent parent
```
