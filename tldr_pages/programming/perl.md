# perl

> The Perl 5 language interpreter. More information: <https://www.perl.org>.

## Examples

### Print lines from `stdin` [m/] matching `regex1` and case insensitive [/i] `regex2`

```bash
perl -n -e 'print if m/regex1/ and m/regex2/i'
```

### Say [-E] first match group, using a `regex`, ignoring space in `regex` [/x]

```bash
perl -n -E 'say $1 if m/before ( group_regex ) after/x'
```

### [-i]n-place, with backup, [s/] substitute all occurrence [/g] of `regex` with replacement

```bash
perl -i'.bak' -p -e 's/regex/replacement/g' path/to/files
```

### Use perl's inline documentation, some pages also available via manual pages on Linux

```bash
perldoc perlrun ; perldoc module ; perldoc -f splice; perldoc -q perlfaq1
```
