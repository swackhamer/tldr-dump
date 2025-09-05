# satis

> The utility for the Satis static Composer repository. More information: <https://github.com/composer/satis>.

## Examples

### Initialize a Satis configuration

```bash
satis init satis.json
```

### Add a VCS repository to the Satis configuration

```bash
satis add repository_url
```

### Build the static output from the configuration

```bash
satis build satis.json path/to/output_directory
```

### Build the static output by updating only the specified repository

```bash
satis build --repository-url repository_url satis.json path/to/output_directory
```

### Remove useless archive files

```bash
satis purge satis.json path/to/output_directory
```
