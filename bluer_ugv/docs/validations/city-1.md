# validations: city-1

UGV(s): 🐬 [`arzhang`](../UGVs/arzhang.md)

## objects


<details>
<summary>code</summary>

```bash
@ls cloud,objects --prefix 2025-12-09
```
```text
🌀   7 objects(s)
🌀  #   0 - 2025-12-09-08-16-53-a4rfg2
🌀  #   1 - 2025-12-09-08-52-54-jre3xs
🌀  #   2 - 2025-12-09-09-09-43-ljsjbb
🌀  #   3 - 2025-12-09-10-51-24-2dfnau
🌀  #   4 - 2025-12-09-14-36-28-3o4zvv
🌀  #   5 - 2025-12-09-16-42-23-h1awiz
🌀  #   6 - 2025-12-09-18-52-03-7jo931
```

```bash
runme() {
    local options=$1
    local publish=$(@option::int "$options" publish 1)
    local upload=$(@option::int "$options" upload 1)

    local object_name
    for object_name in $(@ls \
        cloud,objects \
        --log 0 \
        --delim space \
        --prefix 2025-12-09); do

        @select $object_name

        @download policy=doesnt_exist    

        [[ "$upload" == 1 ]] &&
            @upload public,zip

        [[ "$publish" == 1 ]] &&
            @assets publish extensions=png,push
    done
}

runme ~upload
```

```bash
@select 2025-12-09-18-52-03-7jo931
@gif ~download,~upload . --frame_count=200 --output_filename 200.gif
@upload filename=200.gif
@assets publish extensions=gif,push
```

</details>


|   |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
| [`2025-12-09-08-16-53-a4rfg2`](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-08-16-53-a4rfg2.tar.gz) [![image](https://github.com/kamangir/assets/raw/main/2025-12-09-08-16-53-a4rfg2/2025-12-09-08-16-53-a4rfg2.gif)](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-08-16-53-a4rfg2.tar.gz)  | [`2025-12-09-08-52-54-jre3xs`](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-08-52-54-jre3xs.tar.gz) [![image](https://github.com/kamangir/assets/raw/main/2025-12-09-08-52-54-jre3xs/2025-12-09-08-52-54-jre3xs.gif)](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-08-52-54-jre3xs.tar.gz)  | [`2025-12-09-09-09-43-ljsjbb`](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-09-09-43-ljsjbb.tar.gz) [![image](https://github.com/kamangir/assets/raw/main/2025-12-09-09-09-43-ljsjbb/2025-12-09-09-09-43-ljsjbb.gif)](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-09-09-43-ljsjbb.tar.gz)  | [`2025-12-09-10-51-24-2dfnau`](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-10-51-24-2dfnau.tar.gz) [![image](https://github.com/kamangir/assets/raw/main/2025-12-09-10-51-24-2dfnau/2025-12-09-10-51-24-2dfnau.gif)](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-10-51-24-2dfnau.tar.gz)  | [`2025-12-09-14-36-28-3o4zvv`](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-14-36-28-3o4zvv.tar.gz) [![image](https://github.com/kamangir/assets/raw/main/2025-12-09-14-36-28-3o4zvv/2025-12-09-14-36-28-3o4zvv.gif)](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-14-36-28-3o4zvv.tar.gz)  | [`2025-12-09-16-42-23-h1awiz`](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-16-42-23-h1awiz.tar.gz) [![image](https://github.com/kamangir/assets/raw/main/2025-12-09-16-42-23-h1awiz/2025-12-09-16-42-23-h1awiz.gif)](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-16-42-23-h1awiz.tar.gz)  | [`2025-12-09-18-52-03-7jo931`](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-18-52-03-7jo931.tar.gz) [![image](https://github.com/kamangir/assets/raw/main/2025-12-09-18-52-03-7jo931/2025-12-09-18-52-03-7jo931.gif)](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-12-09-18-52-03-7jo931.tar.gz)  |

## debug object


<details>
<summary>code</summary>

```bash
@ls cloud,objects --prefix swallow-debug-2025-12-09
```
```text
🌀   1 objects(s)
🌀  #   0 - swallow-debug-2025-12-09-15-43-31-o6gh5k
```

```bash
runme() {
    local object_name=$(@list resize $(@ls cloud,objects \
    --prefix swallow-debug-2025-12-09 \
    --log 0 \
    --delim ,) \
    1 \
    --delim space)
    @select 
    @assets publish \
        download,extensions=gif,push \
        $object_name
}

runme
```

</details>



| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/swallow-debug-2025-12-09-15-43-31-o6gh5k/swallow-debug-2025-12-09-15-43-31-o6gh5k.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-12-09-18-52-03-7jo931/200.gif?raw=true) |

## observations

1. 1.8 km drive, battery lasted with ~20 minutes of recharge at the middle.
2. ugv steers right when driving forward, likely because of wheel shaft misalignments.

|   |   |
| --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/arzhang/20251209_143603.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/arzhang/20251209_143603.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/arzhang/city-1-path.png?raw=true)](https://github.com/kamangir/assets2/raw/main/arzhang/city-1-path.png?raw=true) |
