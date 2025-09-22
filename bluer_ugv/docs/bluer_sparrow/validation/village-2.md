# bluer-sparrow: validation: village-2

|   |   |   |
| --- | --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_094548.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_094548.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101156.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101156.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101409.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101409.jpg?raw=true) |
| [![image](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101557.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101557.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101653.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101653.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_102822.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_102822.jpg?raw=true) |
| [![image](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101202_1.gif?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-sparrow/20250922_101202_1.gif?raw=true) |  |  |

---

# debug objects


<details>
<summary>collection</summary>

```bash
@ls local,objects --prefix swallow-debug-$(@today)
```

```bash
runme() {
    local object_name
    for object_name in \
        swallow-debug-2025-09-22-09-47-32-85hag3 \
        swallow-debug-2025-09-22-09-59-29-emj29v \
        swallow-debug-2025-09-22-10-01-01-uzray6 \
        swallow-debug-2025-09-22-10-06-19-hcyl1v \
        swallow-debug-2025-09-22-10-09-44-z6q9kn \
        swallow-debug-2025-09-22-10-19-35-mobajm; do
        
        @upload \
	        filename=$object_name.gif,public \
	        $object_name

        @upload \
	        public,zip \
	        $object_name

        @hr
    done
}

runme
```

</details>


gifs:::

🔥

```bash
@ls local,objects --prefix $(@today)
@ls cloud,objects --prefix $(@today)
```

}

runme
🔥
