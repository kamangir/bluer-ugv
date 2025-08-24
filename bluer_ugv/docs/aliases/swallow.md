# aliases: swallow

## dataset

```bash
@swallow \
	dataset \
	combine \
	[count=<count>,~download,~recent,sequence=<3>,~split,upload] \
	[-|<object-name>] \
	[--datasets <object-name-1>+<object-name-2>] \
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
	list \
	[~download]
 . list the swallow dataset.
@swallow \
	dataset \
	upload \
	[~metadata]
 . upload the swallow dataset.
```

## env

```bash
@swallow \
	env \
	cp \
	[<env-name>]
 . cp swallow swallow-raspbian-<env-name>.
@swallow \
	env \
	list
 . list swallow envs.
@swallow \
	env \
	set \
	steering \
	0 | 1
 . set env.
```
