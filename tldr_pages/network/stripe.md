# stripe

> Interact with a Stripe account. More information: <https://docs.stripe.com/stripe-cli>.

## Examples

### Follow the logs of activity on the account

```bash
stripe logs tail
```

### Listen for events, filtering on events with the name `charge.succeeded` and forwarding them to localhost:3000/events

```bash
stripe listen --events="charge.succeeded" --forward-to="localhost:3000/events"
```

### Send a test webhook event

```bash
stripe trigger charge.succeeded
```

### Create a customer

```bash
stripe customers create --email="test@example.com" --name="Jenny Rosen"
```

### Print to JSON

```bash
stripe listen --print-json
```
