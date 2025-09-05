# git-switch

> Switch between Git branches. Requires Git version 2.23+. See also: `git checkout`. More information: <https://git-scm.com/docs/git-switch>.

## Examples

### Switch to an existing branch

```bash
git switch branch_name
```

### Create a new branch and switch to it

```bash
git switch [-c|--create] branch_name
```

### Create a new branch based on an existing commit and switch to it

```bash
git switch [-c|--create] branch_name commit
```

### Switch to the previous branch

```bash
git switch -
```

### Switch to a branch and update all submodules to match

```bash
git switch --recurse-submodules branch_name
```

### Switch to a branch and automatically merge the current branch and any uncommitted changes into it

```bash
git switch [-m|--merge] branch_name
```

### Switch to a tag

```bash
git switch [-d|--detach] tag
```
