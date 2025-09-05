# say

> Convert text to speech. More information: <https://keith.github.io/xcode-man-pages/say.1.html>.

## Examples

### Say a phrase aloud

```bash
say "I like to ride my bike."
```

### Read a file aloud

```bash
say --input-file filename.txt
```

### Say a phrase with a custom voice and speech rate

```bash
say --voice voice --rate words_per_minute "I'm sorry Dave, I can't let you do that."
```

### List the available voices (different voices speak in different languages)

```bash
say --voice "?"
```

### Say something in Polish

```bash
say --voice Zosia "Litwo, ojczyzno moja!"
```

### Create an audio file of the spoken text

```bash
say --output-file filename.aiff "Here's to the Crazy Ones."
```
