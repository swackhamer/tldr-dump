# git-svn

> Bidirectional operation between a Subversion repository and Git. More information: <https://git-scm.com/docs/git-svn>.

## Examples

### Clone an SVN repository

```bash
git svn clone https://example.com/subversion_repo local_dir
```

### Clone an SVN repository starting at a given revision number

```bash
git svn clone [-r|--revision] 1234:HEAD https://svn.example.net/subversion/repo local_dir
```

### Update local clone from the remote SVN repository

```bash
git svn rebase
```

### Fetch updates from the remote SVN repository without changing the Git HEAD

```bash
git svn fetch
```

### Commit back to the SVN repository

```bash
git svn commit
```
