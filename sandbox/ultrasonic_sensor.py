from RPi import GPIO
import time

# Pin definitions
TRIG = 23  # GPIO 23, pin 16
ECHO = 24  # GPIO 24, pin 18

# Default distance in mm
DISTANCE_MM = 800
# Speed of sound ~ 343 m/s => 0.343 mm/µs
# Time (s) for sound to travel DISTANCE_MM forward+backward:
t_ms = (2 * DISTANCE_MM / 343000.0) * 1000  # in milliseconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print(f"t_ms = {t_ms:.3f} ms for {DISTANCE_MM} mm")

try:
    while True:
        # Send 10 µs pulse on TRIG
        GPIO.output(TRIG, True)
        time.sleep(10e-6)
        GPIO.output(TRIG, False)

        # Wait for ECHO rising edge within t_ms
        start = time.time()
        timeout = start + (t_ms / 1000.0)

        echo_detected = False

        while time.time() < timeout:
            if GPIO.input(ECHO) == 1:
                echo_detected = True
                break

        if echo_detected:
            print("echo detected")

        time.sleep(0.1)  # small delay between triggers

except KeyboardInterrupt:
    print("Stopped by user")
finally:
    GPIO.cleanup()
