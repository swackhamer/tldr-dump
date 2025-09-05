# gcloud-compute

> Create, run, and manage VMs on Google Cloud infrastructure. See also: `gcloud`. More information: <https://cloud.google.com/sdk/gcloud/reference/compute>.

## Examples

### List Compute Engine zones

```bash
gcloud compute zones list
```

### Create a VM instance

```bash
gcloud compute instances create instance_name
```

### Display a VM instance's details

```bash
gcloud compute instances describe instance_name
```

### List all VM instances in a project

```bash
gcloud compute instances list
```

### Create a snapshot of a persistent disk

```bash
gcloud compute disks snapshot disk_name --snapshot-names snapshot_name
```

### Display a snapshot's details

```bash
gcloud compute snapshots describe snapshot_name
```

### Delete a snapshot

```bash
gcloud compute snapshots delete snapshot_name
```

### Connect to a VM instance using SSH

```bash
gcloud compute ssh instance_name
```
