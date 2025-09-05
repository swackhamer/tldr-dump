# apropos

> Search the manual pages for names and descriptions. More information: <https://manned.org/apropos>.

## Examples

### Search for a keyword using a `regex`

```bash
apropos regex
```

### Search without restricting the output to the terminal width ([l]ong output)

```bash
apropos [-l|--long] regex
```

### Search for pages that match all the `regex` given

```bash
apropos regex_1 [-a|--and] regex_2 [-a|--and] regex_3
```
