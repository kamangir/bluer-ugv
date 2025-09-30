# same as v4. ⚠️

# continues -v4

from RPi import GPIO
import argparse
import time

parser = argparse.ArgumentParser(__name__)
parser.add_argument(
    "--side",
    type=str,
    help="left | right",
)
args = parser.parse_args()

# Pin definitions
if args.side == "left":
    TRIG = 23  # GPIO 23, pin 16
    ECHO = 24  # GPIO 24, pin 18
elif args.side == "right":
    TRIG = 5  # GPIO 5, pin 29
    ECHO = 25  # GPIO 25, pin 22
else:
    raise ValueError("side must be 'left' or 'right'")

# Constants
C = 343.0  # speed of sound (m/s)
MAX_RANGE_M = 0.8
THRESHOLD_S = (2 * MAX_RANGE_M) / C  # round-trip time for 0.8 m

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print(
    f"Detection threshold = {MAX_RANGE_M*1000:.0f} mm "
    f"(pulse < {THRESHOLD_S*1000:.2f} ms)"
)

try:
    while True:
        # Send trigger pulse (min 10 µs, but Python sleep can undershoot, so use 30 µs)
        GPIO.output(TRIG, True)
        time.sleep(30e-6)
        GPIO.output(TRIG, False)

        # Wait for echo HIGH
        timeout = time.time() + 0.05  # 50 ms max wait
        while GPIO.input(ECHO) == 0 and time.time() < timeout:
            pass
        start_time = time.time()

        # Wait for echo LOW
        while GPIO.input(ECHO) == 1 and time.time() < timeout:
            pass
        end_time = time.time()

        # Calculate pulse width
        pulse_width = end_time - start_time

        if 0 < pulse_width < THRESHOLD_S:
            distance = (pulse_width * C / 2) * 1000  # mm
            print(f"echo detected, distance ≈ {distance:.0f} mm")
        else:
            print("no object")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopped by user")
finally:
    GPIO.cleanup()
