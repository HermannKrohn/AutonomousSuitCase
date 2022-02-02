import time
import RPi.GPIO as GPIO     # Import the GPIO library

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
    # Initialize pins
    pwm_a.start(0)
    GPIO.output(STBY_PIN, GPIO.HIGH)
    GPIO.output(AIN1_PIN, GPIO.LOW)
    GPIO.output(AIN2_PIN, GPIO.HIGH)

    pwm_a.ChangeDutyCycle(100)
    print("Duty cycle: 100")
    print("AIN1: LOW")
    print("AIN2: HIGH")
    print()
    time.sleep(5)
    pwm_a.ChangeDutyCycle(50)
    print("Duty cycle: 50")
    print("AIN1: LOW")
    print("AIN2: HIGH")
    print()
    time.sleep(5)
    GPIO.output(AIN1_PIN, GPIO.HIGH)
    GPIO.output(AIN2_PIN, GPIO.HIGH)
    print("Duty cycle: 50")
    print("AIN1: HIGH")
    print("AIN2: HIGH")
    print()
    time.sleep(5)
    GPIO.output(AIN1_PIN, GPIO.HIGH)
    GPIO.output(AIN2_PIN, GPIO.LOW)
    print("Duty cycle: 50")
    print("AIN1: HIGH")
    print("AIN2: LOW")
    print()
    time.sleep(5)
    pwm_a.ChangeDutyCycle(100)
    print("Duty cycle: 100")
    print("AIN1: HIGH")
    print("AIN2: LOW")
    print()
    time.sleep(5)
    GPIO.output(AIN1_PIN, GPIO.LOW)
    GPIO.output(AIN2_PIN, GPIO.LOW)
    print("Duty cycle: 100")
    print("AIN1: LOW")
    print("AIN2: LOW")
    print()
    time.sleep(5)

    cleanup()


def cleanup():
    pwm_a.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    main()
