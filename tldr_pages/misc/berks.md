# berks

> Chef cookbook dependency manager. More information: <https://docs.chef.io/berkshelf.html>.

## Examples

### Install cookbook dependencies into a local repo

```bash
berks install
```

### Update a specific cookbook and its dependencies

```bash
berks update cookbook
```

### Upload a cookbook to the Chef server

```bash
berks upload cookbook
```

### View the dependencies of a cookbook

```bash
berks contingent cookbook
```
