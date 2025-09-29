title:::

## how the sensor works

- Trigger: you send a 10 µs pulse on TRIG.
- Transmit: module emits 8 ultrasonic bursts at 40 kHz.
- ECHO goes HIGH: the instant the bursts are sent, the ECHO pin is driven high.
- ECHO duration: stays high until one of two things happens:
- Echo received → goes low early.
- No ECHO → stays high until the internal timeout (~38 ms), then goes low.

Pulse width: the time ECHO is high equals the round-trip travel time of sound, capped at the timeout.

## why diode-OR of two ECHOs fails

Each sensor always produces a pulse, even on timeout.

With diode-OR, the combined line is high until both sensors drop low.

That means the output reflects the longest pulse (the far/timeout sensor), not the shortest (closest obstacle).

Result: if one sensor sees a nearby hand but the other times out, the shared ECHO line looks like “no object.”

🔥
