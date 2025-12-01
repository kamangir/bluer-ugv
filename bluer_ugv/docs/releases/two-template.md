title:::


```bash
@select release-$(@timestamp)
@metadata edit - .

@metadata upload .

@pdf convert combine,upload .

@assets publish extensions=pdf,push .
```

set:::object_name release-2025-11-30-22-48-03-uw8wwl

assets:::get:::object_name/release.pdf

metadata:::get:::object_name:::pdf

details:::ignore-list
metadata:::get:::object_name:::ignore
details:::