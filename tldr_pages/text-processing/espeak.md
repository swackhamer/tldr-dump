# espeak

> Use text-to-speech to speak through the default sound device. More information: <https://espeak.sourceforge.net>.

## Examples

### Speak a phrase aloud

```bash
espeak "I like to ride my bike."
```

### Speak a file aloud

```bash
espeak -f path/to/file
```

### Save output to a WAV audio file, rather than speaking it directly

```bash
espeak -w filename.wav "It's GNU plus Linux"
```

### Use a different voice

```bash
espeak -v voice
```
