# git-flow

> A collection of Git extensions to provide high-level repository operations. More information: <https://github.com/nvie/gitflow>.

## Examples

### Initialize it inside an existing Git repository

```bash
git flow init
```

### Start developing on a feature branch based on `develop`

```bash
git flow feature start feature
```

### Finish development on a feature branch, merging it into the `develop` branch and deleting it

```bash
git flow feature finish feature
```

### Publish a feature to the remote server

```bash
git flow feature publish feature
```

### Get a feature published by another user

```bash
git flow feature pull origin feature
```
