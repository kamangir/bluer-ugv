title:::

items:::

## debug objects

details:::collection
```bash
@ls local,objects --prefix swallow-debug-$(@today)
```

```bash
runme() {
    local options=$1
    local do_publish_gif=$(@option::int "$options" gif 0)
    local do_upload_object=$(@option::int "$options" object 0)

    local object_name
    for object_name in \
        swallow-debug-2025-09-22-09-47-32-85hag3 \
        swallow-debug-2025-09-22-09-59-29-emj29v \
        swallow-debug-2025-09-22-10-01-01-uzray6 \
        swallow-debug-2025-09-22-10-06-19-hcyl1v \
        swallow-debug-2025-09-22-10-09-44-z6q9kn \
        swallow-debug-2025-09-22-10-19-35-mobajm; do
        
        @log $object_name ...
        
        [[ "$do_publish_gif" == 1 ]] &&
            @assets \
            publish \
            extensions=gif,push \
            $object_name

        [[ "$do_upload_object" == 1 ]] &&
            @upload \
	        public,zip \
	        $object_name

        @hr
    done
}

runme gif
```
details:::

debug_objects:::

## observations

- two wheel nuts loosened every few minutes. ⚠️
- one wheel nut tightened every few minutes. ⚠️

-> fixed in [village-3](./village-3.md)

---

assets:::bluer-sparrow/20250922_101202_1.gif