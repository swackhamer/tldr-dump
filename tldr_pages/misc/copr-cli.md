# copr-cli

> Interface with Fedora-Projects copr instance for building RPMs and publishing them. More information: <https://manned.org/copr-cli>.

## Examples

### Show user logged in to copr

```bash
copr-cli whoami
```

### Build a local spec file on copr

```bash
copr-cli build repository path/to/spec_file
```

### Check status of builds

```bash
copr-cli list-builds repository
```

### Trigger a copr build of a spec-file from public (Git) repository

```bash
copr-cli buildscm repository --clone-url https://git.example.org/repo --spec spec_file_name
```
