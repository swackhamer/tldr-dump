# aws-kafka

> Manage an Amazon MSK (Managed Streaming for Apache Kafka) cluster. See also: `aws`. More information: <https://docs.aws.amazon.com/cli/latest/reference/kafka/index.html>.

## Examples

### Create a new MSK cluster

```bash
aws kafka create-cluster --cluster-name cluster_name --broker-node-group-info instanceType=instance_type,clientSubnets=subnet_id1 subnet_id2 ... --kafka-version version --number-of-broker-nodes number
```

### Describe a MSK cluster

```bash
aws kafka describe-cluster --cluster-arn cluster_arn
```

### List all MSK clusters in the current region

```bash
aws kafka list-clusters
```

### Create a new MSK configuration

```bash
aws kafka create-configuration --name configuration_name --server-properties file://path/to/configuration_file.txt
```

### Describe a MSK configuration

```bash
aws kafka describe-configuration --arn configuration_arn
```

### List all MSK configurations in the current region

```bash
aws kafka list-configurations
```

### Update the MSK cluster configuration

```bash
aws kafka update-cluster-configuration --cluster-arn cluster_arn --configuration-info arn=configuration_arn,revision=configuration_revision
```

### Delete the MSK cluster

```bash
aws kafka delete-cluster --cluster-arn cluster_arn
```
