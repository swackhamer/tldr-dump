# magento

> Manage the Magento PHP framework. More information: <https://experienceleague.adobe.com/en/docs/commerce-operations/tools/cli-reference/commerce-on-premises>.

## Examples

### Enable one or more modules

```bash
magento module:enable module1 module2 ...
```

### Disable one or more modules

```bash
magento module:disable module1 module2 ...
```

### Update the database after enabling modules

```bash
magento setup:upgrade
```

### Update code and dependency injection configuration

```bash
magento setup:di:compile
```

### Deploy static assets

```bash
magento setup:static-content:deploy
```

### Enable maintenance mode

```bash
magento maintenance:enable
```

### Disable maintenance mode

```bash
magento maintenance:disable
```

### List all available commands

```bash
magento list
```
