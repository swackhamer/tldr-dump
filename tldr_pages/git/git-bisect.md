# git-bisect

> Use binary search to find the commit that introduced a bug. Git automatically jumps back and forth in the commit graph to progressively narrow down the faulty commit. More information: <https://git-scm.com/docs/git-bisect>.

## Examples

### Start a bisect session on a commit range bounded by a known buggy commit, and a known clean (typically older) one

```bash
git bisect start bad_commit good_commit
```

### For each commit that `git bisect` selects, mark it as "bad" or "good" after testing it for the issue

```bash
git bisect good|bad
```

### After `git bisect` pinpoints the faulty commit, end the bisect session and return to the previous branch

```bash
git bisect reset
```

### Skip a commit during a bisect (e.g. one that fails the tests due to a different issue)

```bash
git bisect skip
```

### Display a log of what has been done so far

```bash
git bisect log
```
