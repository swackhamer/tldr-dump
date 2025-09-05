# cloc

> Count, and compute differences of, lines of source code and comments. More information: <https://github.com/AlDanial/cloc#basic-use->.

## Examples

### Count all the lines of code in a directory

```bash
cloc path/to/directory
```

### Count all the lines of code in a directory, displaying a progress bar during the counting process

```bash
cloc --progress=1 path/to/directory
```

### Compare 2 directory structures and count the differences between them

```bash
cloc --diff path/to/directory/one path/to/directory/two
```

### Ignore files that are ignored by VCS, such as files specified in `.gitignore`

```bash
cloc --vcs git path/to/directory
```

### Count all the lines of code in a directory, displaying the results for each file instead of each language

```bash
cloc --by-file path/to/directory
```
