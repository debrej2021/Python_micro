from machine import Pin
import time

led = Pin(25, Pin.OUT)

for i in range(5):
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

print("Done blinking")
