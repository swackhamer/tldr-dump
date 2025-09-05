# llvd

> Linkedin Learning Video Downloader. More information: <https://github.com/knowbee/llvd>.

## Examples

### Download a course using cookie-based authentication

```bash
llvd [-c|--course] course-slug --cookies
```

### Download a course at a specific resolution

```bash
llvd [-c|--course] course-slug [-r|--resolution] 720
```

### Download a course with captions (subtitles)

```bash
llvd [-c|--course] course-slug [-ca|--caption]
```

### Download a course path with throttling between 10 to 30 seconds

```bash
llvd [-p|--path] path-slug [-t|--throttle] 10,30 --cookies
```
