# git-cvsexportcommit

> Export a single `Git` commit to a CVS checkout. More information: <https://git-scm.com/docs/git-cvsexportcommit>.

## Examples

### Merge a specific patch into CVS

```bash
git cvsexportcommit -v -c -w path/to/project_cvs_checkout commit_sha1
```
