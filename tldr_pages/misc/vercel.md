# vercel

> Deploy and manage your Vercel deployments. More information: <https://vercel.com/docs/cli>.

## Examples

### Deploy the current directory

```bash
vercel
```

### Deploy the current directory to production

```bash
vercel --prod
```

### Deploy a directory

```bash
vercel path/to/project
```

### Initialize an example project

```bash
vercel init
```

### Deploy with environment variables

```bash
vercel [-e|--env] ENV=var
```

### Build with environment variables

```bash
vercel [-b|--build-env] ENV=var
```

### Set default regions to enable the deployment on

```bash
vercel --regions region_id
```

### Remove a deployment

```bash
vercel remove project_name
```
