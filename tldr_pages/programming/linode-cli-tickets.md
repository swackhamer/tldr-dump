# linode-cli-tickets

> Manage Linode Support Tickets. See also: `linode-cli`. More information: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-account-management>.

## Examples

### List your Support Tickets

```bash
linode-cli tickets list
```

### Open a new Ticket

```bash
linode-cli tickets create --summary "Summary or quick title for the Ticket" --description "Detailed description of the issue"
```

### List replies to a Ticket

```bash
linode-cli tickets replies ticket_id
```

### Reply to a specific Ticket

```bash
linode-cli tickets reply ticket_id --description "The content of your reply"
```
