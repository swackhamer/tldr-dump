# ts-node

> Run TypeScript code directly, without any compiling. More information: <https://typestrong.org/ts-node>.

## Examples

### Execute a TypeScript file without compiling (`node` + `tsc`)

```bash
ts-node path/to/file.ts
```

### Execute a TypeScript file without loading `tsconfig.json`

```bash
ts-node --skip-project path/to/file.ts
```

### Evaluate TypeScript code passed as a literal

```bash
ts-node --eval 'console.log("Hello World")'
```

### Execute a TypeScript file in script mode

```bash
ts-node --script-mode path/to/file.ts
```

### Transpile a TypeScript file to JavaScript without executing it

```bash
ts-node --transpile-only path/to/file.ts
```

### Display help

```bash
ts-node --help
```
