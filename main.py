import RPi.GPIO as GPIO # Import the GPIO library
import time

from motor_maintainer import MotorMaintainer
from motor import Motor

# =============
# Pin constants
# =============
LEFT_AIN1_PIN = 13
LEFT_AIN2_PIN = 11
LEFT_PWM_PIN = 32
RIGHT_AIN1_PIN = 29
RIGHT_AIN2_PIN = 31
RIGHT_PWM_PIN = 33
STBY_PIN = 15

# ================
# Global variables
# ================
left_motor = None
right_motor = None
mtr_maintainer = None

def setup():
    global left_motor, right_motor, mtr_maintainer
    GPIO.setmode(GPIO.BOARD) # Use board numbering scheme for GPIO
    left_motor = Motor(LEFT_AIN1_PIN, LEFT_AIN2_PIN, LEFT_PWM_PIN)
    right_motor = Motor(RIGHT_AIN1_PIN, RIGHT_AIN2_PIN, RIGHT_PWM_PIN)
    mtr_maintainer = MotorMaintainer(left_motor, right_motor, STBY_PIN)


def loop():
    while (1):
        mtr_maintainer.nav_forward(50)
        time.sleep(5)
        mtr_maintainer.nav_backwards(50)
        time.sleep(5)
        mtr_maintainer.nav_left(50, 75)
        time.sleep(5)
        mtr_maintainer.nav_right(50, 75)
        time.sleep(5)
        mtr_maintainer.nav_brake()
        time.sleep(5)


def cleanup():
    mtr_maintainer.cleanup()
    GPIO.cleanup()


def main():
    setup()
    try:
        loop()
        cleanup()
    except KeyboardInterrupt:
        cleanup()


if __name__ == "__main__":
    main()
