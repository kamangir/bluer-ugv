# swallow: digital: manual

- to turn the ugv on, flip the led-switch on its side.
- to connect to the ugv, create a WiFi hot spot named `Sion` with the password `HisCatness` and connect to it.
- to view the log of a computer, run,
```bash
@log watch rpi <rpi-name>
```
use the password: `abcli2025`.
- to `ssh` into a computer, run,
```bash
@ssh rpi rpi <rpi-name>
```
or,
```bash
ssh pi@<rpi-name>.local
```
- use the [keyboard](./design/operation.md) to operate the ugv, including shutting it down. 
- to confirm that a computer is shut down either check the log (see ⬆️) or watch the activity led of the computer and validate ten seconds of no green flashes.
- to charge the ugv connect the adapter to the ugv through the [adapter bus](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/battery_bus). stop charging when the intake current is less than 100 mA.
