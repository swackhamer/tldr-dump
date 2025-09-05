# npm-dedupe

> Reduce duplication in the `node_modules` directory. More information: <https://docs.npmjs.com/cli/npm-dedupe>.

## Examples

### Deduplicate packages in `node_modules`

```bash
npm [ddp|dedupe]
```

### Follow `package-lock.json` or `npm-shrinkwrap.json` during deduplication

```bash
npm [ddp|dedupe] --lock
```

### Run deduplication in strict mode

```bash
npm [ddp|dedupe] --strict
```

### Skip optional/peer dependencies during deduplication

```bash
npm [ddp|dedupe] --omit optional|peer
```

### Enable detailed logging for troubleshooting

```bash
npm [ddp|dedupe] --loglevel verbose
```

### Limit deduplication to a specific package

```bash
npm [ddp|dedupe] package_name
```
