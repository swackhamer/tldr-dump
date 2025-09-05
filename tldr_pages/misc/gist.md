# gist

> Upload code to <https://gist.github.com>. More information: <https://github.com/defunkt/gist>.

## Examples

### Log in to gist on this computer

```bash
gist --login
```

### Create a gist from any number of text files

```bash
gist file.txt file2.txt
```

### Create a private gist with a description

```bash
gist --private --description "A meaningful description" file.txt
```

### Read contents from `stdin` and create a gist from it

```bash
echo "hello world" | gist
```

### List your public and private gists

```bash
gist --list
```

### List all public gists for any user

```bash
gist --list username
```

### Update a gist using the ID from URL

```bash
gist --update GIST_ID file.txt
```
