import RPi.GPIO as GPIO # Import the GPIO library

class Motor:
    """
    Abstraction class for controlling a single motor using the TB6612FNG 
    motor controller board
    """
    def __init__(self, ain1_pin, ain2_pin, pwm_pin):
        self.ain1_pin = ain1_pin
        self.ain2_pin = ain2_pin
        self.pwm_pin = pwm_pin
        self.pwm_obj = None

        self.setup()

    def setup(self):
        GPIO.setup(self.ain1_pin, GPIO.OUT)
        GPIO.setup(self.ain2_pin, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)

        # Enable pwm on the pwm pin
        # Use a frequency of 1KHz
        # TODO: Use hardware PWM instead of software
        self.pwm_obj = GPIO.PWM(self.pwm_pin, 100)
        self.pwm_obj.start(0) # Init motor with a duty cycle of zero

    def clamp_speed(self, speed):
        if speed > 100:
            speed = 100
            print(f"Invalid speed: {speed}")
        elif speed < 0:
            speed = 0
            print(f"Invalid speed: {speed}")

        return speed


    def forwards(self, speed):
        clamp_speed = self.clamp_speed(speed)
        GPIO.output(self.ain1_pin, GPIO.LOW)
        GPIO.output(self.ain2_pin, GPIO.HIGH)
        self.pwm_obj.ChangeDutyCycle(clamp_speed)

    def backwards(self, speed):
        clamp_speed = self.clamp_speed(speed)
        GPIO.output(self.ain1_pin, GPIO.HIGH)
        GPIO.output(self.ain2_pin, GPIO.LOW)
        self.pwm_obj.ChangeDutyCycle(clamp_speed)

    def brake(self):
        GPIO.output(self.ain1_pin, GPIO.HIGH)
        GPIO.output(self.ain2_pin, GPIO.HIGH)
        self.pwm_obj.ChangeDutyCycle(0)

    def cleanup(self):
        self.pwm_obj.stop()
