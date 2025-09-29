import RPi.GPIO as GPIO
import time

# Pin definitions
TRIG = 23  # GPIO 23, pin 16
ECHO = 24  # GPIO 24, pin 18

# Constants
C = 343.0  # speed of sound (m/s)
MAX_RANGE_M = 1.0  # only detect obstacles closer than 1 m
THRESHOLD_S = (2 * MAX_RANGE_M) / C  # round-trip time for 1 m

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print(
    f"Detection threshold = {MAX_RANGE_M*1000:.0f} mm "
    f"(pulse < {THRESHOLD_S*1000:.2f} ms)"
)

try:
    while True:
        # Send trigger pulse (10 µs)
        GPIO.output(TRIG, True)
        time.sleep(10e-6)
        GPIO.output(TRIG, False)

        # Wait for echo to go HIGH (start of pulse)
        start_time = time.time()
        timeout = start_time + 0.05  # 50 ms safety
        while GPIO.input(ECHO) == 0 and time.time() < timeout:
            start_time = time.time()

        # Wait for echo to go LOW (end of pulse)
        end_time = start_time
        while GPIO.input(ECHO) == 1 and time.time() < timeout:
            end_time = time.time()

        # Calculate pulse width
        pulse_width = end_time - start_time

        # Check if within threshold
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
