title:::


```bash
@select release-two-$(@timestamp)
cp -v $(python3 -m bluer_ugv locate)/docs/releases/two.yaml ./metadata.yaml

@pdf convert combine,upload .

@assets publish extensions=pdf,push .
```

set:::object_name env:::BLUER_UGV_RELEASE_2

assets:::get:::object_name/release.pdf

details:::metadata
pdf:
metadata:::get:::object_name:::pdf

ignore:
metadata:::get:::object_name:::ignore
details:::