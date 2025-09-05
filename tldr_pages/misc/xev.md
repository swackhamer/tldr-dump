# xev

> Print contents of X events. More information: <https://gitlab.freedesktop.org/xorg/app/xev>.

## Examples

### Monitor all occurring X events

```bash
xev
```

### Monitor all X events of the root window instead of creating a new one

```bash
xev -root
```

### Monitor all X events of a particular window

```bash
xev -id window_id
```

### Monitor X events from a given category (can be specified multiple times)

```bash
xev -event event_category
```
