from gpiozero import LED
from time import sleep

pin_17 = LED(17)

while True:
    pin_17.on()
    sleep(1)
    pin_17.off()
    sleep(1)
