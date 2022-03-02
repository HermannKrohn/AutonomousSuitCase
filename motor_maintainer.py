import RPi.GPIO as GPIO     # Import the GPIO library

class MotorMaintainer:
    def __init__(self, left_motor, right_motor, stand_by_pin):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.stand_by_pin = stand_by_pin

        self.setup()

    def setup(self):
        GPIO.setup(self.stand_by_pin, GPIO.OUT)
        GPIO.output(self.stand_by_pin, GPIO.HIGH) # Init standby pin to 1

    def nav_forward(self, speed):
        self.left_motor.forwards(speed)
        self.right_motor.forwards(speed)

    def nav_dynamic_forward(self, left_speed, right_speed):
        self.left_motor.forwards(left_speed)
        self.right_motor.forwards(right_speed)

    def nav_backwards(self, speed):
        self.left_motor.backwards(speed)
        self.right_motor.backwards(speed)

    def nav_brake(self):
        self.left_motor.brake()
        self.right_motor.brake()

    def nav_left(self, left_speed, right_speed):
        self.left_motor.backwards(left_speed)
        self.right_motor.forwards(right_speed)

    def nav_right(self, left_speed, right_speed):
        self.left_motor.forwards(left_speed)
        self.right_motor.backwards(right_speed)

    def cleanup(self):
        self.left_motor.cleanup()
        self.right_motor.cleanup()
