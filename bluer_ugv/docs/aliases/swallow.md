# swallow

## dataset

```bash
@swallow \
	dataset \
	combine \
	[count=<count>,~download,~recent,~split,upload] \
	[-|<object-name>] \
	[--test_ratio 0.1] \
	[--train_ratio 0.8]
 . combine swallow datasets.
@swallow \
	dataset \
	download \
	[~metadata]
 . download the swallow dataset.
@swallow \
	dataset \
	edit \
	[~download]
 . edit the swallow dataset.
@swallow \
	dataset \
	review \
	[~download,upload] \
	[.|<object-name>]
 . review <object-name>.
@swallow \
	dataset \
	upload \
	[~metadata]
 . upload the swallow dataset.
```
