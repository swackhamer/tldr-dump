# fio

> Flexible I/O tester: do an I/O action spawning multiple threads or processes. More information: <https://fio.readthedocs.io/en/latest/fio_doc.html>.

## Examples

### Test random reads

```bash
fio --filename=path/to/file --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=job_name --eta-newline=1 --readonly
```

### Test sequential reads

```bash
fio --filename=path/to/file --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=job_name --eta-newline=1 --readonly
```

### Test random read/write

```bash
fio --filename=path/to/file --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=job_name --eta-newline=1
```

### Test with parameters from a job file

```bash
fio path/to/job_file
```

### Convert a specific job file to command-line options

```bash
fio --showcmd path/to/job_file
```
