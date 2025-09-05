# wp

> The official interface to manage WordPress instances. More information: <https://developer.wordpress.org/cli/commands/>.

## Examples

### Print information about the operating system, shell, PHP, and WP-CLI (`wp`) installation

```bash
wp --info
```

### Update WP-CLI

```bash
wp cli update
```

### Download a fresh WordPress installation to current directory, optionally specifying the locale

```bash
wp core download --locale=locale
```

### Create basic `wpconfig` file (assuming database on `localhost`)

```bash
wp config create --dbname=dbname --dbuser=dbuser --dbpass=dbpass
```

### Install and activate a WordPress plugin

```bash
wp plugin install plugin --activate
```

### Replace all instances of a string in the database

```bash
wp search-replace old_string new_string
```

### Import the contents of a WordPress Extended RSS (WXR) file

```bash
wp import path/to/file.xml
```
