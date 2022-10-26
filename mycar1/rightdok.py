from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)
servo=14
while True:
    kit.servo[1].angle=35
    kit.continuous_servo[0].throttle =0.2
    sleep(1)
    kit.servo[1].angle=100
    kit.continuous_servo[0].throttle =0
    break
    

