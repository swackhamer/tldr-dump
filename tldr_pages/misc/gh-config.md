# gh-config

> Change configuration for GitHub cli. More information: <https://cli.github.com/manual/gh_config>.

## Examples

### Display what Git protocol is being used

```bash
gh config get git_protocol
```

### Set protocol to SSH

```bash
gh config set git_protocol ssh
```

### Use `delta` in side-by-side mode as the default pager for all `gh` commands

```bash
gh config set pager 'delta --side-by-side'
```

### Set text editor to Vim

```bash
gh config set editor vim
```

### Reset to default text editor

```bash
gh config set editor ""
```

### Disable interactive prompts

```bash
gh config set prompt disabled
```

### Set a specific configuration value

```bash
gh config set key value
```
