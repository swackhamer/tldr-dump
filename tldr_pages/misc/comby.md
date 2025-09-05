# comby

> Tool for structural code search and replace that supports many languages. More information: <https://github.com/comby-tools/comby>.

## Examples

### Match and rewrite templates, and print changes

```bash
comby 'assert_eq!(:[a], :[b])' 'assert_eq!(:[b], :[a])' .rs
```

### Match and rewrite with rewrite properties

```bash
comby 'assert_eq!(:[a], :[b])' 'assert_eq!(:[b].Capitalize, :[a])' .rs
```

### Match and rewrite in-place

```bash
comby -in-place 'match_pattern' 'rewrite_pattern'
```

### Only perform matching and print matches

```bash
comby -match-only 'match_pattern' ""
```
