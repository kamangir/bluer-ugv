title:::


```bash
@select release$(@timestamp)
@pdf convert @ugv swallow .
@assets publish extensions=pdf,push .
```

set:::object_name TBA

assets:::get:::object_name/release.pdf