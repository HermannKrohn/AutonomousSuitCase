import time
import RPi.GPIO as GPIO     # Import the GPIO library

# Remove if not needed ===============
import keyboard  # using module keyboard
#======================================

GPIO.setmode(GPIO.BOARD) # Use board numbering scheme for GPIO

# PIN constants
STBY_PIN = 15
AIN1_PIN = 13
AIN2_PIN = 11
PWMA_PIN = 32

# Setup GPIO pins
GPIO.setup(STBY_PIN, GPIO.OUT)
GPIO.setup(AIN1_PIN, GPIO.OUT)
GPIO.setup(AIN2_PIN, GPIO.OUT)
GPIO.setup(PWMA_PIN, GPIO.OUT)
pwm_a = GPIO.PWM(PWMA_PIN, 100) # Frequency 1KHz


def main():
    pwm_a.start(0)
    GPIO.output(STBY_PIN, GPIO.HIGH)
    GPIO.output(AIN1_PIN, GPIO.LOW)
    GPIO.output(AIN2_PIN, GPIO.HIGH)

    while(1):
        if keyboard.is_pressed('q'):
            break

        pwm_a.ChangeDutyCycle(100)
        # for i in range(100):
        #     pwm_a.ChangeDutyCycle(i)
        #     time.sleep(1)

    cleanup()


def cleanup():
    pwm_a.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
