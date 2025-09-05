# zig

> The Zig compiler and toolchain. More information: <https://ziglang.org>.

## Examples

### Compile the project in the current directory

```bash
zig build
```

### Compile and run the project in the current directory

```bash
zig build run
```

### Initialize a `zig build` project with library and executable

```bash
zig init
```

### Create and run a test build

```bash
zig test path/to/file.zig
```

### Cross compile, build and run a project for `x86_64` architecture and `windows` operating system

```bash
zig build run -fwine -Dtarget=x86_64-windows
```

### Reformat Zig source into canonical form

```bash
zig fmt path/to/file.zig
```

### Translate a C file to `zig`

```bash
zig translate-c -lc path/to/file.c
```

### Use Zig as a drop-in C++ compiler

```bash
zig c++ path/to/file.cpp
```
