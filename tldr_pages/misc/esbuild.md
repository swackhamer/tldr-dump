# esbuild

> JavaScript bundler and minifier built for speed. More information: <https://esbuild.github.io/api/#general-options>.

## Examples

### Bundle a JavaScript application and print to `stdout`

```bash
esbuild --bundle path/to/file.js
```

### Bundle a JSX application from `stdin`

```bash
esbuild --bundle --outfile=path/to/out.js < path/to/file.jsx
```

### Bundle and minify a JSX application with source maps in `production` mode

```bash
esbuild --bundle --define:process.env.NODE_ENV=\"production\" --minify --sourcemap path/to/file.js
```

### Bundle a JSX application for a comma-separated list of browsers

```bash
esbuild --bundle --minify --sourcemap --target=chrome58,firefox57,safari11,edge16 path/to/file.jsx
```

### Bundle a JavaScript application for a specific node version

```bash
esbuild --bundle --platform=node --target=node12 path/to/file.js
```

### Bundle a JavaScript application enabling JSX syntax in `.js` files

```bash
esbuild --bundle app.js --loader:.js=jsx path/to/file.js
```

### Bundle and serve a JavaScript application on an HTTP server

```bash
esbuild --bundle --serve=port --outfile=index.js path/to/file.js
```

### Bundle a list of files to an output directory

```bash
esbuild --bundle --outdir=path/to/output_directory path/to/file1 path/to/file2 ...
```
