# hut

> A CLI tool for sourcehut. More information: <https://manned.org/hut>.

## Examples

### Initialize `hut`'s configuration file (this will prompt for an OAuth2 access token, which is required to use `hut`)

```bash
hut init
```

### List Git/Mercurial repositories

```bash
hut git|hg list
```

### Create a public Git/Mercurial repository

```bash
hut git|hg create name
```

### List jobs on <https://builds.sr.ht>

```bash
hut builds list
```

### Show the status of a job

```bash
hut builds show job_id
```

### SSH into a job container

```bash
hut ssh job_id
```
