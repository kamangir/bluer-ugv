# releases: two


```bash
@select release-two-$(@timestamp)
cp -v $(python3 -m bluer_ugv locate)/docs/releases/two.yaml ./metadata.yaml

@pdf convert combine,upload .

@assets publish extensions=pdf,push .
```


[release.pdf](https://github.com/kamangir/assets/blob/main/release-two-2025-12-01-12-50-03-1hyrts/release.pdf)


<details>
<summary>metadata</summary>

pdf:
```yaml
{}

```

ignore:
```yaml
{}

```

</details>

