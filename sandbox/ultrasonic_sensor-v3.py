from RPi import GPIO
import time

TRIG = 23
ECHO = 24

C = 343.0  # m/s
MAX_RANGE_M = 1.0
THRESHOLD_S = (2 * MAX_RANGE_M) / C  # round-trip for 1 m (~5.8 ms)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print(
    f"Detection threshold = {MAX_RANGE_M*1000:.0f} mm "
    f"(pulse ends before {THRESHOLD_S*1000:.2f} ms)"
)

try:
    while True:
        # Trigger pulse
        GPIO.output(TRIG, True)
        time.sleep(10e-6)
        GPIO.output(TRIG, False)

        # Wait for echo HIGH
        start_time = time.time()
        timeout = start_time + 0.05
        while GPIO.input(ECHO) == 0 and time.time() < timeout:
            start_time = time.time()

        # Now ECHO is high; wait to see how long it lasts
        echo_detected = False
        while GPIO.input(ECHO) == 1 and time.time() < timeout:
            now = time.time()
            if (now - start_time) < THRESHOLD_S:
                # Fell low early enough -> obstacle
                echo_detected = True
            # loop until pin goes low

        if echo_detected:
            print("echo detected (at least one sensor)")
        else:
            print("no object")

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
