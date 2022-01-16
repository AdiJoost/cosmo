import RPi.GPIO as GPIO


PIN_A_MOTOR_A = 19
PIN_B_MOTOR_A = 26

PIN_A_MOTOR_B = 20
PIN_B_MOTOR_B = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_A_MOTOR_A, GPIO.OUT)
GPIO.setup(PIN_B_MOTOR_A, GPIO.OUT)
GPIO.setup(PIN_A_MOTOR_B, GPIO.OUT)
GPIO.setup(PIN_B_MOTOR_B, GPIO.OUT)


print ("[MOTORSYSTEM]: Setup complete")

def rigth_forward():
    GPIO.output(PIN_A_MOTOR_A,0)
    GPIO.output(PIN_B_MOTOR_A,1)
    return "Motor A forward"

def rigth_backward():
    GPIO.output(PIN_B_MOTOR_A,0)
    GPIO.output(PIN_A_MOTOR_A,1)
    return "Motor A backward"

def rigth_stop():
    GPIO.output(PIN_A_MOTOR_A,0)
    GPIO.output(PIN_B_MOTOR_A,0)
    return "Motor A Stop"

def left_forward():
    GPIO.output(PIN_B_MOTOR_B,0)
    GPIO.output(PIN_A_MOTOR_B,1)
    return "Motor B forward"    

def left_backward():
    GPIO.output(PIN_A_MOTOR_B,0)
    GPIO.output(PIN_B_MOTOR_B,1)
    return "Motor B backward"

def left_stop():
    GPIO.output(PIN_B_MOTOR_B,0)
    GPIO.output(PIN_A_MOTOR_B,0)
    return "Motor B stop"

def clean_board():
    GPIO.cleanup()
    return "Cleanup"