# tlmgr-search

> Search for TeX Live packages using (Perl) `regex`. More information: <https://www.tug.org/texlive/doc/tlmgr.html#search>.

## Examples

### Search for a package name and descriptions of all locally installed packages from a specific `regex`

```bash
tlmgr search "regex"
```

### Search for all file names of all locally installed packages from a `regex`

```bash
tlmgr search --file "regex"
```

### Search for all file names, package names, and descriptions of all locally installed packages from a `regex`

```bash
tlmgr search --all "regex"
```

### Search the TeX Live database, instead of the local installation

```bash
tlmgr search --global "regex"
```

### Restrict the matches for package names and descriptions (but not for file names) to whole words

```bash
tlmgr search --all --word "regex"
```
