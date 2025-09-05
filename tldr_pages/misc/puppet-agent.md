# puppet-agent

> Retrieves the client configuration from a Puppet server and applies it to the local host. More information: <https://github.com/puppetlabs/puppet/blob/main/references/man/agent.md>.

## Examples

### Register a node at a Puppet server and apply the received catalog

```bash
puppet agent --test --server puppetserver_fqdn --serverport port --waitforcert poll_time
```

### Run the agent in the background (uses settings from `puppet.conf`)

```bash
puppet agent
```

### Run the agent once in the foreground, then exit

```bash
puppet agent --test
```

### Run the agent in dry-mode

```bash
puppet agent --test --noop
```

### Log every resource being evaluated (even if nothing is being changed)

```bash
puppet agent --test --evaltrace
```

### Disable the agent

```bash
puppet agent --disable "message"
```

### Enable the agent

```bash
puppet agent --enable
```
