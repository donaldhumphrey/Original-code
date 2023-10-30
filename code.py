# Write your code here :-)

# these lines import the necessary libraries to run this code
import time
import time
import board
import digitalio
import pwmio

from adafruit_motor import motor #Imports a function from the adafruit_motor library

left_motor_forward = board.GP12 #initializes the variable left_motor_forward and attachees it to GP12
left_motor_backward = board.GP13#initializes the variable left_motor_backward and attachees it to GP13
right_motor_forward = board.GP14
right_motor_backward = board.GP15

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) #tells the controller that the motor is an output
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000) #tells the controller that the motor is an output
pwm_Lc = pwmio.PWMOut(right_motor_forward, frequency=10000)
pwm_Ld = pwmio.PWMOut(right_motor_backward, frequency=10000)

left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Configuration line (it is required)
left_Motor_speed = 0 # Initiates Variable for the left motor speed
right_Motor = motor.DCMotor(pwm_Lc, pwm_Ld)
right_Motor_speed = 0


while True:

    left_Motor_speed = 1 #Makes the left wheel go forward
    left_Motor.throttle = left_Motor_speed
    right_Motor_speed = 1 #Makes the right wheel go forward
    right_Motor.throttle = right_Motor_speed
    time.sleep(2)
    #makes both the left and right wheel move forward

    left_Motor_speed = -1 #Makes the left wheel go backward
    left_Motor.throttle = left_Motor_speed
    right_Motor_speed = -1 #Makes the right wheel go backward
    right_Motor.throttle = right_Motor_speed
    time.sleep(2)
    #makes both the left and right wheel move backward

    left_Motor_speed = 1 #Makes the left wheel go forward
    left_Motor.throttle = left_Motor_speed
    right_Motor_speed = -1 #Makes the right wheel go backward
    right_Motor.throttle = right_Motor_speed
    time.sleep(2)
    #makes the robot turn right

    left_Motor_speed = -1 #Makes the left wheel go backward
    left_Motor.throttle = left_Motor_speed
    right_Motor_speed = 1 #Makes the right wheel go forward
    right_Motor.throttle = right_Motor_speed
    #makes the robot turn left

# Write your code here :-)


