from pyexpat.errors import XML_ERROR_UNCLOSED_CDATA_SECTION
import RPi.GPIO as GPIO # Import the GPIO library
import time

from motor_maintainer import MotorMaintainer
from motor import Motor
from pixy_wrapper import PixyWrapper

# =============
# Constants
# =============
# Pin constants
LEFT_AIN1_PIN = 13
LEFT_AIN2_PIN = 11
LEFT_PWM_PIN = 32
RIGHT_AIN1_PIN = 29
RIGHT_AIN2_PIN = 31
RIGHT_PWM_PIN = 33
STBY_PIN = 15

# PixyCam block length
PIXY_BLOCK_LEN = 100

# ================
# Global variables
# ================
left_motor = None
right_motor = None
mtr_maintainer = None
pixy_wrap = None

def setup():
    # Init motors
    global left_motor, right_motor, mtr_maintainer, pixy_wrap

    GPIO.setmode(GPIO.BOARD) # Use board numbering scheme for GPIO
    left_motor = Motor(LEFT_AIN1_PIN, LEFT_AIN2_PIN, LEFT_PWM_PIN)
    right_motor = Motor(RIGHT_AIN1_PIN, RIGHT_AIN2_PIN, RIGHT_PWM_PIN)
    mtr_maintainer = MotorMaintainer(left_motor, right_motor, STBY_PIN)

    # Init PixyCam
    pixy_wrap = PixyWrapper(PIXY_BLOCK_LEN)


def loop():
    while (1):
        x_displacement, y_displacement = pixy_wrap.get_dist_from_cam_center()
        if x_displacement == None:
            mtr_maintainer.nav_brake()
            continue

        print(x_displacement, y_displacement)
        if x_displacement > 50:
            mtr_maintainer.nav_right(50, 75)
        elif x_displacement < -50:
            mtr_maintainer.nav_left(50, 75)
        else:
            # dirve forward
            mtr_maintainer.nav_forward(50)

        # mtr_maintainer.nav_forward(50)
        # time.sleep(5)
        # mtr_maintainer.nav_backwards(50)
        # time.sleep(5)
        # mtr_maintainer.nav_left(50, 75)
        # time.sleep(5)
        # mtr_maintainer.nav_right(50, 75)
        # time.sleep(5)
        # mtr_maintainer.nav_brake()
        # time.sleep(5)


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
