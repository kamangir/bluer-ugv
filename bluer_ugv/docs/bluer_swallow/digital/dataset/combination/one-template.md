# bluer_swallow: digital: dataset: combination: one

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    - .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```

🔥